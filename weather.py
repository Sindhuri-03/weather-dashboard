import requests

API_KEY = "de9230bb34b5368fe069049536a41c1a"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("City not found or error occurred.")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)