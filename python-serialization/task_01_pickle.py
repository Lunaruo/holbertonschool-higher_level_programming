#!/usr/bin/env python3
"""
Module for serializing and deserializing custom Python objects.
"""

import pickle


class CustomObject:
    """
    A custom class for demonstrating pickle serialization.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): Person's name.
            age (int): Person's age.
            is_student (bool): Student status.
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file.

        Args:
            filename (str): File to save the object into.
        """

        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): File containing the serialized object.

        Returns:
            CustomObject | None: Deserialized object or None if failed.
        """

        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError,
                EOFError):
            return None
