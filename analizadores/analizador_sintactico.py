import re

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

# Ejemplo de código para detectar el paradigma
sample_code = """
using Money
using Money.CurrencyLayer

# Configurar el conversor de divisas con la API de CurrencyLayer (requiere una clave API válida)
Money.Rails.configure do config
    config.default_bank = Money.Bank.CurrencyLayer()
    config.default_currency = "USD"
    config.locale_backend = :i18n
end

# Mostrar las monedas disponibles para conversión
currencies = keys(Money.Currency.table)
println("Monedas disponibles para conversión:")
for currency in currencies
    println(currency)
end

# Solicitar al usuario ingresar la moneda de origen y destino
println("Ingresa la moneda de origen (ejemplo: USD): ")
from_currency = uppercase(strip(readline()))

println("Ingresa la moneda de destino (ejemplo: EUR): ")
to_currency = uppercase(strip(readline()))

# Verificar si las monedas ingresadas son válidas
if from_currency in keys(Money.Currency.table) && to_currency in keys(Money.Currency.table)
    println("Ingresa la cantidad en $from_currency: ")
    amount = parse(Float64, strip(readline()))

    # Realizar la conversión de divisas
    money = Money(amount * 100, from_currency)
    converted_money = exchange_to(money, to_currency)
    converted_amount = to_float(converted_money) / 100

    println("$amount $from_currency es igual a $converted_amount $to_currency")
else
    println("Moneda de origen o destino no válida. Asegúrate de usar códigos de moneda válidos.")
end

"""

result = validate_code_julia(sample_code)
for pattern_name, occurrences in result.items():
    print(f'Expresion regular {pattern_name}: {occurrences} ')

