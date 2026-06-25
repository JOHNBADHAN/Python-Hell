# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

color = input("Enter the color of Banana: ").capitalize()

if color == "Green":
    print("Unripe")

elif color == "Yellow":
    print("Ripe")

elif color == "Brown":
    print("Overripe")