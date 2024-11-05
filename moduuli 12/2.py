import urllib.request
import json

def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        temp_celsius = data['main']['temp'] - 273.15
        print(f"Weather in {city}: {data['weather'][0]['description'].capitalize()}, {temp_celsius:.2f} °C")

def display_instructions():
    print("Instructions to get your API key from OpenWeather:")
    print("1. Visit the OpenWeather website: https://openweathermap.org/")
    print("2. Click on 'Sign In' at the top right corner.")
    print("3. If you don't have an account, click on 'Sign Up' to create a new account.")
    print("4. Enter the required information (name, email, password) and follow the instructions to complete registration.")
    print("5. Check your email for a confirmation link and confirm your account.")
    print("6. Log back into your account on the OpenWeather website.")
    print("7. Go to the 'API keys' section in your dashboard.")
    print("8. You will see your API key there. You can use the provided key or create a new one.")
    print("9. Copy your API key and use it in your application. Do not share this key with others.")
    print("If You Don't Have Your Own Key , You can Try The Program By This Key >>9843f8ea3789d4a0b63a8617cf105114<<")

# Main program
display_instructions()
api_key = input("Enter your OpenWeather API key: ")
city = input("Enter city: ")
fetch_weather(city, api_key)
print("Thank you..")