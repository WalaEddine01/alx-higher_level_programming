#!/usr/bin/python3
class MyClass:
    class_attribute = 10

    def __init__(self, value):
        self.instance_attribute = value

    @classmethod
    def class_method(cls):
        print(f"This is a class method. Class attribute: {cls.class_attribute}")

# Calling a class method on the class itself
MyClass.class_method()

# Creating an instance and calling the class method
obj = MyClass(20)
obj.class_method()

