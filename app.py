import streamlit as st
import requests
import datetime

# OpenWeatherMap API Key (Replace with your own key)
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

# Function to fetch current weather data
def get_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to fetch 5-day weather forecast
def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Convert timestamp to readable date
def format_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%A, %d %b")

# Streamlit UI
st.title("🌦️ Weather Dashboard")
st.write("Enter a city name to get the current weather and 5-day forecast.")

# Search bar
city = st.text_input("Enter city name:", "")

if city:
    weather_data = get_weather(city)

    if weather_data.get("cod") == 200:
        # Extract current weather details
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"].title()
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        icon = weather_data["weather"][0]["icon"]
        
        # Display current weather
        st.subheader(f"Current Weather in {city}")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        wi
