# Generar la secuencia de Fibonacci hasta el n-ésimo término
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    secuencia = [0, 1]
    while len(secuencia) < n:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia

if __name__ == "__main__":
    n = int(input("Ingrese el número de términos: "))
    secuencia = fibonacci(n)
    print(f"Secuencia de Fibonacci para {n} términos: {secuencia}")