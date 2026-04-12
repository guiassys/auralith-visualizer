import torch
from diffusers import AnimateDiffPipeline, MotionAdapter, EulerDiscreteScheduler
from PIL import Image
import os
import cv2
import numpy as np

def export_to_video(frames, output_path, fps=8):
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
    """Generates a single animation scene."""
    # 0. Setup
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    
    # 1. Load models
    adapter = MotionAdapter.from_pretrained("guoyww/animatediff-motion-adapter-v1-5-2", torch_dtype=dtype)
    model_id = "emilianJR/epiCRealism"
    pipe = AnimateDiffPipeline.from_pretrained(model_id, motion_adapter=adapter, torch_dtype=dtype)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, beta_schedule="linear", timestep_spacing="linspace")

    # 2. Load IP-Adapter
    pipe.load_ip_adapter("h94/IP-Adapter", subfolder="models", weight_name="ip-adapter_sd15.bin")
    pipe.set_ip_adapter_scale(0.95)

    # 3. Optimizations for performance
    pipe.enable_vae_slicing()
    if device == "cuda":
        pipe.enable_model_cpu_offload()

    # 4. Define a negative prompt
    negative_prompt = "bad quality, worse quality, low resolution, blurry, noisy, distorted"

    # 5. Generate animation frames
    print(f"Generating animation with prompt: '{prompt}'")
    generator = torch.Generator("cpu" if device == "cuda" else device).manual_seed(42)
    
    output = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        ip_adapter_image=input_image,
        num_frames=16,
        guidance_scale=7.5,
        num_inference_steps=30,
        generator=generator,
        width=1024,
        height=576,
    )
    frames = output.frames[0]
    
    # 6. Export frames to a video file
    export_to_video(frames, output_path)
