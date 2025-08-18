# Verificar si un número es palíndromo (se lee igual al revés)
def es_palindromo(n):
    return str(n) == str(n)[::-1]

n = int(input("Digite un número: "))
print(es_palindromo(n))