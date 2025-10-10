def add_numbers():
    entrance = input("Enter numbers separated by spaces: ")
    tokens = entrance.split()

    total_sum = 0
    valid = 0
    invalid = []

    for token in tokens:
        try:
            number = float(token)
            total_sum += number
            valid += 1
        except ValueError:
            invalid.append(token)

    print(f"\nSum: {total_sum}")
    print(f"Valid: {valid}")
    print(f"Invalid: {len(invalid)} -> {invalid}")

add_numbers()