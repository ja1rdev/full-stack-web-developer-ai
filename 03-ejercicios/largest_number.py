"""umber = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number > number2:
    print("The largest number is:", number)
elif number2 > number:
    print("The largest number is:", number2)
else:
    print("Both numbers are equal.")"""

# Other solution
number = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

numbers = [number, number2, number3]

print("The largest number is:", max(numbers))