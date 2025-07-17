
# Humanoid AI Robot Mini

This is a simplified project for a humanoid AI robot, focusing on core functionalities to provide a manageable starting point.

## Project Structure

The project is organized into the following main modules:

-   `core`: Handles fundamental robot operations and state management.
-   `perception`: Manages sensor input and basic data processing.
-   `cognition`: Contains the robot's "brain" for decision-making and knowledge.
-   `action`: Controls physical movements and interactions.
-   `interface`: Provides a basic user interface for interaction.
-   `data`: Stores models and logs.
-   `utils`: Contains common utility functions.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd humanoid_ai_robot_mini
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Robot

To start the robot's main loop:

```bash
python main.py