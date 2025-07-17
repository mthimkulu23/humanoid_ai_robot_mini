"""
Stores essential facts and learned information.
"""

class Knowledge:
    def __init__(self):
        """
        Initializes the Knowledge base.
        Can be extended to load from a file or database.
        """
        self._facts = {
            "robot_name": "MiniBot",
            "creator": "AI Assistant",
            "purpose": "Humanoid AI Robot Mini demonstration",
            "known_objects": [] # Example: list of objects the robot has "seen"
        }
        print("Knowledge base initialized.")

    def get_fact(self, key, default=None):
        """
        Retrieves a fact from the knowledge base.
        :param key: The key of the fact to retrieve.
        :param default: Default value if the key is not found.
        :return: The value of the fact or default.
        """
        return self._facts.get(key, default)

    def add_fact(self, key, value):
        """
        Adds or updates a fact in the knowledge base.
        If the key exists and the value is a list, it appends.
        Otherwise, it overwrites.
        """
        if key in self._facts and isinstance(self._facts[key], list) and isinstance(value, str):
            if value not in self._facts[key]:
                self._facts[key].append(value)
        else:
            self._facts[key] = value
        print(f"Fact added/updated: {key} = {value}")

    def remove_fact(self, key):
        """
        Removes a fact from the knowledge base.
        """
        if key in self._facts:
            del self._facts[key]
            print(f"Fact removed: {key}")
        else:
            print(f"Fact '{key}' not found.")

    def get_all_facts(self):
        """
        Returns all facts currently stored.
        """
        return self._facts.copy()
