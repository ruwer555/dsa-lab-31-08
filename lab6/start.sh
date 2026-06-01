# Запуск трех сервисов 
python currency_manager.py &
python data_manager.py &
python gateway.py &

echo "Все микросервисы запущены!"
echo "Gateway: http://localhost:5000"
echo "Currency Manager: http://localhost:5001"
echo "Data Manager: http://localhost:5002"

# Ждем завершения
wait