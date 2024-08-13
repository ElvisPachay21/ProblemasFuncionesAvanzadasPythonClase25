ponderaciones_positivas = {
    "bien": 1,
    "genial": 2,
    "fantástico": 3,
    "excelente": 3,
    "feliz": 2
}

ponderaciones_negativas = {
    "mal": 1,
    "terrible": 3,
    "horrible": 3,
    "malo": 2,
    "triste": 2
}

def analizar_sentimiento(texto):
    texto = texto.lower()
    
    puntuacion_positiva = sum(ponderaciones_positivas.get(palabra, 0) for palabra in texto.split())
    puntuacion_negativa = sum(ponderaciones_negativas.get(palabra, 0) for palabra in texto.split())
    
    if puntuacion_positiva > puntuacion_negativa:
        return "Sentimiento positivo"
    elif puntuacion_negativa > puntuacion_positiva:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")
