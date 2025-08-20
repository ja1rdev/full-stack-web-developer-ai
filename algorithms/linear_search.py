def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input("Enter a number to search: "))
    if linear_search(data, target) != -1:
        print(f"Element {target} found in the list.")
    else:
        print(f"Element {target} not found in the list.")