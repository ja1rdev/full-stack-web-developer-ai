def contar_palabras():
    
    frase = input("Ingrese una frase: ")

    texto = frase.lower()

    signos_puntuacion = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for signo in signos_puntuacion:
        texto = texto.replace(signo, ' ')

    palabras = texto.split()

    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    frecuencias_odernadas = sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)

    print("\n--- Resultados ---")

    print(f"Palabras distintas: {len(frecuencias)}")

    print("\nFrecuencias:")
    for palabra, frecuencia in frecuencias_odernadas:
        print(f"{palabra}: {frecuencia}")

contar_palabras()