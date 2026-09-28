import requests


def get_weather(city):
    """Get current weather information for a city."""

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    current = data["current_condition"][0]

    return {
        "city": city,
        "temperature": current["temp_C"],
        "condition": current["weatherDesc"][0]["value"],
        "humidity": current["humidity"],
    }


if __name__ == "__main__":
    result = get_weather("Chennai")
    print(result)