import re
from pyparsing import *


def validate_code_julia(code):
    patterns = {
        'Declaracion de Importacion': r'using\s+[\w\.]+',
        'Declaracion de configuracion': r'Money\.Rails\.configure\s+do\s+config\s*\n\s+config\..+',
        'Declaracion de Impresion': r'println\(".+"\)',
        'Declaracion de entrada de usuario': r'\b(?:uppercase\()?(?:strip\()?(?:readline\(\))?\)?\s*?[;]?',
        'Declaracion de condiccion': r'if\s+.+',
        'Declaracion de ciclo': r'for\s+\w+\s+in\s+.+',
        'Declaracion while': r'while\s+.+',
        'Asigancion de variable': r'(?<!if)\s*\w+\s*=\s*.+',
        'Funcion de Llamada': r'\w+\(.+\)',
        'Operacion Matematica': r'[\w_]+\s*[\+\-\*/%]\s*[\w_]+',
        'Diccionario': r'"[A-Z]+" => Dict\([^)]*\)'
    }
    
    coincidencias = []

    lineas = code.split('\n')

    for linea in lineas:
        for nombre_expresion, patron in patterns.items():
            if re.search(patron, linea):
                coincidencias.append(f"Línea: {linea.strip()}\nExpresión regular: {nombre_expresion}\n")

    return coincidencias


def validate_code_perl(code):

    patterns = {
        'Declaracion de Importacion': r'use\s+Money;',
        'Declaracion de configuracion': r'Money::Rails\.configure\s+do\s+my\s+\$config\s+=.+?;\s+end',
        'Declaracion de Impresion': r'print\s+".+"',
        'Declaracion de entrada de usuario': r'my\s+\$\w+\s+=\s+<STDIN>;\s+chomp\s+\$\w+;',
        'Declaracion de entrada de usuario ': r"my\s+\$([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*);",
        'Declaracion de condiccion':  r'if\s+.+',
        'Declaracion de ciclo': r'foreach\s+my\s+\$[\w_]+\s+\(.+?\)\s+\{.+?\}',
        'Asigancion de variable': r'my\s+\$\w+\s+=\s+.+?;',
        'Funcion de Llamada': r'my\s+\$\w+\s+=\s+\$[\w_]+\(.+?\);',
        'Operacion Matematica': r'\$[\w_]+\s*[+\-*\/%]\s*[\d\w_]+'
    }

    coincidencias = []

    lineas = code.split('\n')

    for linea in lineas:
        for nombre_expresion, patron in patterns.items():
            if re.search(patron, linea):
                coincidencias.append(f"Línea: {linea.strip()}\nExpresión regular: {nombre_expresion}\n")

    return coincidencias



def validate_code_ruby(code):
    patterns = {
        'Declaracion de Importacion': r'require\s+["\']money["\']',
        'Declaracion de configuracion': r'Money::Rails\.configure\s+do\s+\|config\|\s+.+end',
        'Declaracion de Impresion': r'puts\s+(?:\w+|".+")',
        'Declaracion de entrada de usuario': r'print\s+".+"\s+\+\s+(?:gets\..+)?',
        'Declaracion de condiccion': r'if\s+\w+\s*\.key\?\(\w+\)\s*(?:&&\s*\w+\s*\.key\?\(\w+\))?\s*$',
        'Declaracion de ciclo': r'currencies.each\s+\{\s+\|\w+\|\s+.+\s+\}',
        'Asigancion de variable': r'\w+\s*=\s*.+',
        'Funcion de Llamada': r'\w+\.(?:chomp|upcase|to_f|round|puts)\s*.+',
        'Operacion Matematica': r'\w+\s*[*+-\/%]\s*[\d\w_]+',
        'Diccionario': r"'\w+' => \{[^}]*\}"
    }

    coincidencias = []

    lineas = code.split('\n')

    for linea in lineas:
        for nombre_expresion, patron in patterns.items():
            if re.search(patron, linea):
                coincidencias.append(f"{linea.strip()}\nExpresión regular: {nombre_expresion}\n")

    return coincidencias


#Prototipo Deteccion de Gramatica regular 

# Definir tokens
identifier = Word(alphanums + '_')
keyword = Word(alphanums + '_')
equals = Suppress('=')
colon = Suppress(':')
string = Suppress('"') + Word(alphanums + ' ') + Suppress('"')
number = Word("0123456789.")

# Reglas de producción
import_statement = Group(keyword("using") + keyword("Money"))
configure_statement = Group(keyword("Money.Rails.configure") + keyword("do") + keyword("config") + Suppress('=') + Suppress("Money.Bank.CurrencyLayer()"))
print_statement = Group(keyword("println(") + string("message") + ")")
user_input_statement = Group(keyword("println(") + string("prompt") + colon + identifier("input") + "(" + ")" + equals + identifier("var") + ")")
if_statement = Group(keyword("if") + identifier("condition") + restOfLine + "println(" + string("message") + ")" + "else" + restOfLine + "println(" + string("message") + ")" + "end")
for_loop = Group(keyword("for") + identifier("currency") + keyword("in") + identifier("currencies") + restOfLine + "println(" + string("message") + ")" + "end")
assignment = Group(identifier("var") + equals + (string | number | identifier))
function_call = Group(identifier("func") + "(" + Optional(identifier("args")) + ")" + equals + identifier("var"))

# Gramática completa
expression = (import_statement | configure_statement | print_statement | user_input_statement | if_statement | for_loop | assignment | function_call)


