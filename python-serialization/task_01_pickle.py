#!/usr/bin/env python3
"""Module that will serialize and deserialize a class and its content
    with Pickle"""
import pickle


class CustomObject:
    """Class that represents a custom object, will be serialized later"""
    def __init__(self, name, age, is_student):
        self.__name = name
        self.__age = age
        self.__is_student = is_student

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Is Student: {self.__is_student}")

    def serialize(self, filename):
        try:
            with open(f"{filename}", "wb") as f:
                pickle.dump(self, f)
                return None
        except (IOError, pickle.PicklingError, EOFError, Exception) as e:
            print(f"Cant write in {filename}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                daclass = pickle.load(f)
            return daclass
        except (IOError, pickle.UnpicklingError, EOFError, Exception) as e:
            print(f"Cant read {filename}")
            return None
