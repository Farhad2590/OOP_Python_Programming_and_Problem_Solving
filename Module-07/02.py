import requests
import time

def weather_data():
    pi_address = 'http://api.openweathermap.org/data/2.5/weather?q=Chittagong&appid=4b5f5c378962441c1c0063e2bb400c5c'
    url = pi_address
    json_data = requests.get(url).json()
    print(json_data)

weather_data()
time.sleep(1800)