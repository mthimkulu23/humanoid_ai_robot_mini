"""
General utility functions and constants.
"""
import logging
import os

def setup_logging(log_file_path, level_str="INFO"):
    """
    Sets up basic logging for the application.
    :param log_file_path: Path to the log file.
    :param level_str: Logging level as a string (e.g., "INFO", "DEBUG").
    """
    numeric_level = getattr(logging, level_str.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {level_str}')

    # Create log directory if it doesn't exist
    log_dir = os.path.dirname(log_file_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler() # Also log to console
        ]
    )
    logging.info(f"Logging setup with level {level_str} to {log_file_path}")

def get_logger(name):
    """
    Returns a logger instance for a given module name.
    """
    return logging.getLogger(name)

def clamp(value, min_val, max_val):
    """
    Clamps a value between a minimum and maximum.
    :param value: The value to clamp.
    :param min_val: The minimum allowed value.
    :param max_val: The maximum allowed value.
    :return: The clamped value.
    """
    return max(min_val, min(value, max_val))

def degrees_to_radians(degrees):
    """Converts degrees to radians."""
    return degrees * (3.1415926535 / 180.0)

def radians_to_degrees(radians):
    """Converts radians to degrees."""
    return radians * (180.0 / 3.1415926535)

# Example constant
GRAVITY = 9.81 # m/s^2
