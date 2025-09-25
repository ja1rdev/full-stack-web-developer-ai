def perfects(num):
    
    for number in range(1, num + 1):
        sum_of_divisors = 0

        for i in range(1, number):
            if number % i == 0:
                sum_of_divisors += i

        if sum_of_divisors == number:
            print(f"{number} is a perfect number")

perfects(1000)
