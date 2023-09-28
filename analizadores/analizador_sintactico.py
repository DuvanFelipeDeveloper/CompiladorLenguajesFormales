import re
from pyparsing import *
# este es el codigo de expresiones regulares 

def validate_code_julia(code):
    patterns = {
        'import_statement': r'using\s+[\w\.]+',
        'configure_statement': r'Money\.Rails\.configure\s+do\s+config\s*\n\s+config\..+',
        'print_statement': r'println\(".+"\)',
        'user_input_statement': r'\b(?:uppercase\()?(?:strip\()?(?:readline\(\))?\)?\s*?[;]?',
        'if_statement': r'if\s+.+',
        'for_loop': r'for\s+\w+\s+in\s+.+',
        'while_loop': r'while\s+.+',
        'variable_assignment': r'(?<!if)\s*\w+\s*=\s*.+',
        'function_call': r'\w+\(.+\)',
        'math_operation': r'[\w_]+\s*[\+\-\*/%]\s*[\w_]+'
    }
    
    matches = {}
    for pattern_name, pattern in patterns.items():
        match = re.search(pattern, code)
        if match:
            matches[pattern_name] = match.group()

    return matches


def validate_code_perl(code):
    # Expresiones regulares para validar patrones comunes en el código de conversión de divisas
    patterns = {
        'import_statement': r'use\s+Money;',
        'configure_statement': r'Money::Rails\.configure\s+do\s+my\s+\$config\s+=.+?;\s+end',
        'print_statement': r'print\s+".+"',
        'user_input_statement': r'my\s+\$\w+\s+=\s+<STDIN>;\s+chomp\s+\$\w+;',
        'if_statement': r'if\s+\(.+\)\s+\{.+?\}',
        'for_loop': r'foreach\s+my\s+\$[\w_]+\s+\(.+?\)\s+\{.+?\}',
        'variable_assignment': r'my\s+\$\w+\s+=\s+.+?;',
        'function_call': r'my\s+\$\w+\s+=\s+\$[\w_]+\(.+?\);',
        'math_operation': r'\$[\w_]+\s*[+\-*\/%]\s*[\d\w_]+'
    }

    # Buscar coincidencias en el código
    matches = {}
    for pattern_name, pattern in patterns.items():
        match = re.search(pattern, code)
        if match:
            matches[pattern_name] = match.group()

    return matches



def validate_code_ruby(code):
    # Expresiones regulares para validar patrones comunes en el código de conversión de divisas
    patterns = {
        'import_statement': r'require\s+["\']money["\']',
        'configure_statement': r'Money::Rails\.configure\s+do\s+\|config\|\s+.+end',
        'print_statement': r'puts\s+".+"',
        'user_input_statement': r'print\s+".+"\s+\+\s+(?:gets\..+)?',
        'if_statement': r'if\s+.+\s+&&\s+.+:',
        'for_loop': r'currencies.each\s+\{\s+\|\w+\|\s+.+\s+\}',
        'variable_assignment': r'\w+\s*=\s*.+',
        'function_call': r'\w+\.(?:chomp|upcase|to_f|round|puts)\s*.+',
        'math_operation': r'\w+\s*[*+-\/%]\s*[\d\w_]+'
    }

    # Buscar coincidencias en el código
    matches = {}
    for pattern_name, pattern in patterns.items():
        match = re.search(pattern, code)
        if match:
            matches[pattern_name] = match.group()

    return matches




# #Prototipo Deteccion de Gramatica regular 

# # Definir tokens
# identifier = Word(alphanums + '_')
# keyword = Word(alphanums + '_')
# equals = Suppress('=')
# colon = Suppress(':')
# string = Suppress('"') + Word(alphanums + ' ') + Suppress('"')
# number = Word("0123456789.")

# # Reglas de producción
# import_statement = Group(keyword("using") + keyword("Money"))
# configure_statement = Group(keyword("Money.Rails.configure") + keyword("do") + keyword("config") + Suppress('=') + Suppress("Money.Bank.CurrencyLayer()"))
# print_statement = Group(keyword("println(") + string("message") + ")")
# user_input_statement = Group(keyword("println(") + string("prompt") + colon + identifier("input") + "(" + ")" + equals + identifier("var") + ")")
# if_statement = Group(keyword("if") + identifier("condition") + restOfLine + "println(" + string("message") + ")" + "else" + restOfLine + "println(" + string("message") + ")" + "end")
# for_loop = Group(keyword("for") + identifier("currency") + keyword("in") + identifier("currencies") + restOfLine + "println(" + string("message") + ")" + "end")
# assignment = Group(identifier("var") + equals + (string | number | identifier))
# function_call = Group(identifier("func") + "(" + Optional(identifier("args")) + ")" + equals + identifier("var"))

# # Gramática completa
# expression = (import_statement | configure_statement | print_statement | user_input_statement | if_statement | for_loop | assignment | function_call)


