# AI Agent Prompt: Animation Output System Refactor

## 🎯 Role & Context

You are an expert software engineer tasked with refactoring the animation output system of the Auramove application. Your goal is to enhance flexibility and naming consistency for generated audio assets by eliminating hardcoded paths and standardizing file naming conventions.

## 📝 Task Description

Refactor the existing system to achieve the following objectives:

### 1. Configuration Layer (`config.json`)

#### 1.1. Add Output Directory Parameter

- **Requirement:** The system must support a configurable output directory.
- **Action:**
    - Add a new parameter in the `config.json` file:
    ```json
    {
      "output_directory": "outputs/animations"
    }
    ```
- **Default Behavior:**
    - If the parameter is not defined, the system must fallback to: `outputs/animations`

### 2. Application Logic Layer

#### 2.1. Replace Hardcoded Paths

- **Requirement:** Remove any hardcoded output directory references from the codebase.
- **Action:**
    - Refactor the code to read the `output_directory` value from `config.json`.
    - Ensure all file write operations use this dynamic path.

#### 2.2. Ensure Directory Exists

- **Requirement:** The system must guarantee that the output directory exists before saving files.
- **Action:**
    - Implement a check to verify if the directory exists.
    - If not, automatically create it.

### 3. File Naming Convention

#### 3.1. Standard Naming Format

- **Requirement:** All generated `.wav` files must follow a consistent naming pattern.
- **Format:** `<timestamp>_<name>_v01_gen.wav`
- **Example:** `20260415_014100_aelion_v01_gen.wav`

#### 3.2. Timestamp Format

- **Requirement:** The timestamp must follow a strict format.
- **Format:** `YYYYMMDD_HHMMSS`
- **Example:** `20260415_014100`

#### 3.3. Optional Name Handling

- **Requirement:** The system must handle cases where the user does not provide a name.
- **Behavior:**
    - If a name is provided: `<name>.wav`
    - If no name is provided: `<timestamp>_v01_gen.wav`
- **Example (no name):** `20260415_014100_v01_gen.wav`

### 4. Implementation Details

#### 4.1. Timestamp Generation

- **Requirement:** The system must generate timestamps dynamically at runtime.
- **Action:** Use system time to generate the timestamp in the required format.

#### 4.2. Filename Construction Logic

- **Requirement:** The filename must be dynamically assembled based on user input and timestamp.
- **Action:** Implement conditional logic:
    - If `name` exists → include in filename
    - If `name` is empty or null → omit from filename

#### 4.3. File Saving Workflow

- **Steps:**
    1. Load configuration from `config.json`
    2. Resolve `output_directory`
    3. Ensure directory exists
    4. Generate timestamp
    5. Build filename
    6. Save file to: `<output_directory>/<filename>`

## 🚧 Constraints & Guidelines

- **Minimalist Changes:** Only refactor what is necessary to meet the objectives.
- **No Feature Removal:** All existing functionalities and requirements must be preserved.
- **Language:** All output, including code comments and documentation, must be in English.
- **Current Functionality:** The current code must continue to function correctly after the refactoring.

## 🚀 Final Output

Provide the complete, functional, and ready-to-use source code for the entire Auramove application, structured according to the specified architecture. This includes:

1.  **Updated `config.json`**: Reflecting the new `output_directory` parameter.
2.  **Modified application logic**: Any necessary changes in Python files to read the configuration, replace hardcoded paths, ensure directory existence, and implement the new file naming convention.
3.  **Any other relevant files**: That are impacted by these changes.

The refactored code should be directly usable and adhere to all specified requirements and constraints.
