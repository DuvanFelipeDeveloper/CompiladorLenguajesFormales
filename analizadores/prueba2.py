import re

def validar_diccionario_ruby(texto):
    # Expresión regular para encontrar corchetes y verificar su equilibrio
    patron_corchetes = re.compile(r'[{}]')
    
    # Pila para rastrear los corchetes abiertos
    pila_corchetes = []
    
    # Variable para rastrear si estamos dentro de un diccionario
    dentro_diccionario = False
    
    # Divide el texto en líneas y realiza un seguimiento del número de línea actual
    lineas = texto.split('\n')
    numero_linea = 0
    
    nlinea=0
    for linea in lineas:
        numero_linea += 1
        # Verifica si la línea contiene corchetes
        if re.search(patron_corchetes, linea):
            for caracter in linea:
                if caracter == '{':
                    pila_corchetes.append('{')
                    # Si encontramos una '{', verificamos si estamos dentro de un diccionario
                    if not dentro_diccionario and re.search(r'\w+\s*=\s*\{', linea):
                        dentro_diccionario = True
                    else:
                        nlinea= numero_linea
                elif caracter == '}':
                    if not pila_corchetes:
                        return f"Error: Corchete de cierre sin coincidencia en la línea {numero_linea}"
                    pila_corchetes.pop()
    
    # Si quedan corchetes sin cerrar en la pila, hay un error
    if pila_corchetes:
        return "Error: Corchete de apertura sin coincidencia"
    
    # Si no se encontraron errores de corchetes y estamos dentro de un diccionario, no hay problemas de sintaxis
    if dentro_diccionario:
        return None
    else:
        return f"Error: No se encontraron estructuras en la linea {nlinea}"



# Tu entrada de texto
entrada = """
a= 2
b= ""
exchange_rates  ={
    'USD' => {
        'JPY' => 110.65,
        'BGN' => 1.71,
        'CZK' => 22.26,
        'DKK' => 6.20,
        'GBP' => 0.72,
        'HUF' => 278.58,
        'PLN' => 3.96,
        'RON' => 4.08
    },
    'JPY' => {
        'USD' => 0.0090,
        'BGN' => 0.015,
        'CZK' => 0.19,
        'DKK' => 0.052,
        'GBP' => 0.006,
        'HUF' => 2.31,
        'PLN' => 0.033,
        'RON' => 0.034
    },
    'BGN' => {
        'USD' => 0.59,
        'JPY' => 68.17,
        'CZK' => 1.29,
        'DKK' => 3.60,
        'GBP' => 0.42,
        'HUF' => 159.90,
        'PLN' => 2.27,
        'RON' => 2.34
    },
    'CZK' => {
        'USD' => 0.045,
        'JPY' => 5.23,
        'BGN' => 0.78,
        'DKK' => 0.28,
        'GBP' => 0.032,
        'HUF' => 12.31,
        'PLN' => 0.18,
        'RON' => 0.18
    },
    'DKK' => {
        'USD' => 0.16,
        'JPY' => 18.97,
        'BGN' => 0.28,
        'CZK' => 3.57,
        'GBP' => 0.11,
        'HUF' => 42.57,
        'PLN' => 0.61,
        'RON' => 0.63
    },
    'GBP' => {
        'USD' => 1.39,
        'JPY' => 161.94,
        'BGN' => 2.38,
        'CZK' => 30.62,
        'DKK' => 8.81,
        'HUF' => 385.31,
        'PLN' => 5.48,
        'RON' => 5.66
    },
    'HUF' => {
        'USD' => 0.0036,
        'JPY' => 0.43,
        'BGN' => 0.0063,
        'CZK' => 0.081,
        'DKK' => 0.023,
        'GBP' => 0.0026,
        'PLN' => 0.014,
        'RON' => 0.014
    },
    'PLN' => {
        'USD' => 0.25,
        'JPY' => 28.97,
        'BGN' => 0.43,
        'CZK' => 5.59,
        'DKK' => 1.55,
        'GBP' => 0.18,
        'HUF' => 71.53,
        'RON' => 1.03
    },
    'RON' => {
        'USD' => 0.24,
        'JPY' => 27.66,
        'BGN' => 0.41,
        'CZK' => 5.33,
        'DKK' => 1.48,
        'GBP' => 0.17,
        'HUF' => 67.95,
        'PLN' => 0.97
    }
}





"""

# Llama a la función para validar la sintaxis del diccionario Ruby
resultado = validar_diccionario_ruby(entrada)

# Comprueba si hubo un error y muestra el mensaje de error si lo hubo
if resultado:
    print(resultado)
else:
    print("La sintaxis del diccionario Ruby es válida.")