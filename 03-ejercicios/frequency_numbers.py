try:
    numbers = input("Enter a list of numbers separated by a comma: ")

    numbers_list = [int(num) for num in numbers.split(",")]

    # print(f"The list of numbers is {list}")

    frequency = {}

    for num in numbers_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
            
    print("\nFrequency of each number:")
    for number, count in frequency.items():
        print(f"The number {number} appears {count} times")

except ValueError:
    print("Error: Make sure you enter whole numbers.")