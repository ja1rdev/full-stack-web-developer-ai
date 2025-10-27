number = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number % 2 == 0 and number2 % 2 == 0:
    print("Both numbers are even")
elif number % 2 == 0 and number2 % 2 !=0:
    print(f"{number} is even")
elif number != 0 and number2 % 2 == 0:
    print(f"{number2} is even")
else:
    print("Both numbers are odd")