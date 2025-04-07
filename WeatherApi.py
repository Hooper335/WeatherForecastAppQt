import requests

def getWeather(lat, lon):
    response = requests.get(
       # f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto")
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&current=temperature_2m&timezone=auto&forecast_days=3")
    return response.json()
