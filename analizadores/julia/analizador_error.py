import re

def verificar_equilibrio_julia(codigo):
    stack = []
    lineas = codigo.split("\n")

    for numero_linea, linea in enumerate(lineas, start=1):
        # Buscar palabras clave de inicio y fin en Julia
        inicio = re.search(r'\b(if |while |for |function |struct)\b', linea)
        final = re.search(r'\b(end)\b', linea)

        if inicio:
            stack.append({inicio.group(), numero_linea})
        if final:
            if not stack:
                print(f"Falta un 'end' en la línea {numero_linea}")
                return f"Falta un 'end' en la línea {numero_linea}"
            else:
                stack.pop()
        if("if" in linea):
            if "haskey" in linea:
                pattern = r'if\s+haskey\(\w+,\s*\w+\)\s*(?:&&\s*haskey\(\w+,\s*\w+\))?\s*$'
                if re.match(pattern, linea):
                    print("La cadena es válida.")
                else:
                    pattern2 = r'^\s*if\s+haskey\([^)]+\)\s*$'
                    if re.match(pattern2, linea):
                        print("La cadena es válida.")
                    else:
                        return f"Error en el if en la línea {numero_linea}"


    # Verificar si hay 'end' sin pareja
    for numero_linea, estructura in stack:
        print(f"Falta un end para '{estructura}' en el código, línea '{numero_linea}'")
        return f"Falta un end para '{estructura}' en el código, línea '{numero_linea}'"

    # Llamar a funciones específicas de validación para Julia
    resultado = validar_estructuras_julia(codigo)

    if resultado:
        return str(resultado)


def validar_estructuras_julia(codigo_julia):
    lineas = codigo_julia.split('\n')
    variables_definidas = set()
    patrones = {
        r'^\s*if\s+(.*?)\s*(?:end)?': "if",
        r'^\s*while\s+(.*?)\s*(?:end)?': "while",
        r'^\s*for\s+(.*?)\s+(?:in|=\s*eachpair)\s+(.*?)\s*(?:end)?': "for",
        r'^\s*function\s+(.*?)\s*(?:end)?': "function",
        r'^\s*struct\s+(.*?)\s*(?:end)?': "struct"
    }

    for numero_linea, linea in enumerate(lineas, start=1):
        for patron, estructura in patrones.items():
            if re.search(r'\b' + estructura + r'\b', linea) and not re.search(r'(["\']).*?\1', linea):
                match = re.match(patron, linea)
                if match:
                    condicion = match.group(1).strip()
                    for token in re.findall(r'\w+|\S', condicion):
                        if token.isalpha() and token not in variables_definidas:
                            print(f"Error en la línea {numero_linea}: La variable '{token}' en la condición del '{estructura}' no está definida en líneas anteriores.")
                            return f"Error en la línea {numero_linea}: La variable '{token}' en la condición del '{estructura}' no está definida en líneas anteriores."
                else:
                    print(f"Error en la línea {numero_linea}: La línea '{linea.strip()}' no tiene la sintaxis correcta de un '{estructura}'.")
                    return f"Error en la línea {numero_linea}: La línea '{linea.strip()}' no tiene la sintaxis correcta de un '{estructura}'."

        # Buscar variables definidas en líneas anteriores
        for variable in re.findall(r'\b\w+\b', linea):
            variables_definidas.add(variable)


def validar_diccionario_julia(texto):
    # Expresión regular para buscar corchetes en Julia
    patron_corchetes = re.compile(r'[{}\[\]\(\)]')
    
    # Pila para rastrear los corchetes abiertos
    pila_corchetes = []
    
    # Variable para rastrear si estamos dentro de un diccionario
    dentro_diccionario = False
    
    # Divide el texto en líneas y realiza un seguimiento del número de línea actual
    lineas = texto.split('\n')
    numero_linea = 0
    
    for linea in lineas:
        numero_linea += 1
        # Verifica si la línea contiene corchetes
        if re.search(patron_corchetes, linea):
            for caracter in linea:
                if caracter in "{[(":
                    pila_corchetes.append(caracter)
                    # Si encontramos una '{', '[' o '(', verificamos si estamos dentro de un diccionario
                    if not dentro_diccionario and re.search(r'\w+\s*=\s*(?:Dict\()?\s*\{', linea):
                        dentro_diccionario = True
                elif caracter in "}])":
                    if not pila_corchetes:
                        return f"Error: Corchete de cierre sin coincidencia en la línea {numero_linea}"
                    corchete_abierto = pila_corchetes.pop()
                    if caracter == '}' and corchete_abierto != '{':
                        return f"Error: Falta '{corchete_abierto}' de apertura antes de '}}' en la línea {numero_linea}"
                    elif caracter == ']' and corchete_abierto != '[':
                        return f"Error: Falta '{corchete_abierto}' de apertura antes de ']]' en la línea {numero_linea}"
                    elif caracter == ')' and corchete_abierto != '(':
                        return f"Error: Falta '{corchete_abierto}' de apertura antes de '))' en la línea {numero_linea}"
    
    # Si quedan corchetes sin cerrar en la pila, hay un error
    if pila_corchetes:
        corchetes_abiertos = "".join(pila_corchetes)
        return f"Error: Corchetes de apertura sin coincidencia ({corchetes_abiertos})"

    # Si no se encontraron errores de corchetes y estamos dentro de un diccionario, no hay problemas de sintaxis
    if dentro_diccionario:
        return None
    else:
        return f"Error: No se encontraron estructuras de diccionario en el código"
