# necessary libraries
import streamlit as st  
import requests

# Function to get weather data 
def get_weather(city, country):
    base_url = "https://api.weatherbit.io/v2.0/current"
    # Parameters for the API request
    params = {
        "city": city,
        "country": country,
        "key": '[YOUR_API_KEY]',
    }

    # Make a GET request to the API
    response = requests.get(base_url, params=params)

    # response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Streamlit app
st.title("Weather App")
city = st.text_input("Enter City.....")
country = st.text_input("Enter City's country.....")

weather_data = get_weather(city, country)
if weather_data:
    st.write(f"{city}'s Temperature: {weather_data['data'][0]['temp']}°C")
