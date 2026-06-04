import requests

BASE = "http://127.0.0.1:5000"

print("1. Сохраняем ключ 'name' со значением 'Alice'")
r = requests.post(f"{BASE}/set", json={"key": "name", "value": "Alice"})
print(r.json())

print("\n2. Получаем значение по ключу 'name'")
r = requests.get(f"{BASE}/get/name")
print(r.json())

print("\n3. Проверяем, существует ли ключ 'name'")
r = requests.get(f"{BASE}/exists/name")
print(r.json())

print("\n4. Удаляем ключ 'name'")
r = requests.delete(f"{BASE}/delete/name")
print(r.json())

print("\n5. Пробуем получить удалённый ключ")
r = requests.get(f"{BASE}/get/name")
print(r.json())

