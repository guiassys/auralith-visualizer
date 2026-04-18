# 🎧 Auramove

AI-powered Python tool to create stunning animations from images and text prompts. Auramove is designed to be an intuitive platform for artists and creators to bring their static images to life.

---

# 🎯 Objective

To create an automated pipeline capable of:

1.  Generating animated scenes from a single image and a text prompt.
2.  Providing a simple, web-based interface for easy interaction.
3.  Structuring the system in a modular, layered architecture for scalability.
4.  Producing high-quality video outputs ready for publishing.

---

# 🏗️ System Architecture

Auramove is built as a modular, AI-based multimedia generation pipeline.

## 🔹 System Layers

### 1. Animation Generation Layer
- Utilizes state-of-the-art models like AnimateDiff and IP-Adapter.
- Responsible for creating video animations from image and text inputs.

### 2. Service Layer
- The `AnimationService` class orchestrates the generation process.
- It coordinates the inputs from the web interface and manages the AI engine.

### 3. Web Interface Layer
- A user-friendly UI built with Gradio.
- Allows users to upload an image, enter a prompt, and generate an animation.

### 4. Output Layer
- Exports generated animations as `.mp4` files.
- Future support for additional formats and streaming is planned.

## 🔄 System Flow

Image + Prompt → Gradio UI → AnimationService → AnimateDiff Pipeline → Video File (`.mp4`)

---

# ⚙️ How to Run the Project

## Developer Installation (WSL + Ubuntu)
```bash
cd ~/devtools/repos/auralith-visualizer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_web.py
```

## Quick Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/web/app.py
```

## Via Web Interface (Gradio)
```bash
python src/web/app.py
```
Access the interface at: http://localhost:7860

**Web Interface:**
- Enter a project name (e.g., "Angel_Animation").
- Write a descriptive prompt for the scene (e.g., "A beautiful angel flying through the clouds").
- Upload an initial image to guide the animation.
- Click "GENERATE".
- Track the progress in the "Console" tab.
- Download the generated video file once completed.

## Result
The generated video will be saved in the `outputs/animations/` directory.

---

# 📁 Project Structure

```
auralith-visualizer/
├── src/
│   ├── services/         # Application layer
│   │   └── animation_service.py
│   ├── scripts/          # Animation generation pipeline
│   │   └── animate_breathing_loop.py
│   └── web/              # Web interface
│       ├── app.py
│       └── ui_theme.py
├── outputs/              # Generated files
│   └── animations/
├── .gitignore
├── requirements.txt      # Dependencies
└── README.md
```

---

# 📦 Requirements

- Python 3.10+
- PyTorch
- Diffusers (Hugging Face)
- Transformers (Hugging Face)
- Gradio
- OpenCV-Python
- NumPy

---

# 🚧 Project Status

✔ Functional animation generation from image and text  
✔ Modular, layered architecture  
✔ Web interface with Gradio for user input  
✔ Correctly saves generated videos to the output directory  
✔ Execution via web interface  
🚧 Audio-reactivity (in development)  
🚧 Multi-scene story generation (planned)  
🚧 Continuous lo-fi radio integration (planned)  

---

# 🌌 Vision

Auramove is designed to be a scalable system for creating rich, animated worlds. The current implementation is the first step toward a comprehensive platform where music, narrative, and visual identity coexist to create immersive experiences.

---

# 📄 License

This project is proprietary and confidential.  
All rights reserved.