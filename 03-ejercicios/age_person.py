from datetime import date

current_date = date.today()

year2 = int(input("Enter your year of birth: "))
month2= int(input("Enter your month of birth: "))
day2= int(input("Enter your day of birth: "))

date_of_birth = date(year2, month2, day2)

age = current_date.year - date_of_birth.year

if (current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day):
    age -= 1

print(age)