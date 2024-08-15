from flask import Flask, request, jsonify
from summarizer import Summarizer
from refinar import refinar_resumen  # Importa la función de refinamiento

app = Flask(__name__)

# Cargar el modelo BERT para resumen
model = Summarizer()

@app.route('/resumir', methods=['POST'])
def resumir():
    data = request.json
    texto = data.get('texto', '')
    indicaciones = data.get('indicaciones', '')

    if not texto:
        return jsonify({'error': 'El campo "texto" es obligatorio.'}), 400

    try:
        # Generar resumen usando BERT
        resumen = model(texto)
        
        # Refinar el resumen usando OpenAI
        indicaciones_openai = 'Dale un tono informativo en tercera persona al texto que te paso, ejemplo: Los clientes opinan, Los mejores aspectos y frases de ese tipo'
        resumen_refinado = refinar_resumen(resumen, indicaciones_openai)
        
        return jsonify({'resumen': resumen_refinado})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Elimina o comenta la siguiente línea si la tienes en el archivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
