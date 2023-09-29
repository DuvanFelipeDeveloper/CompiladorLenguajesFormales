import re
import subprocess

# Diccionario para almacenar las variables y sus valores
variables = {}

# Expresiones regulares para detectar declaraciones de variables y usos de variables
variable_declaration_pattern = r"my\s+\$([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*);"
variable_usage_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
patron = r'^\s*puts\s+"[^"]*"'

patron_bloque_datos = r"'\w+' => \{[^}]*\}"
patron_inicio_bloque = r"'[\w\s]+' => \{\s*"
patron_bloque = r"\s*'[\w\s]+' => (?:\{[^}]*\}|\d+\.\d+,\s*)"
patron_bloque_penultimo= r"\s*'[\w\s]+' => (?:\{[^}]*\}|\d+\.\d+\s*)"
patron_fin_bloque = r"\s*\}"
patron_inicio_bloque_personalizado = r"\s*'?\w+'?\s*=>\s*{"

patrondiccionariovar = r"\s*my\s+\$([a-zA-Z_]\w*)\s*=\s*\$([a-zA-Z_]\w*)\s*\*\s*\$([a-zA-Z_]\w*)\{\$([a-zA-Z_]\w*)\}\{\$([a-zA-Z_]\w*)\};"

def evaluate_ruby_line(line):
    match_declaration = re.match(variable_declaration_pattern, line)
    vardiccionario = re.match(patrondiccionariovar, line)



    if(vardiccionario):

        newvar = vardiccionario.group(1)
        amount = vardiccionario.group(2)
        varglobal = vardiccionario.group(3)
        elemnt1 = vardiccionario.group(4)
        elemen2 = vardiccionario.group(5)

        if newvar not in variables:
                try:

                    variables[newvar] = int(variables[amount]) * variables[varglobal][variables[elemnt1].replace("'", "").replace('"', '')][variables[elemen2]]

                    print("codigo ", variables[newvar])
                except Exception as e:
                    mensaje= f"Error crear la variable '{newvar}': {str(e)}"
                    return str(mensaje), 0

    elif match_declaration:
        variable_name = match_declaration.group(1)
        variable_value = match_declaration.group(2)

        if variable_value.replace(".", "", 1).isdigit():
            variables[variable_name] = variable_value
        else:
            if (variable_value.startswith('"') and variable_value.endswith('"')) or \
            (variable_value.startswith("'") and variable_value.endswith("'")):
                variables[variable_name] = variable_value

            elif re.match(r'^\[[^\[\]]*\]$', variable_value):
                patronArray = r'(\d+|"[^"]+"|\w+)'
                coincidenciasArray = re.findall(patronArray, line)
                if coincidenciasArray:
                    coincidenciasArray.pop(0)
                    for coincidencia in coincidenciasArray:
         
                        if coincidencia.isdigit():
                            print(f'{coincidencia} es un número')
                        elif re.match(r'"[^"]+"', coincidencia):
                            print(f'{coincidencia} es una cadena entre comillas')
                        else:
                            mensaje = f"Error: variable al definir variable '{variable_name}' = '{variable_value}'"
                            return str(mensaje), 0
                    variables[variable_name] = variable_value
            else:

                mensaje = f"Error: variable al definir variable '{variable_name}' = '{variable_value}'"
                return str(mensaje), 0
    else:
        match_usage = re.findall(variable_usage_pattern, line)
        for variable_name in match_usage:
            if variable_name not in variables:
                keywords = {"exists", "print", "if","true", "false","for","else", "my"}
                if variable_name not in keywords:
                    if re.match(patron, line):
                        return str(variable_name),1
                    elif ".each do" in line:

                  
                        patronEach = r".*?\.each do \|([^|]+)\|"
                        coincidenciaEach = re.search(patronEach, line)
   
                        if coincidenciaEach:
               
                            texto_extraido = coincidenciaEach.group(1).strip()
                            variables[texto_extraido]=0
                        else:
                            mensaje= f"Error: for each mal definico"


                    else:
                        if not ("print" in line) :
                            mensaje= f"Error: Variable '{variable_name}' no definida"
                            return str(mensaje), 0

    if "print" in line:
        
        output_line = line.replace("print", "").strip()
        print("acaaa",output_line)
        for variable_name, variable_value in variables.items():
            output_line = output_line.replace("$"+variable_name, str(variable_value))
        print("accaaaa 2 " , output_line)
        try:
            result = eval(output_line)
            return str(result), 1
        except Exception as e:
            if not ("converted" in line):
                mensaje= f"Error al evaluar la expresión '{output_line}': {str(e)}"
                return str(mensaje), 0
    return "",3



