# Create a ordered list
list = list(range(1, 101))

def binary_search(list, number):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        average_value = list[mid]
        if average_value == number:
            return mid
        elif average_value < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example of use
number_to_search = int(input("Enter the number to search: "))
index = binary_search(list, number_to_search)
        
if index != -1:
    print(f"The number {number_to_search} is at position {index}")
else:
    print(f"The number {number_to_search} was not found in the list")