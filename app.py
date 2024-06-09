from flask import Flask, jsonify, request

app = Flask(__name__)

def read_data():
    data = []
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            id, name = line.strip().split(',')
            data.append({'id': int(id), 'name': name})
    return data

@app.route('/data', methods=['GET'])
def get_data():
    data = read_data()
    return jsonify(data)

@app.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    data = read_data()
    for item in data:
        if item['id'] == data_id:
            return jsonify(item)
    return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run()