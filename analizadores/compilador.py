import re

# Diccionario para almacenar las variables y sus valores
variables = {}

# Expresiones regulares para detectar declaraciones de variables y usos de variables
variable_declaration_pattern = r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*)$'
variable_usage_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
patron = r'^\s*puts\s+"[^"]*"'

patron_bloque_datos = r"'\w+' => \{[^}]*\}"
patron_inicio_bloque = r"'[\w\s]+' => \{\s*"
patron_bloque = r"\s*'[\w\s]+' => (?:\{[^}]*\}|\d+\.\d+,\s*)"
patron_bloque_penultimo= r"\s*'[\w\s]+' => (?:\{[^}]*\}|\d+\.\d+\s*)"
patron_fin_bloque = r"\s*\}"



patrondiccionariovar = r'^\s*(\w+)\s*=\s*(\w+)\s*\*\s*(\w+)\[(\w+)\]\[(\w+)\]'
# Función para evaluar una línea de código Ruby
def evaluate_ruby_line(line):
    match_declaration = re.match(variable_declaration_pattern, line)
    vardiccionario = re.match(patrondiccionariovar, line)

    if(vardiccionario):
        print("esntra bien")
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
                mensaje= f"Error al evaluar la expresión '{line}': {str(e)}"
                return str(mensaje), 0
        else:
            mensaje= f"La variable ya esta definida '{newvar}'"
            return str(mensaje), 0
            

    elif match_declaration:
        variable_name = match_declaration.group(1)
        variable_value = match_declaration.group(2)
        variables[variable_name] = variable_value
    else:
        match_usage = re.findall(variable_usage_pattern, line)
        for variable_name in match_usage:
            if variable_name not in variables:
                if not (variable_name == "puts") :
                    if re.match(patron, line):
                        return str(variable_name),1
                    else:
                        mensaje= f"Error: Variable '{variable_name}' no definida"
                        return str(mensaje), 0
    
    if "puts" in line:
        


        output_line = line.replace("puts", "").strip()
        for variable_name, variable_value in variables.items():
            output_line = output_line.replace(variable_name, str(variable_value))
        try:
            result = eval(output_line)
            return str(result), 1
        except Exception as e:
            mensaje= f"Error al evaluar la expresión '{output_line}': {str(e)}"
            return str(mensaje), 0
        
    return "",3



def compilar(code):
    global variables 
    variables = {} 

    pattern =  r"'(\w+)'\s*=>\s*{([^}]+)}"
    patron_condicion = r'\b(if|elsif)\s+(.+)\s*$'
    patronifdiccionario =  r'if\s+(.*?)\.key\?\((.*?)\)\s+(.*?)\s+(.*?)\.key\?\((.*?)\)'
 

    matches = list(re.finditer(pattern, code, re.DOTALL))
    start_line =99999
    end_line=0
    
    if matches:
     
        for match in matches:
            start_line = code.count('\n', 0, match.start()) -1 if code.count('\n', 0, match.start()) < start_line else start_line
            end_line = code.count('\n', 0, match.end()) +1 if code.count('\n', 0, match.end()) > start_line else start_line




    lines = code.split('\n')
    output = []
    enif = False
    ifvalid=False
    for index,line in enumerate(lines):
        
        if index >= start_line and index <= end_line:

            lineas_seleccionadas = lines[start_line:end_line+1]
            resultado = '\n'.join(lineas_seleccionadas)
            match = re.search(r'(\w+)\s*=', resultado)

            validacion= procesar_bloques(resultado)
            
            if match and not validacion:
                name =match.group(1)
                if name not in variables:
                    variables[name] = diccionario(resultado)
            else:
                output.append(validacion)
                return output
        else:
        
            if "if" in line:
                match = re.search(patron_condicion, line)
                
                if match:
                    
                    enif=True
                    tipo = match.group(1)
                    condicion = match.group(2)
                    coincidencias = re.search(patronifdiccionario, line)

                    if coincidencias :

                        
                        var1 = coincidencias.group(1).strip()
                        elemen1 = coincidencias.group(2).strip()
                        operator = coincidencias.group(3).strip()
                        var2 = coincidencias.group(4).strip()
                        elemen2 = coincidencias.group(5).strip()

             
                        if var1 in variables:
                            var1=variables[var1]
                         
                        if var2 in variables:
                            var2 = variables[var2]
                           

                  
                        result1= variables[elemen1].replace("'", "").replace('"', '') in var1 and variables[elemen2].replace("'", "").replace('"', '') in var2
                        print("resultado", result1)
                        ifvalid = result1
                        
                    else:
                        patron_operadores = r'(\S+)\s*([<>=]+)\s*(\S+)'
                        match_operadores = re.search(patron_operadores, condicion)
                
                        if match_operadores:
                            valor_uno = match_operadores.group(1)
                            operador = match_operadores.group(2)
                            valor_dos = match_operadores.group(3)
                        
                            if valor_uno in variables:
                                valor_uno=variables[valor_uno]
                            if valor_dos in variables:
                                valor_dos in variables[valor_dos]

                            try:
                                valor_uno = float(valor_uno)
                            except ValueError:
                                pass  

                            try:
                                valor_dos = float(valor_dos)
                            except ValueError:
                                pass
                            
                            if operador == ">":
                                resultado = valor_uno > valor_dos
                            elif operador == ">=":
                                resultado = valor_uno >= valor_dos
                            elif operador == "<":
                                resultado = valor_uno <  valor_dos  
                            elif operador == "<=":
                                resultado = valor_uno <= valor_dos
                            elif operador == "==":
                                resultado = valor_uno == valor_dos
                            elif operador == "!=":
                                resultado = valor_uno != valor_dos
                            else:
                                print("Operador no válido")
                            
                            
                            if resultado:
                                ifvalid = True
                            else:
                                ifvalid = False
         
            else:

                if((not enif or ifvalid) and not ("end" in line) and not ("else" in line)):
        
                    evaluate, status = evaluate_ruby_line(line)
                    if status == 1:
                        output.append(evaluate)
                    elif status == 0 :
                        return evaluate
                elif("else" in line and not ifvalid):
                    print("entra")
                    ifvalid=True
                    enif=True
                elif("end" in line):
                    ifvalid=False
                    enif=False
                
                

    return output



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
                return f"En el bloque {numero_bloque}, línea {i}: Estructura incorrecta en la línea."
        else:
            bloque_match = re.match(patron_bloque, linea.strip())
            if not bloque_match:
                return f"En el bloque {numero_bloque}, línea {i}: Estructura incorrecta en la línea."
            else:
                bloque = bloque_match.group(0)
                

    return None 



def procesar_bloques(hash_str):
    bloques = re.findall(patron_bloque_datos, hash_str)

    for i, bloque in enumerate(bloques, start=1):
        errores_bloque = verificar_errores_linea_por_linea(bloque, i)
        if errores_bloque:
            return errores_bloque

    return None

 
