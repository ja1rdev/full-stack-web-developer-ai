from collections import Counter

def digit_counter(n):
    digits = [int(d) for d in str(n)]
    average = sum(digits) / len(digits)
    frequencie = Counter(digits)
    primes = {2, 3, 5, 7}

    count = 0
    for d in digits:
        if d in primes or d > average or frequencie[d] > 1:
            count += 1
    return count

print(digit_counter(1237))
print(digit_counter(1122))
print(digit_counter(555))
print(digit_counter(8))