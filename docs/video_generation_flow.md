# Auralith Visualizer - Video Generation Flow

This document outlines the step-by-step process of how the Auralith Visualizer application generates an animated video from user inputs.

---

## High-Level Workflow

The application follows a layered architecture to process user requests. The flow begins at the user interface, passes through a service layer that orchestrates the main logic, and is executed by an AI engine. The result is then returned to the user.

1.  **User Input**: The user provides a project name, a text prompt, and an initial image through the Gradio web interface.
2.  **Initiate Generation**: The user clicks the "GENERATE" button.
3.  **Service Orchestration**: The web app calls the `AnimationService` in a background thread. This service manages the entire animation generation task.
4.  **AI Engine Execution**: The service invokes the core AI script (`animate_breathing_loop.py`), which loads the necessary models (AnimateDiff, IP-Adapter) and generates the animation frames.
5.  **Video Export**: The generated frames are encoded into an `.mp4` video file.
6.  **UI Feedback**: The final video is displayed in the web interface, and a download link is provided.

---

## Mermaid Flowchart

The following flowchart provides a visual representation of the entire process.

```mermaid
---
flowchart TD
    subgraph "1. Web Interface (app.py)"
        A --> B[Scene Prompt];
    end

    subgraph "2. UI Backend (app.py)"
        B --> C[run_generation function];
        C --> D{Inputs Valid?};
    end

    subgraph "3. Service Layer (animation_service.py)"
        D -- Yes --> E[Start Background Thread];
        E --> F[AnimationService.generate_animation];
    end

    subgraph "4. AI Engine (animate_breathing_loop.py)"
        F --> G[generate_animation_scene];
        G --> H[Load AnimateDiff & IP-Adapter Models];
        H --> I[Generate Animation Frames];
        I --> J[export_to_video];
    end

    subgraph "5. Output"
        J --> K["<br><b>output.mp4</b><br>Video File<br>"];
    end

    subgraph "6. UI Update"
        K --> L[Return File Path];
        L --> M[Display Video & Download Link];
    end
```
