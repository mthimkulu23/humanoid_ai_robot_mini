"""
Commands for all physical movements, including simplified kinematics and gait.
"""

class MotorControl:
    def __init__(self, hardware_interface):
        """
        Initializes the MotorControl system.
        :param hardware_interface: An instance of HardwareInterface for low-level control.
        """
        self.hardware_interface = hardware_interface
        self.joint_positions = {} 
        print("MotorControl initialized.")

    def set_joint_position(self, joint_name, position):
        """
        Sets the target position for a specific joint.
        :param joint_name: Name of the joint (e.g., 'right_shoulder_pitch').
        :param position: Target position (e.g., angle in degrees or radians).
        """
        print(f"Setting joint '{joint_name}' to position: {position}")
        self.hardware_interface.send_motor_command(joint_name, position)
        self.joint_positions[joint_name] = position

    def get_joint_position(self, joint_name):
        """
        Retrieves the current position of a specific joint.
        """
        return self.joint_positions.get(joint_name, 0)

    def move_to_pose(self, pose_data):
        """
        Moves the robot to a predefined pose (collection of joint positions).
        :param pose_data: A dictionary of {joint_name: position}.
        """
        print(f"Moving to pose: {pose_data}")
        for joint, position in pose_data.items():
            self.set_joint_position(joint, position)

    def walk_forward(self, steps=1):
        """
        Simulates a simple forward walking gait.
        In a real robot, this would involve complex gait generation.
        """
        print(f"Initiating forward walk for {steps} steps.")
       
        for i in range(steps):
            print(f"  Step {i+1}...")
           
            self.set_joint_position('left_hip', 10)
            self.set_joint_position('right_knee', -10)
            self.set_joint_position('left_hip', 0)
            self.set_joint_position('right_knee', 0)
        print("Walk completed.")

    def stop_movement(self):
        """
        Stops all current robot movements.
        """
        print("Stopping all motor movements.")
        self.hardware_interface.stop_all_motors()
