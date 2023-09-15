from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para recibir un texto mediante POST y devolver "esto es un compilador"
@app.route('/api/compilador', methods=['POST'])
def compilador():
    if request.method == 'POST':
        data = request.json  # Suponemos que el cliente envía un JSON con un campo llamado 'texto'
        if 'texto' in data:
            texto_entrada = data['texto']
            respuesta = "esto es un compilador"
            return jsonify({'respuesta': respuesta})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400

if __name__ == '__main__':
    app.run(debug=True)
