"""
Main entry point for the Humanoid AI Robot Mini application.
This script initializes all core components and starts the robot's main loop.
"""

import threading
import time
import sys

# Import modules from the project structure
from config import (
    SERIAL_PORT, BAUD_RATE, ROBOT_NAME,
    SENSOR_TYPES, LOG_LEVEL, LOG_FILE_PATH,
    UI_MODE
)
from core.hardware_interface import HardwareInterface
from core.robot_state import RobotState
from perception.sensor_input import SensorInput
from perception.data_processing import DataProcessing
from cognition.knowledge import Knowledge
from cognition.brain import Brain
from action.motor_control import MotorControl
from action.interaction import InteractionController
from interface.user_interface import UserInterface
from utils.common import setup_logging, get_logger

def main():
    """
    Initializes the robot system and starts its operation.
    """
    # Setup logging
    setup_logging(LOG_FILE_PATH, LOG_LEVEL)
    logger = get_logger(__name__)
    logger.info(f"Starting {ROBOT_NAME}...")

    # 1. Initialize Core Components
    hardware_interface = HardwareInterface(SERIAL_PORT, BAUD_RATE)
    robot_state = RobotState()

    # 2. Initialize Action Components
    motor_control = MotorControl(hardware_interface)
    interaction_controller = InteractionController(motor_control)

    # 3. Initialize Perception Components
    sensor_input = SensorInput(hardware_interface, SENSOR_TYPES)
    data_processing = DataProcessing()

    # 4. Initialize Cognition Components
    knowledge_base = Knowledge()
    brain = Brain(knowledge_base, data_processing, interaction_controller)

    # Inject motor_control into interaction_controller for brain to use
    interaction_controller.motor_controller = motor_control

    # 5. Initialize User Interface
    user_interface = UserInterface(brain)

    logger.info("All robot components initialized.")
    # Initial greeting through interaction controller
    interaction_controller.speak(f"Hello, I am {ROBOT_NAME}. I am ready.")

    # Start background processes
    # Start sensor input in a separate thread
    sensor_input_thread = threading.Thread(target=sensor_input.start_sensing_loop, daemon=True)
    sensor_input_thread.start()
    logger.info("Sensor input loop started.")

    # Start data processing in a separate thread
    data_processing_thread = threading.Thread(target=data_processing.start_processing_loop, daemon=True)
    data_processing_thread.start()
    logger.info("Data processing loop started.")

    # Start brain's cognitive loop in a separate thread
    brain_loop_thread = threading.Thread(target=brain.run_brain_loop, daemon=True)
    brain_loop_thread.start()
    logger.info("Brain cognitive loop started.")

    # Start the user interface (blocking for CLI, or non-blocking for API)
    if UI_MODE == "CLI":
        user_interface.start_cli() # This will block until 'exit' is typed
    elif UI_MODE == "API":
        # Run Flask app in the main thread (blocking)
        user_interface.run_api(host='0.0.0.0', port=5000) # Listen on all interfaces
    else:
        logger.warning(f"Unknown UI_MODE: {UI_MODE}. Robot running without active UI.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("No UI mode: Ctrl+C detected. Shutting down.")


    logger.info(f"{ROBOT_NAME} shutting down.")
    # Perform cleanup
    hardware_interface.disconnect()
    logger.info("Cleanup complete. Goodbye!")
    sys.exit(0)

if __name__ == "__main__":
    main()
