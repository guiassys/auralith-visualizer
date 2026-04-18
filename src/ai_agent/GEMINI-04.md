# AI Agent Prompt: Hardcoded Parameters Refactor

## 🎯 Role & Context

You are an expert Python developer specializing in code refactoring. Your task is to improve the flexibility and maintainability of the Auramove application by removing hardcoded parameters and centralizing them into a configuration file.

## 📝 Task Description

Refactor the existing system to load configuration from a central JSON file, eliminating hardcoded values from the application logic.

### 1. Configuration Layer (`config.json`)

#### 1.1. Centralize Hardcoded Parameters

- **Requirement:** All hardcoded parameters from `@/src/services/animation_service.py` and `@/src/scripts/animate.py` must be moved to `config.json`.
- **Action:**
    - Identify and transfer all hardcoded values to the `config.json` file. This includes, but is not limited to:
        - `total_frames`
        - `frames_per_chunk`
        - `guidance_scale`
        - `num_inference_steps`
        - `width`
        - `height`
        - `fps`
- **Example `config.json` structure:**
    ```json
    {
      "total_frames": 160,
      "frames_per_chunk": 16,
      "guidance_scale": 7.5,
      "num_inference_steps": 40,
      "width": 1024,
      "height": 576,
      "fps": 12
    }
    ```

### 2. Application Logic Layer

#### 2.1. Replace Hardcoded Values

- **Requirement:** Remove all hardcoded configuration values from the Python scripts.
- **Action:**
    - Refactor `@/src/services/animation_service.py` and `@/src/scripts/animate.py` to read the configuration values from `config.json`.
    - Ensure that all parts of the code that previously used hardcoded values now reference the loaded configuration.

#### 2.2. Configuration Loading

- **Requirement:** Implement a robust mechanism to load the configuration.
- **Action:**
    - Apply the Single Responsibility Principle (SRP). Consider creating a dedicated configuration loading utility or class if it simplifies the design and promotes reuse.
    - This utility should handle opening, parsing, and providing access to the configuration data.

### 3. Implementation Details

#### 3.1. File Modification Workflow

- **Steps:**
    1.  **Scan Files:** Analyze `@/src/services/animation_service.py` and `@/src/scripts/animate.py` to locate all hardcoded parameters.
    2.  **Update `config.json`:** Add the identified parameters to the `config.json` file.
    3.  **Refactor Python Code:**
        - Implement the configuration loading logic.
        - Replace each hardcoded value with a call to retrieve the corresponding value from the loaded configuration.
    4.  **Add Comments:** Add clear English comments where the code is modified to explain the change (e.g., "Load parameters from config").

## 🚧 Constraints & Guidelines

- **Minimal Changes:** The primary goal is to refactor the configuration handling. Do not change the core application logic.
- **No Feature Removal:** The code is currently functional, and we want to keep it that way. All existing functionalities must be preserved.
- **Language:** All output, including code comments and documentation, must be in English.
- **Code Quality:** Write clean, readable, and idiomatic Python code.

## 🚀 Final Output

Provide the complete, functional, and ready-to-use source code for the modified files. This includes:

1.  **Updated `config.json`**: Containing all the externalized parameters.
2.  **Modified `@/src/services/animation_service.py`**: With hardcoded values replaced by configuration lookups.
3.  **Modified `@/src/scripts/animate.py`**: With hardcoded values replaced by configuration lookups.

The refactored code should be directly usable and adhere to all specified requirements and constraints.
