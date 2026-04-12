from flask import Flask, request, jsonify
import random
import time
import requests
app = Flask(__name__)

@app.route('/number/', methods=['GET'])
def get_number():
    param = request.args.get('param', type=int)
    random_num = random.randint(1, 100)
    result = random_num * param
    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)
    print(f"[GET] param={param}, число={random_num}, результат={result}, операция={operation}")
    return jsonify({'result': result, 'operation': operation})

@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()
    json_param = data.get('jsonParam')
    random_num = random.randint(1, 100)
    result = random_num * json_param
    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)
    print(f"[POST] jsonParam={json_param}, число={random_num}, результат={result}, операция={operation}")
    return jsonify({'result': result, 'operation': operation})

@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_num = random.randint(1, 100)
    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)
    print(f"[DELETE] число={random_num}, операция={operation}")
    return jsonify({'result': random_num, 'operation': operation})

def run_server():
    """Запуск сервера на порту 5000"""
    app.run(debug=False, use_reloader=False)

def run_client():
    time.sleep(2)
    # 1. GET запрос
    param = random.randint(1, 10)
    print(f"1. GET запрос: /number/?param={param}")
    response_get = requests.get(f'http://127.0.0.1:5000/number/?param={param}')
    data_get = response_get.json()
    print(f"   Ответ: result={data_get['result']}, operation={data_get['operation']}\n")
    
    # 2. POST запрос
    json_param = random.randint(1, 10)
    headers = {'Content-Type': 'application/json'}
    data_post_raw = {'jsonParam': json_param}
    print(f"2. POST запрос: /number/ с телом {data_post_raw}")
    response_post = requests.post('http://127.0.0.1:5000/number/', headers=headers, json=data_post_raw)
    data_post = response_post.json()
    print(f"   Ответ: result={data_post['result']}, operation={data_post['operation']}\n")
    
    # 3. DELETE запрос
    print("3. DELETE запрос: /number/")
    response_delete = requests.delete('http://127.0.0.1:5000/number/')
    data_delete = response_delete.json()
    print(f"   Ответ: result={data_delete['result']}, operation={data_delete['operation']}\n")
    
    calc_result = data_get['result']
    print(f"\nНачальное значение: {calc_result}")
    
    print(f"\nШаг 1: {calc_result} {data_get['operation']} {data_post['result']}")
    if data_get['operation'] == 'sum':
        calc_result = calc_result + data_post['result']
    elif data_get['operation'] == 'sub':
        calc_result = calc_result - data_post['result']
    elif data_get['operation'] == 'mul':
        calc_result = calc_result * data_post['result']
    elif data_get['operation'] == 'div':
        calc_result = calc_result / data_post['result']
    print(f"   Результат: {calc_result}")
    
    print(f"\nШаг 2: {calc_result} {data_post['operation']} {data_delete['result']}")
    if data_post['operation'] == 'sum':
        calc_result = calc_result + data_delete['result']
    elif data_post['operation'] == 'sub':
        calc_result = calc_result - data_delete['result']
    elif data_post['operation'] == 'mul':
        calc_result = calc_result * data_delete['result']
    elif data_post['operation'] == 'div':
        calc_result = calc_result / data_delete['result']
    print(f"   Результат: {calc_result}")
    
    print(f"\nШаг 3: {calc_result} {data_delete['operation']} {data_delete['result']}")
    if data_delete['operation'] == 'sum':
        calc_result = calc_result + data_delete['result']
    elif data_delete['operation'] == 'sub':
        calc_result = calc_result - data_delete['result']
    elif data_delete['operation'] == 'mul':
        calc_result = calc_result * data_delete['result']
    elif data_delete['operation'] == 'div':
        calc_result = calc_result / data_delete['result']
    print(f"   Результат: {calc_result}")
    
run_client()