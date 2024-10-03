import requests
from tkinter import *

def get_weather(city):
    api_key = 'e1e1a6fda9baa1f4b9f0249e9b81d896'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    print(f"URL: {url}") 
    print(f"Response Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f'{city}: {weather}, {temp}°C'
    else:
        return 'City not found'

def show_weather():
    city = city_entry.get()
    weather_info = get_weather(city)
    weather_label.config(text=weather_info)

app = Tk()
app.title("Weather App")

city_entry = Entry(app)
city_entry.pack()

get_weather_btn = Button(app, text="Get Weather", command=show_weather)
get_weather_btn.pack()

weather_label = Label(app, text="")
weather_label.pack()

app.mainloop()
