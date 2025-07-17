"""
Basic interpretation of sensor data (e.g., object detection, speech-to-text).
"""
import time
import random
import queue

class DataProcessing:
    def __init__(self):
        """
        Initializes the data processing module.
        """
        self.raw_data_queue = queue.Queue()
        self.processed_data = {} # Stores latest processed data
        print("DataProcessing initialized.")

    def add_raw_data(self, sensor_type, data):
        """
        Adds raw sensor data to the processing queue.
        :param sensor_type: Type of sensor (e.g., 'camera', 'microphone').
        :param data: The raw data from the sensor.
        """
        self.raw_data_queue.put({"type": sensor_type, "data": data})

    def process_data(self, sensor_type, raw_data):
        """
        Processes raw data based on sensor type.
        This is where actual AI models would be applied.
        :param sensor_type: Type of sensor.
        :param raw_data: Raw data to process.
        :return: Processed data.
        """
        processed_output = {}
        if sensor_type == 'camera':
            # Simulate object detection
            objects = ["chair", "table", "person", "cup", "book"]
            detected = random.sample(objects, random.randint(0, len(objects)))
            processed_output["objects_detected"] = detected
            if detected:
                processed_output["new_object_detected"] = detected[0] # Signal a new object for brain
            print(f"  [DP] Processed camera data: Detected {detected}")
        elif sensor_type == 'microphone':
            # Simulate speech-to-text
            phrases = ["hello robot", "walk forward", "what is your name", "identify object"]
            if random.random() < 0.3: # Simulate occasional speech detection
                speech_text = random.choice(phrases)
                processed_output["speech_text"] = speech_text
                print(f"  [DP] Processed audio data: Transcribed '{speech_text}'")
            else:
                processed_output["speech_text"] = ""
        elif sensor_type == 'imu':
            # Simulate basic posture analysis from IMU
            processed_output["posture_stable"] = raw_data['accelerometer']['z'] > 9.5
            print(f"  [DP] Processed IMU data: Posture stable = {processed_output['posture_stable']}")

        return processed_output

    def get_latest_perceptions(self):
        """
        Returns the latest processed perception data.
        """
        return self.processed_data.copy()

    def get_latest_object_detections(self):
        """
        Returns the latest detected objects.
        """
        return self.processed_data.get("objects_detected", [])

    def start_processing_loop(self):
        """
        Continuously pulls raw data from the queue and processes it.
        """
        print("DataProcessing loop started.")
        while True:
            try:
                item = self.raw_data_queue.get(timeout=1) # Wait for data for 1 second
                sensor_type = item["type"]
                raw_data = item["data"]
                processed = self.process_data(sensor_type, raw_data)
                self.processed_data.update(processed) # Update overall processed data
            except queue.Empty:
                # print("  [DP] No new raw data to process.")
                pass
            time.sleep(0.05) # Simulate processing time
