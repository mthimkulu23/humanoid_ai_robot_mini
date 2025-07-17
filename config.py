"""
Centralized configuration settings for the Humanoid AI Robot Mini.
"""

# Hardware settings
ROBOT_NAME = "MiniBot"
MOTOR_COUNT = 12
SENSOR_TYPES = ["camera", "microphone", "imu"]
SERIAL_PORT = "/dev/ttyUSB0" # Example serial port for hardware communication
BAUD_RATE = 115200

# Perception settings
CAMERA_RESOLUTION = (640, 480)
MIC_SAMPLE_RATE = 44100
OBJECT_DETECTION_MODEL_PATH = "data/models/tiny_yolo.pt" # Placeholder for a small model

# Brain settings
LEARNING_RATE = 0.001
KNOWLEDGE_BASE_FILE = "data/knowledge.json" # Optional: for persistent knowledge

# Log settings
LOG_LEVEL = "INFO" # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE_PATH = "data/logs/robot.log"

# User Interface settings
UI_MODE = "API" # "CLI" for Command Line Interface, "API" for basic API
