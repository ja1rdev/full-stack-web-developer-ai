def is_reversible(number):    
    inverted_number = int(str(number)[::-1])
    addition = number + inverted_number
    for digit in str(addition):
        if int(digit) % 2 == 0:
            return "No"
    return "Yes"

number = int(input("Enter a number: "))
print(is_reversible(number))