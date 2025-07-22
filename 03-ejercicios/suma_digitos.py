# Crear una función que sume los dígitos de un número.
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

numero = int(input("Digite un número: "))
print(f"La suma de dígitos del número {numero} es {suma_digitos(numero)}")