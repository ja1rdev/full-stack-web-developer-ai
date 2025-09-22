from collections import Counter

def digitos_dominantes(numero):
    conteo = Counter(str(numero))
    # Frecuencia primero, dígito numérico después
    max_digito = max(conteo.keys(), key=lambda d: (conteo[d], int(d)))
    return int(max_digito)

numero = int(input("Digite un número: "))
print(digitos_dominantes(numero))