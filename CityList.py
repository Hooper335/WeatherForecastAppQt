from PySide6.QtWidgets import QListWidget
import json
import requests

class CityList(QListWidget):
    def __init__(self):
        super().__init__()

        try:
            with open("cities.json") as f:
                self.items = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.items = []
        self.citiesNames = []
        for city in self.items:
            self.citiesNames.append(city["name"])
        self.addItems(self.citiesNames)

    def removeCity(self, city_id):
        del self.items[city_id]
        self.takeItem(city_id)
        with open("cities.json", 'w') as f:
            json.dump(self.items, f, indent=4)


    def addCity(self, cityName):
        print(cityName)
        response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={cityName}&format=json")
        data = response.json()
        try:
            name = data["results"][0]["name"]
        except (KeyError, IndexError):
            print(f"No city name found for {cityName}")
            return
        country = data["results"][0]["country"]
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]
        new_entry = {
            "name": name,
            "country": country,
            "latitude": latitude,
            "longitude": longitude,
        }
        self.items.append(new_entry)
        self.addItem(name)
        with open("cities.json", 'w') as f:
            json.dump(self.items, f, indent=4)





