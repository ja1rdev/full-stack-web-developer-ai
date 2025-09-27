# Definir la funciones
def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        a / b

# Obtener la entradas
try:
    num1 = float(input("Ingresa el primero número: "))
    operador = input("Ingresa la operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))

    if operador == '+':
        resultado = suma(num1, num2)
    elif operador == '-':
        resultado = resta(num1, num2)
    elif operador == '*':
        resultado = multiplicacion(num1, num2)
    elif operador == '/':
        resultado = division(num1, num2)
    else:
        resultado = "Operación no válida"
    
    print(f"El resultado es : {resultado}")

except ValueError:
   print("Entrada no válida. Por favor, ingresa números")