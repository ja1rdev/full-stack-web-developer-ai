def binary_search(list, number):
    left = 0
    rigth = len(list) - 1

    while left <= rigth:
        mid = (left + rigth) // 2
        if list[mid] == number:
            return mid
        elif list[mid] < number:
            left = mid + 1
        else:
            rigth = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    list = list(range(1, 101))
    number = int(input("Enter a number to search for: "))
    if binary_search(list, number) !=  -1:
        print(f"Number {number} found in the list.")
    else:
        print(f"Number {number} not found in the list.")