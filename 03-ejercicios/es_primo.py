# Verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))
if es_primo(n):
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")