#!/usr/bin/env python3
"""Module that will serialize and deserialize a class and its content
    with Pickle"""
import pickle


class CustomObject:
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
        except IOError:
            print(f"Cant write in {filename}")
        except pickle.PicklingError:
            print("Cant serialize the object")
    
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                daclass = pickle.load(f)
            return daclass
        except IOError:
            print(f"Cant read {filename}")
        except pickle.UnpicklingError:
            print("Cant deserialize the object")


# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()