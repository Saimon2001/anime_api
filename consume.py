import requests

response = requests.get('http://127.0.0.1:8000/anime_recomendation') #if errors add at the start HTTP
print(response.json())