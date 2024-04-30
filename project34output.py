import requests
from win11toast import toast

# Set your location here (for example, "Los Angeles, US" or "New York, US" )
location = "Columbus, Georgia, US"

# Drop your API key for OpenWeatherMap
api_key = "bb51b4a7cb492103c51c04b3ddc14920"

# Drop the URL for the OpenWeatherMap API
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

# Get the weather data from OpenWeatherMap
response = requests.get(url)
data = response.json()

# Set the notification title and message
title = f"Weather in {data['name']}"
message = f"{data['weather'][0]['description'].capitalize()}, {round(data['main']['temp']-273.15, 1)}°C, {data['main']['humidity']}% humidity"

# Create the notification icon
toast('Columbus, Georgia Weather', 'Here is the forecast in Columbus, Georgia',  icon='D:/Python/cloud.ico')

toast(title, message)
