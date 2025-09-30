import string
import random

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    if length <= 0:
        return "La longitud debe ser un número positivo"
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

length = int(input("Ingrese la logitud de la contraseña: "))
print(password_generator(length))