# Exercise 3

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"Initial values a = {a}, b = {b}")

a, b = b, a

print(f"Exchanged values a = {a}, b = {b}")