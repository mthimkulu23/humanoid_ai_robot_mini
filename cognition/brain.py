"""
Core AI logic: decision-making, simple NLP, basic learning.
"""
import time

class Brain:
    def __init__(self, knowledge_base, perception_data_processor, interaction_controller):
        """
        Initializes the Brain.
        :param knowledge_base: An instance of Knowledge for accessing stored information.
        :param perception_data_processor: An instance of DataProcessing for interpreted sensor data.
        :param interaction_controller: An instance of InteractionController for output.
        """
        self.knowledge_base = knowledge_base
        self.perception_data_processor = perception_data_processor
        self.interaction_controller = interaction_controller
        self.current_state = "idle"
        print("Brain initialized.")

    def process_command(self, command_text):
        """
        Processes a natural language command.
        :param command_text: The command received from the user.
        :return: A string response from the robot.
        """
        print(f"Brain processing command: '{command_text}'")
        command_text = command_text.lower()

        if "hello" in command_text or "hi" in command_text:
            self.interaction_controller.speak("Hello there! How can I help you?")
            return "Hello there! How can I help you?"
        elif "walk forward" in command_text:
            self.interaction_controller.speak("Walking forward now.")
            self.interaction_controller.motor_controller.walk_forward(steps=2)
            return "Walking forward now."
        elif "what is your name" in command_text:
            name = self.knowledge_base.get_fact("robot_name")
            self.interaction_controller.speak(f"My name is {name}.")
            return f"My name is {name}."
        elif "identify object" in command_text:
            self.interaction_controller.speak("Looking for objects now.")
            detected_objects = self.perception_data_processor.get_latest_object_detections()
            if detected_objects:
                self.interaction_controller.speak(f"I see: {', '.join(detected_objects)}.")
                return f"I see: {', '.join(detected_objects)}."
            else:
                self.interaction_controller.speak("I don't see any prominent objects.")
                return "I don't see any prominent objects."
        elif "stop" in command_text:
            self.interaction_controller.speak("Stopping current actions.")
            self.interaction_controller.motor_controller.stop_movement()
            return "Stopping current actions."
        else:
            self.interaction_controller.speak("I'm not sure how to respond to that.")
            return "I'm not sure how to respond to that."

    def make_decision(self):
        """
        Simulates the robot's continuous decision-making process based on its state and perception.
        """
        # Example: If a new object is detected, decide to acknowledge it.
        latest_perceptions = self.perception_data_processor.get_latest_perceptions()
        if latest_perceptions.get("new_object_detected"):
            object_name = latest_perceptions["new_object_detected"]
            if object_name not in self.knowledge_base.get_fact("known_objects", []):
                self.interaction_controller.speak(f"Oh, I see a new {object_name}!")
                self.knowledge_base.add_fact("known_objects", object_name)
                print(f"Brain learned about a new object: {object_name}")

        # Basic state machine example
        if self.current_state == "idle":
            # Check for external commands or internal needs
            pass
        elif self.current_state == "walking":
            # Continue walking or check for obstacles
            pass
        # ... more states

    def update_knowledge(self, new_fact_key, new_fact_value):
        """
        Allows the brain to update its knowledge base.
        """
        self.knowledge_base.add_fact(new_fact_key, new_fact_value)
        print(f"Brain updated knowledge: {new_fact_key} = {new_fact_value}")

    def run_brain_loop(self):
        """
        A continuous loop for the brain's cognitive processes.
        """
        while True:
         
            self.make_decision()
            time.sleep(1) 
