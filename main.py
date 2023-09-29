import analizadores.analizador_lexico as al
import analizadores.analizador_paradigma as ap
import analizadores.analizador_sintactico as asi
import analizadores.ruby.analizador_error as aeRuby
import analizadores.ruby.compilador  as compiladorRuby
import analizadores.perl.analizador_error as aePerl
import analizadores.perl.compilador  as compiladorPerl
import analizadores.julia.analizador_error as aeJulia
import analizadores.julia.compilador  as compiladorJulia
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
    
    
    if(lenguaje == "ruby"):
        error=aeRuby.verificar_equilibrio_ruby(code)

        if(not error):
            error =aeRuby.validar_estructuras_ruby(code)
            if(not error):
                error = ""
        output = compiladorRuby.compilar(code)
    
    elif(lenguaje == "julia"):
        
        error=aeJulia.verificar_equilibrio_julia(code)
        
        if(not error):
            error =aeJulia.validar_estructuras_julia(code)
            if(not error):
                error = ""
        output = compiladorJulia.compilar(code)
    
    elif(lenguaje == "perl"):
        error=aePerl.validar_codigo(code)
        print("perl" , error)
        if(not error):
            # error =aePerl.validar_estructuras_ruby(code)
            if(not error):
                error = ""
        output = compiladorPerl.compilar(code)
    


    return lenguaje, paradigma, expressionAnalysis,error,output
    

