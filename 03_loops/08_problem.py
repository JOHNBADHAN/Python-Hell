# Prime Number Checker
# Problem: Check if a number is prime.

n = int(input("Enter your number: "))
is_prime = True

if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            is_prime = False

print(is_prime)