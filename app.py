from flask import Flask, request, jsonify
import main 

app = Flask(__name__)


@app.route('/api/compilador', methods=['POST'])
def compilador():
    if request.method == 'POST':
        data = request.json  
        if 'texto' in data:
            texto_entrada = data['texto']
            lenguaje, paradigma, expressionAnalysis,error, output= main.analizador(texto_entrada)
         
            return jsonify({'lenguaje':lenguaje ,'paradigma' : paradigma, 'ExpresionesRegulares' : expressionAnalysis ,'error' : error ,"output" :output})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400

if __name__ == '__main__':
    app.run(debug=True)
