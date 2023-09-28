import re

# Expresión regular
pattern = r'if\s+\w+\s*\[\w+\]\.key\?\(\w+\)\s*$'

# Cadena de ejemplo
cadena = "if exchange_rates[from_currency].key?(to_currency)"

# Comprobar si la cadena coincide con la expresión regular
if re.match(pattern, cadena):
    print("La cadena es válida.")
else:
    print("La cadena no es válida.")
