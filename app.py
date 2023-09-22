from flask import Flask, request, jsonify
import main 

app = Flask(__name__)

# Ruta para recibir un texto mediante POST y devolver "esto es un compilador"
@app.route('/api/compilador', methods=['POST'])
def compilador():
    if request.method == 'POST':
        data = request.json  # Suponemos que el cliente envía un JSON con un campo llamado 'texto'
        if 'texto' in data:
            texto_entrada = data['texto']
            lenguaje, paradigma = main.analizador(texto_entrada)
            return jsonify({'lenguaje':lenguaje ,'paradigma' : paradigma })
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400

if __name__ == '__main__':
    app.run(debug=True)
