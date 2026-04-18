# AI Agent Prompt: Settings Tab Implementation

## 🎯 Role & Context

You are an expert Python developer specializing in building user interfaces with the Gradio library. Your task is to add a new feature to the Auramove application, allowing users to configure system parameters through the interface.

## 📝 Task Description

Create a new "Settings" tab in the Gradio application. This tab will display system configuration parameters, allowing the user to modify them before starting the animation generation process.

### 1. User Interface (UI) Layer

#### 1.1. Create the Settings Tab

- **Requirement:** Add a new tab named "Settings" to the main application interface.
- **Action:**
    - Inside this new tab, create UI components (e.g., text boxes, sliders) for each of the configuration parameters.
    - Visually organize the components to mirror the structure of the configuration JSON, separating "Generator Settings" and "Animation Settings".
    - The initial values displayed in the UI must be loaded from a central configuration file (`config.json`).

### 2. Configuration Layer

#### 2.1. `config.json` Structure

- **Requirement:** The `config.json` file must be the central source for the default configuration values.
- **Action:**
    - Ensure the `config.json` file exists and contains the following structure and default values:
    ```json
    {
        "generator_settings": {
            "chunk_duration": 10,
            "overlap_duration": 2,
            "fade-out_duration": 2
        },
        "output_directory": "outputs/animations",
        "animation_settings": {
            "total_frames": 32,
            "frames_per_chunk": 16,
            "guidance_scale": 7.5,
            "num_inference_steps": 40,
            "width": 1024,
            "height": 576,
            "fps": 12,
            "ip_adapter_scale": 0.7
        }
    }
    ```

### 3. Application Logic Layer

#### 3.1. UI Parameter Integration

- **Requirement:** The animation generation logic must use the values set by the user in the "Settings" tab.
- **Action:**
    - Modify the function triggered by the "Generate" button.
    - Before executing the animation, the function must collect the current values from all UI components in the "Settings" tab.
    - Pass these values as arguments to the services or scripts responsible for animation generation (e.g., `animation_service.py`).

## 🚧 Constraints & Guidelines

- **Minimal Changes:** The primary goal is to add the new settings tab. Do not change the core application logic unless it is to pass the new parameters.
- **No Feature Removal:** The application is currently functional and must remain so. All existing functionalities must be preserved.
- **Language:** All output, including code, comments, and documentation, must be in English.
- **Code Quality:** Write clean, readable, and idiomatic Python code.
- **File Modification Workflow:**
    1.  **Analyze UI File:** Identify the main Gradio application file (e.g., `app.py`).
    2.  **Update UI:** Add the "Settings" tab and its components.
    3.  **Update Logic:** Modify the "Generate" button's callback function to read from the new UI components and pass them to the backend services.
    4.  **Add Comments:** Add clear English comments where the code is modified to explain the change (e.g., "Load parameters from settings tab").

## 🚀 Final Output

Provide the complete, functional, and ready-to-use source code for the modified files. This includes, but is not limited to:

1.  **The Gradio UI file (likely `app.py` or similar):** Updated with the new "Settings" tab and its components.
2.  **The `config.json` file:** Containing the default configuration parameters.
3.  **Any other modified files:** Such as `services/animation_service.py`, to receive the new parameters from the UI.

The refactored code should be directly usable and adhere to all specified requirements and constraints.
