import re

# Texto de entrada en Ruby
codigo_ruby = """
nombre = "pepe"
numero = 23
texto = "Hola, mundo"
puts "Esto es un mensaje de texto."
puts nombre sdadsad
puts "Otro mensaje de texto."
"""

# Patrón de expresión regular para buscar definiciones de variables en Ruby
patron_variable = r'(\w+)\s*=\s*("[^"]*")'

# Patrón de expresión regular para buscar declaraciones 'puts' con comillas
patron_puts_comillas = r'puts\s*("[^"]*")'

# Patrón de expresión regular para buscar declaraciones 'puts' sin comillas
patron_puts_sin_comillas = r'puts\s+(\w+)'

# Buscar todas las coincidencias de patrones en el código Ruby
coincidencias_variables = re.findall(patron_variable, codigo_ruby)
coincidencias_puts_comillas = re.findall(patron_puts_comillas, codigo_ruby)
coincidencias_puts_sin_comillas = re.findall(patron_puts_sin_comillas, codigo_ruby)

# Almacenar los nombres y valores de las variables en un diccionario
variables = {}
errores = []

for nombre, valor in coincidencias_variables:
    nombre = nombre.strip()
    valor = valor.strip('"')
    variables[nombre] = valor

# Imprimir el valor de las variables cuando se encuentra 'puts' sin comillas
for nombre_variable in coincidencias_puts_sin_comillas:
    nombre_variable = nombre_variable.strip()
    if nombre_variable in variables:
        valor_variable = variables[nombre_variable]
        print(f"Valor de {nombre_variable}: {valor_variable}")
    else:
        print(f"Variable {nombre_variable} no definida")

# Imprimir el texto contenido en las comillas en 'puts' con comillas
for texto in coincidencias_puts_comillas:
    print("Texto en 'puts' con comillas: %s" % texto.strip('\"'))


# Imprimir errores de definición de variable
if errores:
    print("\nErrores de definición de variable:")
    for linea in errores:
        print(f"Error en línea: {linea}")
