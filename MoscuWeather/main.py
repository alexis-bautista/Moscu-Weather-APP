import requests
import csv
from datetime import datetime
import os

api_key = '54a3c0e6465643426b5015070674af0d'
latitude = 55.75222
longitude = 37.61556
url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

response = requests.get(url)
data = response.json()

if 'main' in data:
    weather = {
        'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'weather': data['weather'][0]['description']
    }

    # Verifica si el archivo ya existe para evitar escribir el encabezado nuevamente
    file_path = '/home/alexis/MoscuWeather/clima-moscu-hoy.csv'
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['datetime', 'temperature', 'humidity', 'pressure', 'weather']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Solo escribe el encabezado si el archivo no existe
        writer.writerow(weather)  # Escribe los datos del clima
else:
    print("Error: No se encontró la clave 'main' en la respuesta del API")
