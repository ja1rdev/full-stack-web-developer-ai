number = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number >= number2 and number >= number3:
    largest = number
elif number2 >= number and number2>= number3:
    largest = number2
else:
    largest = number3

print(f"The largest number is {largest}")