def compilar(code):
    global variables 
    variables = {} 
    pattern =  r"'(\w+)'\s*=>\s*{([^}]+)}"
    matches = list(re.finditer(pattern, code, re.DOTALL))
    print(matches)
    start_line =99999
    end_line=0
    
    if matches:
     
        for match in matches:
            start_line = code.count('\n', 0, match.start()) -1 if code.count('\n', 0, match.start()) < start_line else start_line
            end_line = code.count('\n', 0, match.end()) +1 if code.count('\n', 0, match.end()) > start_line else start_line

    lines = code.split('\n')
    for index,line in enumerate(lines):
        
        if index >= start_line and index <= end_line:

            lineas_seleccionadas = lines[start_line:end_line+1]
            resultado = '\n'.join(lineas_seleccionadas)
            match = re.search(r'(\w+)\s*=', resultado)

            validacion= procesar_bloques(resultado)
            
            if match and not validacion:
                name =match.group(1)
                if name not in variables:
                    variables[name] = diccionario(code)
            else:
                return validacion
        else:

            evaluate, status = evaluate_ruby_line(line)
            print("aca esta", evaluate, line)
            if status == 0:
                return evaluate    


    output1 = compilarperl(code)
    return output1






def compilarperl(code):
    resultado = subprocess.run(["perl", "-e", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    print("Errores:")
    print(resultado.stderr)

    print("Salida:")
    return resultado.stdout

    


def diccionario(code):
    pattern = r"'(\w+)'\s*=>\s*{([^}]+)}"

    # Encuentra todas las coincidencias en el código Ruby
    matches = re.findall(pattern, code, re.DOTALL)

    # Crea un diccionario en Python a partir de las coincidencias
    exchange_rates_dict = {}
    for match in matches:
        currency = match[0]
        conversion_data = match[1].split(',')
        conversion_dict = {}
        for item in conversion_data:
            key, value = item.split('=>')
            conversion_dict[key.strip()] = float(value.strip())
        exchange_rates_dict[currency] = conversion_dict

    
    return exchange_rates_dict




def verificar_errores_linea_por_linea(bloque, numero_bloque):
    lineas = bloque.strip().split('\n')
    total_lineas = len(lineas)  
    
    for i, linea in enumerate(lineas, start=1):
        if i == 1:
            continue
        if i == total_lineas:  
            if not re.match(patron_fin_bloque, linea.strip()):
                return f"En el bloque {numero_bloque}, línea {i}: El bloque debe finalizar con '}}'"
        elif i == total_lineas - 1: 
            bloque_match = re.match(patron_bloque_penultimo, linea.strip())
            if not bloque_match:
                return f"En el bloque {numero_bloque}, línea {i}: Estructura con ,"
        else:
            bloque_match = re.match(patron_bloque, linea.strip())
            if not bloque_match:
                return f"En el bloque {numero_bloque}, línea {i}: Estructura incompleta."
    
    return None 

def procesar_bloques(hash_str):
    bloques = re.findall(patron_bloque_datos, hash_str)

    for i, bloque in enumerate(bloques, start=1):
        errores_bloque = verificar_errores_linea_por_linea(bloque, i)
        if errores_bloque:
            return errores_bloque
    
    partes_no_coincidentes = re.split(patron_bloque_datos, hash_str)

    # Analizar las partes que no coinciden con bloques
    
    for i, parte in enumerate(partes_no_coincidentes):
        es_linea_valida = verificar_errores_linea_por_linea(parte, i + len(bloques) + 1)
        if es_linea_valida is None:
            x=1
        elif es_linea_valida:
            message =  f"Errores encontrados en la línea {i + len(bloques) + 1}: {es_linea_valida}"
            return message
        else:
            message = f"No se encontraron errores en la línea {i + len(bloques) + 1}."
            return message

    return None
 
