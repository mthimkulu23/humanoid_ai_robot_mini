"""
Handles specific physical interactions like speaking or grasping.
"""
from gtts import gTTS
import os
import subprocess 

class InteractionController:
    def __init__(self, motor_controller):
        """
        Initializes the InteractionController.
        :param motor_controller: An instance of MotorControl for physical actions.
        """
        self.motor_controller = motor_controller
        print("InteractionController initialized.")

    def speak(self, text):
        """
        Converts a given text into speech and plays it using a system command.
        Uses gTTS for text-to-speech and 'afplay' (macOS) for audio playback.
        :param text: The text string for the robot to speak.
        """
        print(f"Robot says: '{text}' (speaking via TTS and system player)")
        audio_file = "robot_speech.mp3"
        try:
            # Generate speech audio file
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(audio_file)

            
            subprocess.run(["afplay", audio_file], check=True)

            # Clean up the audio file
            os.remove(audio_file)
        except FileNotFoundError:
            print("Error: 'afplay' command not found. Ensure it's in your system's PATH (macOS default).")
            print(f"Robot would have said: '{text}'") 
        except subprocess.CalledProcessError as e:
            print(f"Error playing audio: {e}")
            print(f"Robot would have said: '{text}'") 
        except Exception as e:
            print(f"Error in TTS generation or file handling: {e}")
            print(f"Robot would have said: '{text}'") 
        finally:
            
            if os.path.exists(audio_file):
                os.remove(audio_file)


    def grasp_object(self, object_id):
        """
        Simulates the robot attempting to grasp an object.
        This would involve complex motor sequences.
        :param object_id: Identifier for the object to grasp.
        """
        print(f"Attempting to grasp object: {object_id}")
      
        print(f"Grasping sequence initiated for {object_id}.")
