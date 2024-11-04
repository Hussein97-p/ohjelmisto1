import http.client
import json

def fetch_weather(city, api_key):

    conn = http.client.HTTPSConnection("api.openweathermap.org")
    

    conn.request("GET", f"/data/2.5/weather?q={city}&appid={api_key}")
    

    response = conn.getresponse()
    

    if response.status == 200:

        data = response.read()
        weather_data = json.loads(data)
        

        weather_description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        

        temperature_celsius = temperature_kelvin - 273.15
        

        print(f"Weather in {city.capitalize()}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f} °C")
    
    else:
        print("Failed to retrieve data. Please check the city name or your API key.")
        print("Status code:", response.status)

    conn.close()


print("To use this program, you need an API key from OpenWeather.")
print("Follow these steps to obtain your API key:")
print("1. Visit the OpenWeather website: https://openweathermap.org/api")
print("2. Sign up for a free account if you don't have one.")
print("3. After signing in, go to the 'API Keys' section in your account.")
print("4. You will find your default API key, or you can generate a new one.")
print("5. When prompted, enter your API key and the name of the city.")

# Input city name and API key
api_key = input("Enter your API key: ")  # Prompt user to enter their API key
city = input("Enter the city name: ")
fetch_weather(city, api_key)
