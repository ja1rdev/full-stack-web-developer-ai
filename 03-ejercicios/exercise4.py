# Exercise 4

import math

radio = float(input("Enter the radius of a circle: "))

area = math.pi * radio**2

length = 2 * math.pi * radio

print(f"The area is {area:.3f}\nThe length of the circumference is {length:.3f}")