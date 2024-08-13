def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Celsius":
        kelvin = valor + 273.15
        rankine = kelvin * 9/5
        if unidad_destino == "Rankine":
            return rankine
        elif unidad_destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif unidad_destino == "Kelvin":
            return kelvin
    elif unidad_origen == "Fahrenheit":
        rankine = valor + 459.67
        if unidad_destino == "Rankine":
            return rankine
        elif unidad_destino == "Celsius":
            return (valor - 32) * 5/9
        elif unidad_destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "Kelvin":
        rankine = valor * 9/5
        if unidad_destino == "Rankine":
            return rankine
        elif unidad_destino == "Celsius":
            return valor - 273.15
        elif unidad_destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
    elif unidad_origen == "Rankine":
        if unidad_destino == "Celsius":
            kelvin = valor * 5/9
            return kelvin - 273.15
        elif unidad_destino == "Fahrenheit":
            return valor - 459.67
        elif unidad_destino == "Kelvin":
            return valor * 5/9
        elif unidad_destino == "Celsius":
            return (valor - 491.67) * 5/9

valor = float(input("Ingresa el valor de la temperatura: "))
unidad_origen = input("Ingresa la unidad de origen (Celsius, Fahrenheit, Kelvin, Rankine): ")
unidad_destino = input("Ingresa la unidad de destino (Celsius, Fahrenheit, Kelvin, Rankine): ")

resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
print(f"{valor} {unidad_origen} son {resultado:.2f} {unidad_destino}")
