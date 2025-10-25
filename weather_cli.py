# weather_cli.py
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
    except Exception as e:
        return {"error": f"Network error: {e}"}

    if data.get("cod") != 200:
        return {"error": data.get("message", "City not found")}

    result = {
        "city": f"{data['name']}, {data['sys']['country']}",
        "temp": f"{data['main']['temp']} °C",
        "humidity": f"{data['main']['humidity']}%",
        "condition": data['weather'][0]['description'].capitalize()
    }
    return result

def main():
    api_key ="5d57453117fda95e31a34c3a38a71c8f"
    city = input("Enter city name: ").strip()
    if not city:
        print("Please enter a city name.")
        return

    weather = get_weather(city, api_key)
    if "error" in weather:
        print("Error:", weather["error"])
    else:
        print("\n🌆 City:", weather["city"])
        print("🌡️ Temperature:", weather["temp"])
        print("💧 Humidity:", weather["humidity"])
        print("🌥️ Condition:", weather["condition"])

if __name__ == "__main__":
    main()
    