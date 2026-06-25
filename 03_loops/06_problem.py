# Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter your number: "))
factorial = 1
n = number

while n > 0:
    factorial *= n
    n -= 1

print(f"The factorail of {number} is {factorial}")