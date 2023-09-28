import re

<<<<<<< HEAD:analizadores/julia/analizador_error.py
=======
# Función para verificar el equilibrio de las estructuras de control en Ruby
>>>>>>> a39ec5a630edb8027575b49cc88b61a5ab8c742e:analizadores/analizador_error.py
def verificar_equilibrio_ruby(codigo):
    stack = []  # Utilizamos una pila para rastrear las estructuras de control abiertas
    lineas = codigo.split("\n")

    for numero_linea, linea in enumerate(lineas, start=1):
<<<<<<< HEAD:analizadores/julia/analizador_error.py
        inicio = re.search(r'\b(if |unless|while|until|for|case|class|def)\b', linea)
=======
        inicio = re.search(r'\b(if|unless|while|until|for|case|class|def)\b', linea)
>>>>>>> a39ec5a630edb8027575b49cc88b61a5ab8c742e:analizadores/analizador_error.py
        final = re.search(r'\bend\b', linea)

        if inicio:
            stack.append((inicio.group(), numero_linea))
        if final:
            if not stack:
                print(f"Falta un 'end' en la línea {numero_linea}")
                return f"Falta un 'end' en la línea {numero_linea}"
            else:
                stack.pop()

        if("if" in linea):
            if "key" in linea:
                pattern = r'if\s+\w+\s*\.key\?\(\w+\)\s*(?:&&\s*\w+\s*\.key\?\(\w+\))?\s*$'
                if re.match(pattern, linea):
                    print("La cadena es válida.")
                else:
                    pattern2 = r'^\s*if\s+\w+\s*\[\w+\]\.key\?\(\w+\)\s*$'
                    if re.match(pattern2, linea):
                        print("La cadena es válida.")
                    else:
                        return f"Error en el if en la línea {numero_linea}"
                    
                    
                
    # Verificar si hay 'end' sin pareja
    for estructura, numero_linea in stack:
        print(f"Falta un 'end' para '{estructura}' en la línea {numero_linea}")
        return f"Falta un 'end' para '{estructura}' en la línea {numero_linea}"
    
    resultado = validar_diccionario_ruby(codigo)
    if resultado:
        return str(resultado)

# Función para validar estructuras de control específicas en Ruby
def validar_estructuras_ruby(codigo_ruby):
    lineas = codigo_ruby.split('\n')
    variables_definidas = set()
    patrones = {
        r'^\s*(if|while|elsif|unless|until)\s*(\([^)]+\))?([^:]+)$': "if/while/unless/until",
    }

    for numero_linea, linea in enumerate(lineas, start=1):
        for patron, estructura in patrones.items():
            if re.search(r'\b' + estructura + r'\b', linea) and not re.search(r'(["\']).*?\1', linea):
                match = re.match(patron, linea)
                if match:
                    condicion = match.group(3).strip()
                    for token in re.findall(r'\w+|\d+|\S', condicion):
                        if token.isalpha() and token not in variables_definidas and token != "then":
                            if not (token == "key"):
                                print(f"Error en la línea {numero_linea}: La variable '{token}' en la condición del '{estructura}' no está definida en líneas anteriores.")
                                return f"Error en la línea {numero_linea}: La variable '{token}' en la condición del '{estructura}' no está definida en líneas anteriores."
                else:
                    print(f"Error en la línea {numero_linea}: La línea '{linea.strip()}' no tiene la sintaxis correcta de un '{estructura}'.")
                    return f"Error en la línea {numero_linea}: La línea '{linea.strip()}' no tiene la sintaxis correcta de un '{estructura}'."

        for variable in re.findall(r'\w+', linea):
            variables_definidas.add(variable)

# Función para validar la estructura de bucles 'for' en Ruby
def validar_for_ruby(codigo_ruby):
    lineas = codigo_ruby.split('\n')
    patron_for = r'^\s*for\s+([a-zA-Z_]\w*)\s+in\s+([a-zA-Z_]\w*|\d+\.\.\d+)\s*$'

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


# Función para validar la estructura de diccionarios en Ruby
def validar_diccionario_ruby(texto):
    patron_corchetes = re.compile(r'[{}]')
    pila_corchetes = []  # Pila para rastrear los corchetes abiertos
    dentro_diccionario = False  # Variable para rastrear si estamos dentro de un diccionario
    lineas = texto.split('\n')
    numero_linea = 0

    for linea in lineas:
        numero_linea += 1
        if re.search(patron_corchetes, linea):
            for caracter in linea:
                if caracter == '{':
                    pila_corchetes.append('{')
                    if not dentro_diccionario and re.search(r'\w+\s*=\s*\{', linea):
                        dentro_diccionario = True
                elif caracter == '}':
                    if not pila_corchetes:
                        return f"Error: Corchete de cierre sin coincidencia en la línea {numero_linea}"
                    pila_corchetes.pop()
    
    if pila_corchetes:
        return "Error: Corchete de apertura sin coincidencia"
    
    if not dentro_diccionario:
        return f"Error: No se encontraron estructuras de diccionario en ninguna línea."
