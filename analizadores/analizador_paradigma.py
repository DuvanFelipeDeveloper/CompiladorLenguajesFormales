from pygments.lexers import guess_lexer
from pygments.lexers import get_lexer_for_filename, get_lexer_by_name
from pygments.util import ClassNotFound

def detect_paradigm(code):
    try:
        # Intenta determinar el lenguaje del código
        lexer = get_lexer_for_filename("example.py", code)
    except ClassNotFound:
        # Si no se puede determinar automáticamente, usa un lexer de Python
        lexer = get_lexer_by_name("python")

    # Detección de paradigmas basada en el lexer
    detected_paradigms = set()

    if "oop" in lexer.aliases or "Python" in lexer.name:
        detected_paradigms.add("Programación Orientada a Objetos")

    if "functional" in lexer.aliases:
        detected_paradigms.add("Programación Funcional")

    if "imperative" in lexer.aliases:
        detected_paradigms.add("Programación Imperativa")

    return detected_paradigms


def detect_language(code):
    try:
        lexer = guess_lexer(code)
        language = lexer.name
        return language
    except Exception as e:
        return f"No se pudo detectar el lenguaje: {str(e)}"


# Ejemplo de código para detectar el paradigma
sample_code = """

require 'money'
require 'money/bank/currencylayer_bank'

# Configurar el conversor de divisas con la API de currencylayer (requiere una clave API válida)
Money::Rails.configure do |config|
  config.default_bank = Money::Bank::Currencylayer.new
  config.default_currency = 'USD'
  config.locale_backend = :i18n
end

# Mostrar las monedas disponibles para conversión
currencies = Money::Currency.table.keys
puts "Monedas disponibles para conversión:"
currencies.each { |currency| puts currency }

# Solicitar al usuario ingresar la moneda de origen y destino
print "Ingresa la moneda de origen (ejemplo: USD): "
from_currency = gets.chomp.upcase

print "Ingresa la moneda de destino (ejemplo: EUR): "
to_currency = gets.chomp.upcase

# Verificar si las monedas ingresadas son válidas
if currencies.include?(from_currency) && currencies.include?(to_currency)
  print "Ingresa la cantidad en #{from_currency}: "
  amount = gets.chomp.to_f

  # Realizar la conversión de divisas
  money = Money.new(amount * 100, from_currency)
  converted_money = money.exchange_to(to_currency)
  converted_amount = converted_money.to_f / 100

  puts "#{amount} #{from_currency} es igual a #{converted_amount} #{to_currency}"
else
  puts "Moneda de origen o destino no válida. Asegúrate de usar códigos de moneda válidos."
end


"""

result = detect_paradigm(sample_code)
print(f"El paradigma predominante es: {result}")

language_detected = detect_language(sample_code)
print(f"El lenguaje detectado es: {language_detected}")


"""
from forex_python.converter import CurrencyRates

# Crear una instancia de CurrencyRates
c = CurrencyRates()

# Mostrar las monedas disponibles para conversión
print("Monedas disponibles para conversión:")
currencies = c.get_rates("")
for currency in currencies:
    print(currency)

# Solicitar al usuario ingresar la moneda de origen y destino
from_currency = input("Ingresa la moneda de origen (ejemplo: USD): ").upper()
to_currency = input("Ingresa la moneda de destino (ejemplo: EUR): ").upper()

# Verificar si las monedas ingresadas son válidas
if from_currency in currencies and to_currency in currencies:
    amount = float(input(f"Ingresa la cantidad en {from_currency}: "))

    # Realizar la conversión de divisas
    converted_amount = c.convert(from_currency, to_currency, amount)

    print(f"{amount} {from_currency} es igual a {converted_amount} {to_currency}")
else:
    print("Moneda de origen o destino no válida. Asegúrate de usar códigos de moneda válidos.")
"""