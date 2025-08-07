numbers = [1,2,3,4,5]
search = int(input("Enter number: "))

if search in numbers:
    print(f"The number {search} found.")
else:
    print("The number not found.")