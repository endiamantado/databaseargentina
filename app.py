import os
from flask import Flask, jsonify
import json

app = Flask(__name__)

def read_data():
    with open('titumovistar.txt', 'r') as file:
        data = json.load(file)
    return data

with open('titumovistar.txt', 'r') as file:
    for i, line in enumerate(file):
        try:
            json_data = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"Error en la línea {i+1}: {e}")

@app.route('/')
def index():
    return '¡Hola, Render! Esta es la página de inicio.'

@app.route('/data', methods=['GET'])
def get_data():
    data = read_data()
    return jsonify(data)

@app.route('/data/celular/<int:celular>', methods=['GET'])
def get_data_by_celular(celular):
    data = read_data()
    for item in data:
        if item['celular'] == celular:
            return jsonify(item)
    return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
