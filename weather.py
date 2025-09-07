import requests

API_KEY = "54877877b324a1e90d706e9540cc86bc"  # REPLACE with your OpenWeatherMap API key

def main():
    city = input("Enter city name: ").strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"].capitalize()
        cityname = data["name"]
        print(f"\nWeather in {cityname}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {desc}")
    else:
        print(f"Error {data.get('cod')}: {data.get('message').capitalize()}")

if __name__ == "__main__":
    main()