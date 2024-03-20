import requests
import sys

token = sys.argv[2]

url = 'https://thecowboys.duckdns.org/api/tontos'

def enviar_tonto_api(tonto):
    id_tonto = tonto[2]

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {'id': id_tonto}

    print(f"Enviando tonto a la API: {id_tonto}")

    x = requests.post(url, json = data, headers = headers)

    print(f"Response: {x.status_code}")
    print(f"Response: {x.text}")

    x.raise_for_status()
