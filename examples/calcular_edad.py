from datetime import date

def calcular_edad(anio):
    return date.today().year - anio

anio = int(input("Ingresa tu año de nacimiento: "))
print(f"Tienes: {calcular_edad(anio)} años")