import requests  # Corrected 'request' to 'requests'

api_key = "your_api_key"  # Replace with your actual OpenWeatherMap API key
city = input("Enter your city: ")

# Send GET request to OpenWeatherMap API
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
)

# Parse the JSON response
if response.status_code == 200:
    weather_data = response.json()
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    print(f"Weather in {city}: {description}, Temperature: {temperature}°C")
else:
    print("City not found or error in API request.")
