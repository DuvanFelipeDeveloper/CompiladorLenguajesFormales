
import re

entrada_ruby = """
valor = 10

if 3 < 4
  puts "El valor es mayor que 10"
elsif valor == 10
  puts "El valor es igual a 10"
else
  puts "Ninguna condición es verdadera"
end
"""

# Dividir la entrada en líneas
lineas = entrada_ruby.split('\n')

# Bandera para indicar si estamos dentro de una estructura 'if'
en_if = False

# Patrón de expresión regular para buscar condiciones en 'if' o 'elsif'
patron_condicion = r'\b(if|elsif)\s+(.+)\s*$'

for linea in lineas:
    match = re.search(patron_condicion, linea)
    if match:
        tipo = match.group(1)
        condicion = match.group(2)
        
        # Dividir la condición en sus componentes: valor uno, operador lógico y valor dos
        patron_operadores = r'(\S+)\s*([<>=]+)\s*(\S+)'
        match_operadores = re.search(patron_operadores, condicion)
        
        if match_operadores:
            valor_uno = match_operadores.group(1)
            operador = match_operadores.group(2)
            valor_dos = match_operadores.group(3)
            
            print(f"{tipo}: Valor Uno = {valor_uno}, Operador = {operador}, Valor Dos = {valor_dos}")
        else:
            print(f"{tipo}: La condición '{condicion}' no se pudo analizar correctamente.")
