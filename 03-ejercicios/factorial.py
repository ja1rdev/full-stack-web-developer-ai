numero = int(input("Ingresar un número, no  negativo para calcular su factorial: "))

if numero < 0:
    print("El factorial no está definido para números negativos")
elif numero == 0 or numero == 1:
    print(f"El factorial de {numero} es ***1***")
else:
    factorial_calculado  = 1
    for i in range(2, numero + 1):
        factorial_calculado *= i
    print(f"El factorial de {numero} es ***{factorial_calculado}***")