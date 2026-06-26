# Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargs(name= "John", age= 21)
kwargs(name= "John", age= 21, hobby= "reading")
kwargs(name= "John")