# Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference

a, c = circle(2)
# print("Area:",a, "circumference:", c)
print(f"Area:{a:.2f}, circumference:{c:.2f}")