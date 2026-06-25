# Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    n = int(input("Enter a number between 1 and 10: "))

    # if n >=1 and n <= 10:
    if 1 <= n <=10:
        print("Valid Input")
        break

    else:
        print("Invalid output")