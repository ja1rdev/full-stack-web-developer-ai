import re

def check_passwords(password):

    valid_length = len(password) >= 8

    has_min = bool(re.search(r'[a-z]', password))
    has_may = bool(re.search(r'[A-Z]', password))
    has_num = bool(re.search(r'\d', password))
    has_car = bool(re.search(r'[\W_]', password))

    if not valid_length or password.isalpha() or password.isdigit():
        return "Débil"
    elif has_min and has_may and has_num and has_car:
        return "Fuerte"
    elif has_min and has_num:
        return "Media"
    elif has_may and has_num:
        return "Media"
    else:
        return "Debil"

password = input("Digite una contraseña: ")
print(f"{password} es una contraseña {check_passwords(password)}")