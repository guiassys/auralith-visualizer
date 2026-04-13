# Technical Specification: Auralith Visualizer Application Enhancements

This document details the technical requirements to fix and enhance the Auralith Visualizer application, focusing on issues related to interface functionality, video output quality, and user prompt adherence.

---

## 🎯 Primary Objective

Refactor the existing application to resolve the following issues, treating them as functional and non-functional requirements:

1.  **Functional Requirement:** The video preview component in the web interface must correctly display the generated `.mp4` videos.
2.  **Functional Requirement:** The generated animation must more accurately reflect the instructions provided in the user's text prompt.
3.  **Non-Functional Requirement (Quality):** The visual quality of the generated video must be significantly improved by reducing artifacts, noise, and distortions.
4.  **Non-Functional Requirement (Performance/Duration):** The duration of the generated video must be extended to a minimum of 10 seconds, ensuring the process does not exhaust system memory resources.

---

## 🛠️ Technical Solution Specification

The following modifications must be implemented in the application's architecture.

### 1. Web Interface Layer (`src/web/app.py`)

#### 1.1. Video Component Fix

-   **Location:** `create_ui` function, in the definition of the `gr.Video` component.
-   **Requirement:** The `gr.Video` component must be configured to explicitly declare the video format it will handle.
-   **Technical Action:** Assign the value `"mp4"` to the `format` parameter of the `gr.Video` component's constructor to ensure Gradio uses the correct video player for `.mp4` files.

### 2. AI Engine Layer (`src/scripts/animate.py`)

The issues of quality, duration, and prompt adherence require a reconfiguration of generation parameters and a change in the processing strategy.

#### 2.1. Improvement in Visual Quality and Prompt Adherence

-   **Requirement 1: Increase the Influence of the Text Prompt.** The weight of the input image must be reduced so that the AI model prioritizes the text prompt's instructions.
    -   **Technical Action:** Reduce the value of the `ip_adapter_scale` parameter. The value should be adjusted to a point where the text prompt takes precedence, but the initial image still serves as a coherent base. An initial value of `0.7` is recommended for testing.

-   **Requirement 2: Reduce Artifacts and Visual Flaws.** The model must be instructed to avoid undesirable characteristics in the image.
    -   **Technical Action:** Expand the `negative_prompt` to include a more detailed and comprehensive list of common image generation flaws, such as incorrect anatomy, poor composition, rendering artifacts, and overall low quality.

-   **Requirement 3: Increase Image Refinement.** The generation process must have more iterations to produce a more detailed and polished result.
    -   **Technical Action:** Increase the number of inference steps (`num_inference_steps`). A value around 40 steps is a recommended starting point to balance quality and rendering time.

#### 2.2. Increase in Video Duration

-   **Requirement: Implement Long Video Generation with Controlled Memory Usage.** Video generation must be restructured to support longer durations without causing Out-of-Memory errors.
    -   **Technical Action:** Replace the one-time generation of all frames with a batch processing (chunking) mechanism within the `generate_animation_scene` function.
        1.  The logic must divide the total desired number of frames into smaller, manageable batches (e.g., 16 frames per batch).
        2.  Generation should occur in a loop that processes one batch at a time.
        3.  To ensure continuity and smoothness of the animation, the last frame generated from one batch must be used as the input image (`ip_adapter_image`) for the next batch.
        4.  At the end of the loop, all frames generated in all batches must be aggregated into a single list.
        5.  This list of frames must then be compiled into a single video file.
        6.  Additionally, the frames per second (FPS) rate in the video export function (`export_to_video`) should be increased to approximately 12 FPS to produce a smoother animation.

---

## 🚀 Expected Outcome

The implementation of these specifications will result in a more robust and functional application, capable of producing longer, higher-quality videos that are more aligned with the user's creative intent, with an interface that functions as expected.
