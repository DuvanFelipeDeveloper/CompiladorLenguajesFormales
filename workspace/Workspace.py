import tkinter as tk
from tkinter import scrolledtext
import requests 

def consumir_api():

    url = "http://127.0.0.1:5000/api/compilador"  
    texto_a_enviar = input_text.get("1.0", "end-1c")

    try:

        response = requests.post(url, json={"texto": texto_a_enviar})

        if response.status_code == 200:
            analysis = response.json()
            response_text.delete("1.0", "end")
            
            if "ExpresionesRegulares" in analysis:
                for pattern_name in analysis["ExpresionesRegulares"]:
                    response_text.insert("1.0", f'Expresion regular {pattern_name} ' + "\n")

            if "paradigma" in analysis:
                response_text.insert("1.0", "Paradigma " + analysis["paradigma"] + "\n")

            if "lenguaje" in analysis:
                response_text.insert("1.0", "Lenguaje " + analysis["lenguaje"] + "\n")

            if "error" in analysis:
                response_text.insert("1.0", "error " + analysis["error"] + "\n")

            if "output" in analysis:
                response_text.insert("1.0", "salida " + analysis["output"] + "\n")

        else:
            response_text.delete("1.0", "end")
            response_text.insert("1.0", "Error: No se pudo obtener datos de la API")
    except Exception as e:
        response_text.delete("1.0", "end")
        response_text.insert("1.0", "Error: " + "De entrada validar linea 1")


root = tk.Tk()
root.title("Compilador")


input_text = scrolledtext.ScrolledText(root, width=80, height=20)
input_text.pack()


button = tk.Button(root, text="Enviar a la API", command=consumir_api)
button.pack()


response_text = scrolledtext.ScrolledText(root, width=80, height=20)
response_text.pack()


root.mainloop()

