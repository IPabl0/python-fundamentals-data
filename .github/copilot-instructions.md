# Copilot Instructions for python-fundamentals-data

## Project Overview
This repository is a structured set of Python learning materials, organized by topic and difficulty. It is intended for hands-on practice and self-guided exploration of Python fundamentals and intermediate concepts.

## Directory Structure
- `python_basics/`: Introductory Python scripts covering variables, operators, data types, control flow, functions, classes, exceptions, and modules. Each file focuses on a single concept.
- `python_intermediate/`: Intermediate topics such as dates, list comprehensions, lambdas, higher-order functions, error types, and file handling.
- `exercises/basics_exercises/`: Contains exercises for beginners, with both markdown instructions and Python files for practice.
- `data/`: (Not detailed here; add info if data files are used in exercises.)

## Key Patterns and Conventions
- **File Naming:** Each concept is covered in a separate file (e.g., `01_variables.py`, `2_List_comprehension.py`). Exercise files use the pattern `exercise_XX.py`.
- **Exercises:** Markdown files (e.g., `Excersises.md`) provide instructions. Corresponding `.py` files are for code solutions.
- **No central runner:** Scripts are intended to be run individually. There is no main entry point or build system.
- **No external dependencies:** All code uses only the Python standard library. No requirements.txt or package management is present.
- **No test framework:** There are no automated tests. Validation is manual by running scripts.

## Developer Workflow
- **Run scripts:** Execute any `.py` file directly (e.g., `python python_basics/04_lists.py`).
- **Debugging:** Use print statements or Python debuggers (e.g., `pdb`) as needed. No custom debug tooling.
- **Exercises:** Read the markdown instructions, then implement solutions in the corresponding `.py` file.

## Integration Points
- **Data files:** If used, data files are located in the `data/` directory. Reference them with relative paths.
- **No external APIs or services:** All code is self-contained.

## Example Patterns
- Each script is self-contained and demonstrates a single concept.
- Exercises are paired: instructions in markdown, solutions in `.py`.
- Example: To learn about lists, see `python_basics/04_lists.py`.

## AI Agent Guidance
- When generating new exercises, follow the existing naming and pairing conventions.
- When updating or adding concept files, keep each topic isolated in its own script.
- Avoid introducing external dependencies or test frameworks unless explicitly requested.
- Reference existing files for style and structure.

---

If any section is unclear or missing important project-specific details, please provide feedback or specify additional conventions to document.