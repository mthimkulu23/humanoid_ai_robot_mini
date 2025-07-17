"""
Simple command line or basic API for interaction.
"""
import threading
import time
from flask import Flask, request, jsonify # Import Flask components

class UserInterface:
    def __init__(self, brain):
        """
        Initializes the UserInterface.
        :param brain: An instance of Brain to send commands to.
        """
        self.brain = brain
        self.running = False
        self.app = Flask(__name__) # Initialize Flask app
        self._setup_routes() # Setup Flask routes
        print("UserInterface initialized.")

    def _setup_routes(self):
        """
        Sets up the Flask routes for the API.
        """
        @self.app.route('/')
        def home():
            return "Humanoid AI Robot Mini API is running!"

        @self.app.route('/command', methods=['POST'])
        def handle_command():
            data = request.get_json()
            command_text = data.get('command')
            if command_text:
                response = self.brain.process_command(command_text)
                return jsonify({"status": "success", "message": response}), 200
            return jsonify({"status": "error", "message": "No command provided"}), 400

        @self.app.route('/status', methods=['GET'])
        def get_status():
            # Assuming brain can provide status or robot_state is accessible
            status_info = {
                "robot_name": self.brain.knowledge_base.get_fact("robot_name"),
                "current_mode": self.brain.current_state, # Using brain's current_state for simplicity
                "battery_level": "N/A" # Placeholder, would get from robot_state
            }
            return jsonify(status_info), 200

    def start_cli(self):
        """
        Starts a simple command-line interface for user input.
        """
        self.running = True
        print("\n--- Humanoid AI Robot Mini CLI ---")
        print("Type commands (e.g., 'hello', 'walk forward', 'what is your name', 'identify object', 'stop').")
        print("Type 'exit' to quit.")
        while self.running:
            try:
                command = input("You: ").strip()
                if command.lower() == 'exit':
                    self.running = False
                    print("Exiting CLI.")
                    break
                if command:
                    # The brain.process_command now returns a response string
                    response = self.brain.process_command(command)
                    print(f"Robot: {response}") # Display robot's response in CLI
            except EOFError: # Handle Ctrl+D
                print("\nExiting CLI.")
                self.running = False
            except KeyboardInterrupt: # Handle Ctrl+C
                print("\nExiting CLI.")
                self.running = False
            time.sleep(0.1) # Prevent busy-waiting

    def start_background_cli(self):
        """
        Starts the CLI in a separate thread.
        """
        cli_thread = threading.Thread(target=self.start_cli)
        cli_thread.daemon = True # Allow main program to exit even if thread is running
        cli_thread.start()
        print("CLI started in background thread.")

    def run_api(self, host='0.0.0.0', port=5000):
        """
        Runs the Flask API.
        """
        print(f"Starting Flask API on http://{host}:{port}")
        self.app.run(host=host, port=port, debug=False, use_reloader=False) # debug=False for production-like behavior
