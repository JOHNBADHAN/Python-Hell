# Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n = int(input("Enter your number: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{n} * {i} = {n*i}")
    # print(n, 'x', i, '=', n * i)