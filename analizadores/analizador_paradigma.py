from pygments.lexers import guess_lexer
import ahocorasick

def detect_paradigm(code):
    # Dividir el código en líneas, espacios y el carácter ":"
    lines_and_tokens = [token for line in code.split('\n') for token in line.split() + line.split(":") + line.split(".")]


    # Contadores para diferentes paradigmas
    count_imperative = 0
    count_object_oriented = 0
    count_functional = 0

    # Diccionario de palabras clave y características de cada paradigma
    paradigms_keywords = {
        'Imperativo': ['for', 'while', 'if', 'else', 'switch', 'break', 'continue'],
        'Orientado a Objetos': ['class', 'def', 'new', 'this', 'super', 'private', 'public', 'protected', 'extends'],
        'Funcional': ['lambda', 'map', 'reduce', 'filter']
    }

    # Analizar los tokens del código
    for token in lines_and_tokens:
        # Detección de características de programación en el lenguaje detectado
        for paradigm, keywords in paradigms_keywords.items():
            for keyword in keywords:
                if keyword == token:
                    print(f"Se encontró una similitud con el paradigma {paradigm}: {token}")

                    if paradigm == 'Imperativo':
                        count_imperative += 1
                    elif paradigm == 'Orientado a Objetos':
                        count_object_oriented += 1
                    elif paradigm == 'Funcional':
                        count_functional += 1

    # Determinar el paradigma predominante
    paradigms = {
        'Imperativo': count_imperative,
        'Orientado a Objetos': count_object_oriented,
        'Funcional': count_functional
    }

    predominant_paradigm = max(paradigms, key=paradigms.get)
    print("Imperativo " + str(count_imperative))
    print("Funcional " + str(count_functional))
    print("Poo " + str(count_object_oriented))

    return predominant_paradigm

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

paradigm=detect_paradigm(sample_code)
print(f"El paradigma predominante es: {paradigm}")