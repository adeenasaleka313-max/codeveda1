import requests

city = input("Enter city name: ")

url = "https://wttr.in/" + city + "?format=j1"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        current = data["current_condition"][0]

        print("\nWeather Information")
        print("-------------------")
        print("City:", city)
        print("Temperature:", current["temp_C"], "°C")
        print("Feels Like:", current["FeelsLikeC"], "°C")
        print("Weather:", current["weatherDesc"][0]["value"])
        print("Humidity:", current["humidity"], "%")
        print("Wind Speed:", current["windspeedKmph"], "km/h")

    else:
        print("Could not get weather information.")

except requests.exceptions.RequestException:
    print("Error: Unable to connect to the API.")