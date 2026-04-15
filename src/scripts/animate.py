import torch
from diffusers import AnimateDiffPipeline, MotionAdapter, EulerDiscreteScheduler
from PIL import Image
import os
import cv2
import numpy as np
import json

def load_config():
    """Loads the configuration from config.json."""
    # Load configuration from the root of the project
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)

def export_to_video(frames, output_path, fps):
    """Exports a list of PIL Images to a video file."""
    print(f"Exporting video to {output_path}...")
    if not frames:
        print("No frames to export.")
        return

    first_frame = frames[0]
    width, height = first_frame.size
    # Ensure dimensions are even
    if width % 2 != 0: width -= 1
    if height % 2 != 0: height -= 1

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if not writer.isOpened():
        raise IOError(f"Could not open video writer for path {output_path}.")

    for frame in frames:
        # Resize frame if it doesn't match the writer's dimensions
        if frame.size != (width, height):
            frame = frame.resize((width, height), Image.Resampling.LANCZOS)
        
        frame_bgr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        writer.write(frame_bgr)

    writer.release()
    print("Video saved successfully.")

def generate_animation_scene(prompt, input_image, output_path):
    """Generates a single animation scene in chunks to create a longer video."""
    # 0. Load configuration
    config = load_config()
    anim_config = config.get('animation_settings', {})
    
    # Load parameters from config
    total_frames = anim_config.get('total_frames', 160)
    frames_per_chunk = anim_config.get('frames_per_chunk', 16)
    guidance_scale = anim_config.get('guidance_scale', 7.5)
    num_inference_steps = anim_config.get('num_inference_steps', 40)
    width = anim_config.get('width', 1024)
    height = anim_config.get('height', 576)
    fps = anim_config.get('fps', 12)
    ip_adapter_scale = anim_config.get('ip_adapter_scale', 0.7)

    # 1. Setup device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    
    # 2. Load models
    adapter = MotionAdapter.from_pretrained("guoyww/animatediff-motion-adapter-v1-5-2", torch_dtype=dtype)
    model_id = "emilianJR/epiCRealism"
    pipe = AnimateDiffPipeline.from_pretrained(model_id, motion_adapter=adapter, torch_dtype=dtype)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, beta_schedule="linear", timestep_spacing="linspace")

    # 3. Load IP-Adapter
    pipe.load_ip_adapter("h94/IP-Adapter", subfolder="models", weight_name="ip-adapter_sd15.bin")
    pipe.set_ip_adapter_scale(ip_adapter_scale) # Use value from config

    # 4. Optimizations
    pipe.enable_vae_slicing()
    if device == "cuda":
        pipe.enable_model_cpu_offload()

    # 5. Define a detailed negative prompt
    negative_prompt = "bad quality, worse quality, low resolution, blurry, noisy, distorted, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face"

    # 6. Generate animation frames in chunks
    print(f"Generating animation with prompt: '{prompt}'")
    generator = torch.Generator("cpu" if device == "cuda" else device).manual_seed(42)
    
    all_frames = []
    current_image = input_image

    for i in range(total_frames // frames_per_chunk):
        print(f"Generating chunk {i+1}/{total_frames // frames_per_chunk}...")
        output = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            ip_adapter_image=current_image,
            num_frames=frames_per_chunk,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            generator=generator,
            width=width,
            height=height,
        )
        chunk_frames = output.frames[0]
        all_frames.extend(chunk_frames)
        
        # Use the last frame of the current chunk as the input for the next
        current_image = chunk_frames[-1]

    # 7. Export all collected frames to a single video file
    if all_frames:
        export_to_video(all_frames, output_path, fps=fps) # Use fps from config
    else:
        print("Warning: No frames were generated.")
