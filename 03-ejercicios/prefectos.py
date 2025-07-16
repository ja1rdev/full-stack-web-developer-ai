# Verificar si un número es perfecto (suma de sus divisores propios es igual al número).
def es_numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero

n = int(input("Digite un número: "))
if es_numero_perfecto(n):
    print(f"{n} es un número perfecto")
else:
    print(f"{n} no es un número perfecto")