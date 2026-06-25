# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

str = input("Enter your string: ")

for char in str:
    print(char)
    if str.count(char) == 1:
        print("First non-repeated char is", char)