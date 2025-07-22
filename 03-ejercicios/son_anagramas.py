# Determinar si palabras/frases son anagramas
def son_anagramas(palabra1, palabra2):
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()
    return sorted(p1) == sorted(p2)

palabra1 = input("Introduzca la 1ra palabra: ")
palabra2 = input("Introduzca la 2da palabra: ")

if son_anagramas(palabra1,palabra2):
    print("Si son anagramas")
else:
    print("No son anagramas")