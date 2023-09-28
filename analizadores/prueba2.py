import re

# Texto de ejemplo
texto = "cualquiercadena.each do |numero|"

# Expresión regular para extraer el texto entre '|'
regex = r".*?\.each do \|([^|]+)\|"

# Busca la coincidencia en el texto
match = re.search(regex, texto)

if match:
    resultado = match.group(1)
    print("Texto extraído:", resultado)
else:
    print("No se encontró ninguna coincidencia.")
