import re

# Diccionario para almacenar las variables y sus valores
variables = {}

# Expresiones regulares para detectar declaraciones de variables y usos de variables
variable_declaration_pattern = r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*)$'
variable_usage_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
patron = r'^\s*puts\s+"[^"]*"'

# Función para evaluar una línea de código Ruby
def evaluate_ruby_line(line):
    match_declaration = re.match(variable_declaration_pattern, line)
    if match_declaration:
        variable_name = match_declaration.group(1)
        variable_value = match_declaration.group(2)
        variables[variable_name] = variable_value
    else:
        match_usage = re.findall(variable_usage_pattern, line)
        for variable_name in match_usage:
            if variable_name not in variables:
                if not (variable_name == "puts") :
                    print(line)
                    print(variable_name)
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

# Código de ejemplo
ruby_code = """
x = [2,3,5]
y = "juan" 
puts x 
"""

def compilar(code):
    global variables 
    variables = {} 

    pattern =  r"'(\w+)'\s*=>\s*{([^}]+)}"
    patron_condicion = r'\b(if|elsif)\s+(.+)\s*$'


    matches = list(re.finditer(pattern, code, re.DOTALL))
    start_line =99999
    end_line=0
    
    if matches:
     
        for match in matches:
            start_line = code.count('\n', 0, match.start()) -1 if code.count('\n', 0, match.start()) < start_line else start_line
            end_line = code.count('\n', 0, match.end()) +1 if code.count('\n', 0, match.end()) > start_line else start_line

    else:
        print("No se encontraron coincidencias")


    lines = code.split('\n')
    output = []
    enif = False
    ifvalid=False
    for index,line in enumerate(lines):
        
        if index >= start_line and index <= end_line:

            lineas_seleccionadas = lines[start_line:end_line+1]
            resultado = '\n'.join(lineas_seleccionadas)
            
           
            match = re.search(r'(\w+)\s*=', resultado)
            
            if match:
                name =match.group(1)
                if name not in variables:
                    variables[name] = diccionario(resultado)
        else:
        
            if "if" in line:
                match = re.search(patron_condicion, line)
            
                if match:
                    enif=True
                    tipo = match.group(1)
                    condicion = match.group(2)
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
                
                
    print(variables)
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

 
