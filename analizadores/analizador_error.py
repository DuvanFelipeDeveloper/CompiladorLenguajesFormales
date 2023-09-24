import re

def verificar_equilibrio_ruby(codigo):
    stack = []
    lineas = codigo.split("\n")

    for numero_linea, linea in enumerate(lineas, start=1):
        # Buscar patrones de inicio y finalización de estructuras de control
        inicio = re.search(r'\b(if |unless|while|until|for|case|class|def)\b', linea)
        final = re.search(r'\bend\b', linea)

        if inicio:
            stack.append({inicio.group(), numero_linea})
        if final:
            if not stack:
                print(f"Falta un 'end' en la línea {numero_linea}")
                return f"Falta un 'end' en la línea {numero_linea}"
            else:
                stack.pop()

    # Verificar si hay 'end' sin pareja
    for numero_linea,estructura  in stack:
        print(f"falta un end para '{estructura}' en el código linea '{numero_linea}'")
        return f"falta un end para '{estructura}' en el código linea '{numero_linea}'"
      






def validar_estructuras_ruby(codigo_ruby):
    lineas = codigo_ruby.split('\n')
    variables_definidas = set()
    patrones = {
        r'^\s*if\s*(\([^)]+\))?([^:]+)$': "if",
        r'^\s*while\s*(\([^)]+\))?([^:]+)$': "while",
        r'^\s*elsif\s*(\([^)]+\))?([^:]+)$': "elsif",
        r'^\s*unless\s*(\([^)]+\))?([^:]+)$': "unless",
        r'^\s*until\s*(\([^)]+\))?([^:]+)$': "until"
    }

    for numero_linea, linea in enumerate(lineas, start=1):
        for patron, estructura in patrones.items():
            if re.search(r'\b' + estructura + r'\b', linea) and not re.search(r'(["\']).*?\1', linea):
                match = re.match(patron, linea)
                if match:
                    condicion = match.group(2).strip()
                    for token in re.findall(r'\w+|\d+|\S', condicion):
                        if token.isalpha() and token not in variables_definidas and token != "then":
                            print(f"Error en la línea {numero_linea}: La variable '{token}' en la condición del '{estructura}' no está definida en líneas anteriores.")
                            return f"Error en la línea {numero_linea}: La variable '{token}' en la condición del '{estructura}' no está definida en líneas anteriores."
                else:
                    print(f"Error en la línea {numero_linea}: La línea '{linea.strip()}' no tiene la sintaxis correcta de un '{estructura}'.")
                    return f"Error en la línea {numero_linea}: La línea '{linea.strip()}' no tiene la sintaxis correcta de un '{estructura}'."

        # Buscar variables definidas en líneas anteriores
        for variable in re.findall(r'\w+', linea):
            variables_definidas.add(variable)



def validar_for_ruby(codigo_ruby):
    lineas = codigo_ruby.split('\n')
    patron_for = r'^\s*for\s+([a-zA-Z_]\w*)\s+in\s+([a-zA-Z_]\w*|\d+\.\.\d+)\s*$'  # Expresión regular para buscar "for variable in variable_o_rango"

    for numero_linea, linea in enumerate(lineas, start=1):
        if re.search(r'\bfor\b', linea) and not re.search(r'(["\']).*?\1', linea):
            match = re.match(patron_for, linea)
            if match:
                variable = match.group(1)
                variable_o_rango = match.group(2)
                if not variable.isspace():
                    if '..' in variable_o_rango:
                        rangos = variable_o_rango.split('..')
                        if len(rangos) != 2 or not rangos[0].isdigit() or not rangos[1].isdigit():
                            print(f"Error en la línea {numero_linea}: El rango '{variable_o_rango}' después de 'in' no es válido.")
                    elif not variable_o_rango.isalpha():
                        print(f"Error en la línea {numero_linea}: '{variable_o_rango}' después de 'in' no es una variable o un rango válido.")
            else:
                print(f"Error en la línea {numero_linea}: La línea '{linea.strip()}' no tiene la sintaxis correcta de un 'for'.")


# Ejemplo de código Ruby para validar
codigo_ruby = """
x = 5
y = 3

if x > 5
  puts "Mayor que 5"
elsif y < 3
  puts "Menor que 3"
end

z = 0

while (z == 0)
  puts "Igual a 0"
end

puts "Esto no es una estructura de control"

if (a > 10)
  puts "Mayor que 10"
end

puts "Esto tampoco"

while(b < 2)
  puts "Menor que 2"
end

unless(c > 5)
  puts "unless(condicional) es válido"
end

until d > 7
  puts "until(condicional) es válido"
end



for i in 1..5
  puts i
end

for texto in ["a", "b", "c"]
  puts texto
end

for 123 in 1..10
  puts 123
end
"""

# validar_estructuras_ruby(codigo_ruby)
validar_for_ruby(codigo_ruby)











