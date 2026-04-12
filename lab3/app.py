from flask import Flask, request, jsonify
import random
app = Flask(__name__)

@app.route('/number/', methods=['GET'])
def get_number():
    param = request.args.get('param', type=int)
    random_num = random.randint(1, 100)
    result = random_num * param
    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)
    return jsonify({'result': result, 'operation': operation})

@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()
    json_param = data.get('jsonParam')
    random_num = random.randint(1, 100)
    result = random_num * json_param
    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)
    return jsonify({'result': result, 'operation': operation})

@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_num = random.randint(1, 100)
    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)
    return jsonify({'result': random_num, 'operation': operation})
