def get_weather(city):
    # Dummy data (no API needed)
    weather_data = {
        "chennai": "32°C, sunny",
        "delhi": "28°C, cloudy",
        "mumbai": "30°C, humid",
        "bangalore": "25°C, pleasant"
    }

    city = city.lower()

    if city in weather_data:
        return f"🌦 Weather in {city.capitalize()}: {weather_data[city]}"
    else:
        return "🌦 Weather data not available (demo mode)"