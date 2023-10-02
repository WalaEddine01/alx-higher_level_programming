#!/usr/bin/python3
class MyClass:
    class_attribute = 10

    def __init__(self, value):
        self.instance_attribute = value

    @staticmethod
    def static_method():
        print(f"This is a static method{MyClass}")

# Calling a static method without an instance
MyClass.static_method()

# Creating an instance and calling the static method
obj = MyClass(20)
obj.static_method()

