# Calculadora que permita realizar operaciones aritméticas básicas.
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else "Error: División entre 0"

while True:
    print("\nCalculadora aritmética...")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Por favor. Ingresa un número del 1 a 5.")
        continue

    if 1 <= opcion <= 4:
        try:
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
        except ValueError:
            print("Debes ingresar números enteros.")
            continue
        
        if opcion == 1:
            print("Suma =",sumar(a, b))
        elif opcion == 2:
            print("Resta =", restar(a, b))
        elif opcion == 3:
            print("Multiplicación =", multiplicar(a, b))
        elif opcion == 4:
            print("División =", dividir(a, b))
    elif opcion == 5:
        print("Saliendo de la calculadora...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")