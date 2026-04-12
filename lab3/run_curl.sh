curl "http://127.0.0.1:5000/number/?param=5"
curl -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"jsonParam":5}' "http://127.0.0.1:5000/number/"
curl -Method DELETE "http://127.0.0.1:5000/number/"