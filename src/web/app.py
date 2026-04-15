"""
Professional Web Interface for Auralith using Gradio with a DAW-inspired,
dark-themed layout and real-time log streaming.
"""
import gradio as gr
import logging
import os
import threading
import time
import base64
import json
from src.services.animation_service import AnimationService
from src.web.log_stream import LogStream
from src.web.ui_theme import auralith_theme, custom_css

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Load Configuration ---
def load_config():
    """Loads the application configuration from config.json."""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("config.json not found. Using default settings.")
        return {"output_directory": "outputs/animations"}

config = load_config()
output_dir = config.get("output_directory", "outputs/animations")

# --- Service Initialization ---
animation_service = AnimationService(output_dir=output_dir)

# --- Helper Functions ---
def get_video_html(video_path):
    """Encodes video to Base64 and returns an HTML video tag."""
    if not os.path.exists(video_path):
        return "<div>Video not found.</div>"
    
    with open(video_path, "rb") as video_file:
        encoded_string = base64.b64encode(video_file.read()).decode()
    
    return f"""
    <video width="100%" height="auto" controls autoplay muted loop>
        <source src="data:video/mp4;base64,{encoded_string}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """

# --- UI DEFINITION ---
def create_ui():
    """Builds the Gradio Blocks UI for Auralith Visualizer."""
    with gr.Blocks(title="Auralith Visualizer") as demo:
        # --- Header ---
        with gr.Row(elem_classes=["header"]):
            gr.Markdown("## 🎬 Auralith Visualizer", elem_id="logo")
            with gr.Column(scale=3):
                progress_bar = gr.Slider(label="Rendering Progress", value=0, interactive=False, elem_classes=["glowing-progress"])
        
        with gr.Row():
            # --- Sidebar ---
            with gr.Column(scale=1, min_width=100):
                gr.Markdown("### 🛠️ Tools")
                gr.Button("Studio", variant="primary")
                gr.Button("About")
                gr.Button("Help")

            # --- Main Workspace ---
            with gr.Column(scale=5):
                with gr.Tabs() as tabs:
                    # --- Tab 1: Animation Definitions ---
                    with gr.TabItem("🎬 Animation Definitions", id=0):
                        with gr.Group():
                            name_input = gr.Textbox(label="Project Name", placeholder="e.g., Angel_Animation")
                            prompt_input = gr.Textbox(label="Scene Prompt", placeholder="e.g., A beautiful angel flying through the clouds", lines=3)
                            image_upload = gr.Image(label="Upload Initial Image (Optional)", type="filepath")
                            with gr.Row():
                                clear_btn = gr.Button("🗑️ Clear Inputs")
                                generate_btn = gr.Button("🚀 GENERATE", variant="primary")

                    # --- Tab 2: Studio Console & Output ---
                    with gr.TabItem("🖥️ Studio Console", id=1):
                        status_output = gr.Textbox(label="AI Engine Status", lines=15, interactive=False, elem_classes=["terminal-box"])
                        with gr.Row():
                            file_output = gr.File(label="Download Video", visible=False)
                            video_preview = gr.HTML(label="Animation Preview", visible=False)

        # --- Event Handling & Logic ---
        def run_generation(name, prompt, image):
            """Handles the animation generation process and UI updates."""
            if not prompt:
                gr.Warning("A prompt is required to generate an animation.")
                yield {
                    tabs: gr.update(selected=0),
                    status_output: "Error: A prompt is required.",
                    generate_btn: gr.update(interactive=True),
                    clear_btn: gr.update(interactive=True),
                }
                return

            # Switch to console tab and lock UI
            yield {
                tabs: gr.update(selected=1),
                status_output: "Initializing animation generation...",
                generate_btn: gr.update(interactive=False, value="Generating..."),
                clear_btn: gr.update(interactive=False),
                progress_bar: gr.update(value=0, label="Rendering... 0%")
            }

            log_stream = LogStream()
            log_history = []
            
            gen_config = {
                "name": name, "prompt": prompt, "image_path": image
            }

            generation_task_result = {"result": None}
            def generation_task():
                try:
                    result = animation_service.generate_animation(config=gen_config, log_stream=log_stream)
                    generation_task_result["result"] = result
                finally:
                    log_stream.end()

            thread = threading.Thread(target=generation_task)
            thread.start()

            # Stream logs and update progress
            total_steps = 30 # Animation is slower
            for i, log_message in enumerate(log_stream.stream_generator()):
                log_history.append(log_message)
                progress_val = min(0.95, (i + 1) / total_steps)
                progress_label = f"Rendering... {int(progress_val * 100)}%"
                yield {
                    status_output: "\n".join(log_history),
                    progress_bar: gr.update(value=progress_val, label=progress_label)
                }
                time.sleep(0.1)

            thread.join()
            result = generation_task_result["result"]

            # Final UI update
            if result and result["success"]:
                video_html = get_video_html(result["file_path"])
                log_history.append(f"✅ Generation successful! Output: {result['file_path']}")
                yield {
                    tabs: gr.update(selected=1),
                    status_output: "\n".join(log_history),
                    file_output: gr.update(value=result["file_path"], visible=True),
                    video_preview: gr.update(value=video_html, visible=True),
                    generate_btn: gr.update(interactive=True, value="🚀 GENERATE"),
                    clear_btn: gr.update(interactive=True),
                    progress_bar: gr.update(value=1, label="Rendering Complete")
                }
            else:
                error_msg = result.get('error', "An unknown error occurred.") if result else "An unknown error occurred."
                log_history.append(f"❌ ERROR: {error_msg}")
                gr.Error(f"Generation Failed: {error_msg}")
                yield {
                    tabs: gr.update(selected=1),
                    status_output: "\n".join(log_history),
                    generate_btn: gr.update(interactive=True, value="🚀 GENERATE"),
                    clear_btn: gr.update(interactive=True),
                    progress_bar: gr.update(value=0, label="Rendering Failed")
                }

        generate_btn.click(
            fn=run_generation,
            inputs=[name_input, prompt_input, image_upload],
            outputs=[tabs, status_output, generate_btn, clear_btn, progress_bar, file_output, video_preview]
        )

        def clear_form():
            """Resets all input fields to their default state."""
            return {
                name_input: "",
                prompt_input: "",
                image_upload: None,
                status_output: "",
                file_output: gr.update(visible=False),
                video_preview: gr.update(value=None, visible=False),
                progress_bar: gr.update(value=0, label="Rendering Progress"),
            }

        clear_btn.click(fn=clear_form, outputs=[
            name_input, prompt_input, image_upload, status_output, file_output, video_preview, progress_bar
        ])

    return demo

# --- Main Execution ---
interface = create_ui()

if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        theme=auralith_theme,
        css=custom_css
    )
