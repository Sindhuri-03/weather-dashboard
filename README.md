# Weather Dashboard

A simple Python command-line app that fetches real-time weather data using the OpenWeatherMap API.

## Features
- Get current temperature, humidity, weather condition, and wind speed for any city
- Uses environment variables to keep API keys secure

## Tech Stack
- Python
- requests library
- python-dotenv for environment variable management
- OpenWeatherMap API

## Setup

1. Clone this repository

2. Install dependencies:

pip install -r requirements.txt

3. Get a free API key from OpenWeatherMap (https://openweathermap.org/)

4. Create a .env file in the project folder with:

API_KEY=your_api_key_here

5. Run the script:

python weather.py

## Example

Enter city name: Delhi

Weather in Delhi:
Temperature: 34.78°C
Condition: overcast clouds
Humidity: 49%
Wind Speed: 3.33 m/s
