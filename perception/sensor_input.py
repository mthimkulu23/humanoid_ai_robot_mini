"""
Handles raw data acquisition from all sensors (e.g., camera frames, microphone audio, IMU readings).
"""
import time
import threading
from config import SENSOR_TYPES # Import SENSOR_TYPES from config

class SensorInput:
    def __init__(self, hardware_interface, sensor_types=None):
        """
        Initializes the SensorInput module.
        :param hardware_interface: An instance of HardwareInterface to read from.
        :param sensor_types: A list of sensor types to monitor (e.g., ['camera', 'microphone']).
        """
        self.hardware_interface = hardware_interface
        self.sensor_types = sensor_types if sensor_types is not None else []
        self.latest_raw_data = {} # Stores the latest raw data from each sensor
        self.running = False
        print(f"SensorInput initialized for sensors: {self.sensor_types}")

    def read_all_sensors(self):
        """
        Reads data from all configured sensors and updates latest_raw_data.
        """
        for sensor_type in self.sensor_types:
            data = self.hardware_interface.read_sensor_data(sensor_type)
            if data:
                self.latest_raw_data[sensor_type] = data
                # In a real system, you'd push this to a processing queue
                # For this simplified example, we'll assume it's directly accessible
                # or passed to a data processing module.
                # If DataProcessing has an add_raw_data method:
                # from perception.data_processing import DataProcessing
                # DataProcessing().add_raw_data(sensor_type, data)
                # For now, we'll simulate passing it to a global queue or direct call
                # to DataProcessing if it's initialized globally or passed in.
                # In main.py, we'll connect this to DataProcessing.
                pass

    def get_latest_raw_data(self, sensor_type=None):
        """
        Retrieves the latest raw data for a specific sensor or all sensors.
        :param sensor_type: Optional. The type of sensor to get data from.
        :return: Raw sensor data or dictionary of all raw data.
        """
        if sensor_type:
            return self.latest_raw_data.get(sensor_type)
        return self.latest_raw_data.copy()

    def start_sensing_loop(self):
        """
        Starts a continuous loop for reading sensor data.
        This should run in a separate thread.
        """
        self.running = True
        print("SensorInput sensing loop started.")
        while self.running:
            self.read_all_sensors()
            time.sleep(0.1) # Simulate sensor reading frequency (e.g., 10 Hz)
        print("SensorInput sensing loop stopped.")

    def stop_sensing_loop(self):
        """
        Stops the continuous sensor reading loop.
        """
        self.running = False
