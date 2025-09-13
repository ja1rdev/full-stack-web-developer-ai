def round_point(number):
    number_str = str(abs(number)) # Absolute value as string
    n = len(number_str)

    # Validate the length of the number
    if n < 2 or n > 6:
        return "Invalid input"

    original = number_str
    count = 0
    rotated = original

    for _ in range(n):
        # Rotate: move first digit to the end
        rotated = rotated[1:] + rotated[0]
        if rotated == original:
            count += 1
    
    result = "If it meets the condition" if count >= 2 else "Does not meet the condition"
    return f"Output 1: {count}\nOutput 2: {result}"

print(round_point(9992))