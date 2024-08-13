def calcular_propina(total_cuenta, porcentaje_propina):
    """Calcula la propina y el total a pagar dado el total de la cuenta y el porcentaje de propina."""
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

while True:
    try:
        total_cuenta = float(input("Ingresa el total de la cuenta (número positivo): "))
        porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar (número positivo): "))
        
        if total_cuenta < 0 or porcentaje_propina < 0:
            print("Por favor, ingresa números positivos.")
            continue
        
        propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)
        
        num_personas = int(input("Ingresa el número de personas que compartirán la cuenta: "))
        
        if num_personas <= 0:
            print("El número de personas debe ser un número entero positivo.")
            continue
        
        pago_por_persona = total_pagar / num_personas
        
        print(f"Debes dejar una propina de: ${propina:.2f}")
        print(f"El total a pagar es: ${total_pagar:.2f}")
        print(f"Cada persona debe pagar: ${pago_por_persona:.2f}")
        break
    
    except ValueError:
        print("Entrada inválida. Por favor, ingresa valores numéricos válidos.")
