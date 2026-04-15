import torch
from diffusers import AnimateDiffPipeline, MotionAdapter, EulerDiscreteScheduler
from PIL import Image
import os
import cv2
import numpy as np
import json
from typing import Optional
from src.web.log_stream import LogStream

def load_config():
    """Loads the configuration from config.json."""
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)

def export_to_video(frames, output_path, fps, log_stream: Optional[LogStream] = None):
    """Exports a list of PIL Images to a video file."""
    def _log(message):
        print(message)
        if log_stream:
            log_stream.log(message)

    _log(f"Exporting video to {output_path}...")
    if not frames:
        _log("No frames to export.")
        return

    first_frame = frames[0]
    width, height = first_frame.size
    if width % 2 != 0: width -= 1
    if height % 2 != 0: height -= 1

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if not writer.isOpened():
        raise IOError(f"Could not open video writer for path {output_path}.")

    for frame in frames:
        if frame.size != (width, height):
            frame = frame.resize((width, height), Image.Resampling.LANCZOS)
        
        frame_bgr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        writer.write(frame_bgr)

    writer.release()
    _log("Video saved successfully.")

def generate_animation_scene(prompt, input_image, output_path, log_stream: Optional[LogStream] = None):
    """Generates a single animation scene in chunks to create a longer video."""
    def _log(message):
        print(message)
        if log_stream:
            log_stream.log(message)

    config = load_config()
    anim_config = config.get('animation_settings', {})
    
    total_frames = anim_config.get('total_frames', 160)
    frames_per_chunk = anim_config.get('frames_per_chunk', 16)
    guidance_scale = anim_config.get('guidance_scale', 7.5)
    num_inference_steps = anim_config.get('num_inference_steps', 40)
    width = anim_config.get('width', 1024)
    height = anim_config.get('height', 576)
    fps = anim_config.get('fps', 12)
    ip_adapter_scale = anim_config.get('ip_adapter_scale', 0.7)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    
    adapter = MotionAdapter.from_pretrained("guoyww/animatediff-motion-adapter-v1-5-2", torch_dtype=dtype)
    model_id = "emilianJR/epiCRealism"
    pipe = AnimateDiffPipeline.from_pretrained(model_id, motion_adapter=adapter, torch_dtype=dtype)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, beta_schedule="linear", timestep_spacing="linspace")

    if input_image:
        _log("IP-Adapter enabled.")
        pipe.load_ip_adapter("h94/IP-Adapter", subfolder="models", weight_name="ip-adapter_sd15.bin")
        pipe.set_ip_adapter_scale(ip_adapter_scale)
    else:
        _log("No initial image provided. IP-Adapter will be disabled.")


    pipe.enable_vae_slicing()
    if device == "cuda":
        pipe.enable_model_cpu_offload()

    negative_prompt = "bad quality, worse quality, low resolution, blurry, noisy, distorted, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face"

    _log(f"Generating animation with prompt: '{prompt}'")
    generator = torch.Generator("cpu" if device == "cuda" else device).manual_seed(42)
    
    all_frames = []
    current_image = input_image

    for i in range(total_frames // frames_per_chunk):
        _log(f"Generating chunk {i+1}/{total_frames // frames_per_chunk}...")
        
        pipe_kwargs = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "num_frames": frames_per_chunk,
            "guidance_scale": guidance_scale,
            "num_inference_steps": num_inference_steps,
            "generator": generator,
            "width": width,
            "height": height,
        }

        if current_image:
            pipe_kwargs["ip_adapter_image"] = current_image

        output = pipe(**pipe_kwargs)
        chunk_frames = output.frames[0]
        all_frames.extend(chunk_frames)
        
        if current_image:
            current_image = chunk_frames[-1]

    if all_frames:
        export_to_video(all_frames, output_path, fps=fps, log_stream=log_stream)
    else:
        _log("Warning: No frames were generated.")
