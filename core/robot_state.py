"""
Manages the robot's current internal status.
"""

class RobotState:
    def __init__(self):
        """
        Initializes the robot's state with default values.
        """
        self._state = {
            "current_pose": {}, # Dictionary of joint_name: position
            "battery_level": 100, # Percentage
            "mode": "idle",       # e.g., "idle", "walking", "interacting"
            "last_command": None,
            "error_status": "OK",
            "location": {"x": 0.0, "y": 0.0, "z": 0.0}, # Simple 3D location
            "orientation": {"roll": 0.0, "pitch": 0.0, "yaw": 0.0} # Euler angles
        }
        print("RobotState initialized.")

    def get_state(self, key=None):
        """
        Retrieves the entire state dictionary or a specific state variable.
        :param key: Optional. The specific state variable to retrieve.
        :return: The state dictionary or the value of the specific variable.
        """
        if key:
            return self._state.get(key)
        return self._state.copy()

    def set_state(self, key, value):
        """
        Sets the value of a specific state variable.
        :param key: The state variable to set.
        :param value: The new value for the variable.
        """
        if key in self._state:
            self._state[key] = value
            print(f"RobotState updated: {key} = {value}")
        else:
            print(f"Warning: Attempted to set unknown state variable '{key}'.")

    def update_pose(self, joint_name, position):
        """
        Updates a specific joint position in the current pose.
        """
        self._state["current_pose"][joint_name] = position
        # print(f"Pose updated: {joint_name} = {position}")

    def update_battery_level(self, level):
        """
        Updates the battery level.
        :param level: New battery level (0-100).
        """
        self._state["battery_level"] = max(0, min(100, level))
        print(f"Battery level: {self._state['battery_level']}%")

    def set_mode(self, mode):
        """
        Sets the robot's operational mode.
        """
        valid_modes = ["idle", "walking", "interacting", "error"]
        if mode in valid_modes:
            self._state["mode"] = mode
            print(f"Robot mode set to: {mode}")
        else:
            print(f"Warning: Invalid robot mode '{mode}'.")

    def get_current_mode(self):
        """
        Returns the robot's current operational mode.
        """
        return self._state["mode"]
