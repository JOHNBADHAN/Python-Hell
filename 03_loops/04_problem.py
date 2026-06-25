# Reverse a String
# Problem: Reverse a string using a loop.

str = input("Enter your string: ")
reversed_str = ""

for char in str:
    reversed_str = char + reversed_str

print(reversed_str)

# Using join

str = input("Enter your string: ")
reversed_str = "".join(reversed(str))
print(reversed_str)

# Using slicing

str = input("Enter your string: ")
reversed_str = str[::-1]
print(reversed_str)

# function

def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))