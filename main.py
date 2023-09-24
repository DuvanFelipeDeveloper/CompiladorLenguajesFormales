import analizadores.analizador_lexico as al
import analizadores.analizador_paradigma as ap
import analizadores.analizador_sintactico as asi
import analizadores.analizador_error as ae
import analizadores.compilador  as compilador
from collections import Counter

def analizador(code):
    lenguajes = al.detect_language(code)
    contador = Counter(lenguajes)
    lenguaje, repeticiones = contador.most_common(1)[0]
    paradigma = ap.detect_paradigm(code)

    validation_functions = {
    "ruby": asi.validate_code_ruby,
    "julia": asi.validate_code_julia,
    "perl": asi.validate_code_perl,
    }
    expressionAnalysis = ""
    if lenguaje in validation_functions:
        expressionAnalysis = validation_functions[lenguaje](code)
    else:
        expressionAnalysis ="no compatible"
    
    error=ae.verificar_equilibrio_ruby(code)

    if(not error):
        error =ae.validar_estructuras_ruby(code)
        if(not error):
            error = ""
    output = compilador.compilar(code)
    
    

    return lenguaje, paradigma, expressionAnalysis,error,output
    

