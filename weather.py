import requests

print("Weather Dashboard")
api_key = "e8db3855a317bb437b89b8a836e128a7"  # Replace this with an environment variable or secure storage
base_url = "https://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter your city name (or type 'exit' to quit): ").strip()
    if city.lower() == "exit":
        print("Goodbye!")
        break
    if not city:
        print("Please enter a valid city name.")
        continue

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\nWeather Information:")
        print(f"City: {city}, Country: {country}")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError:
        print("City not found or invalid response from API.")
