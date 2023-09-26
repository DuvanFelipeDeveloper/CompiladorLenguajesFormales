import re

# Cadena de entrada
cadena = "converted_amount = amount * exchange_rates[from_currency][to_currency]"

# Definir la expresión regular para separar la cadena
patron = r'^\s*(\w+)\s*=\s*(\w+)\s*\*\s*(\w+)\[(\w+)\]\[(\w+)\]'

# Buscar coincidencias en la cadena
coincidencias = re.match(patron, cadena)

if coincidencias:
    # Extraer las partes en variables
    resultado_variable = coincidencias.group(1)
    amount_variable = coincidencias.group(2)
    operador_multiplicacion = coincidencias.group(3)
    exchange_rates_variable = coincidencias.group(4)
    from_currency_variable = coincidencias.group(5)


    # Imprimir las partes
    print(f"Resultado variable: {resultado_variable}")
    print(f"Amount variable: {amount_variable}")
    print(f"Operador multiplicación: {operador_multiplicacion}")
    print(f"Exchange rates variable: {exchange_rates_variable}")
    print(f"From currency variable: {from_currency_variable}")

else:
    print("No se encontró ninguna coincidencia")
