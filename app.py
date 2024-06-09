from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def read_data():
    with open('titumovistar.txt', 'r') as file:
        data = json.load(file)
    return data

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
    app.run()
