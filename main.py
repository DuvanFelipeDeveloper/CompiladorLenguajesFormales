import analizadores.analizador_lexico as al
import analizadores.analizador_paradigma as ap
from collections import Counter

def analizador(code):
    lenguajes = al.detect_language(code)
    contador = Counter(lenguajes)
    lenguaje, repeticiones = contador.most_common(1)[0]

    paradigma = ap.detect_paradigm(code)
    return lenguaje, paradigma

