# Tech Expert System

This project is a simple expert system for troubleshooting common computer problems. It's built with Python and uses a forward-chaining inference engine to deduce solutions from a set of given symptoms. The user interface is a web application powered by Streamlit.

## Features

*   **Knowledge Base:** Stores facts and rules for troubleshooting computer issues.
*   **Inference Engine:** Reasons about the knowledge base using forward chaining to deduce new facts.
*   **Conflict Resolution:** Implements a priority-based strategy to handle conflicting rules.
*   **Web UI:** A simple and interactive web interface built with Streamlit to guide users through the troubleshooting process.

## Getting Started

### Prerequisites

*   Python 3.7+
*   pip

### Installation and Running the Application

1.  **Navigate to the project's `main` directory:**
    ```bash
    cd src/main
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the expert system:**
    ```bash
    streamlit run main.py
    ```
This will start the Streamlit web application in your browser.

## Testing

To run the test suite, navigate to the project's root directory and use the following command:

```bash
python -m unittest discover src/tests
```

## Project Structure

```
.
├── src
│   ├── main
│   │   ├── __init__.py
│   │   ├── inference_engine.py   # Core logic for the inference engine (forward/backward chaining)
│   │   ├── knowledge_base.py     # Manages the facts and rules
│   │   ├── main.py               # Main application file with the Streamlit UI
│   │   ├── requirements.txt      # Project dependencies
│   │   └── rule.py               # Defines the structure of a rule
│   └── tests
│       ├── __init__.py
│       └── test_expert_system.py # Unit tests for the expert system
├── .gitignore
└── README.md
```