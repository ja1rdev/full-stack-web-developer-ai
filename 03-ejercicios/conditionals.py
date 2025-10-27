age = int(input("Enter your age: "))

if age > 0:
    print("Age is valid.")
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
else:
    print("Age is not valid.")