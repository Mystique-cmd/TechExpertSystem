# Tech Expert System

This project is a mini expert system for troubleshooting common computer problems. It's built with Python and demonstrates both forward and backward chaining inference methods.

## Features

*   **Knowledge Base:** Stores facts and rules for troubleshooting.
*   **Inference Engine:** Can reason about the knowledge base using:
    *   Forward Chaining: To deduce new facts from existing ones.
    *   Backward Chaining: To find the cause of a specific problem.
*   **Conflict Resolution:** Implements a strategy to handle conflicting rules.
*   **CLI:** A simple command-line interface to interact with the system.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/tech-expert-system.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd tech-expert-system
    ```
3.  **Run the expert system:**
    ```bash
    python src/main/main.py
    ```

## Testing

To run the test suite, use the following command:

```bash
python -m unittest discover src/tests
```
