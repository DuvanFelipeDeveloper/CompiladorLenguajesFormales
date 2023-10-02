from pygments.lexers import guess_lexer


def detect_paradigm(code):
    lines_and_tokens = [token for line in code.split('\n') for token in line.split() + line.split(":") + line.split(".")]

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




