from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from WeatherApi import *
from datetime import datetime
import matplotlib.dates as mdates
import random


class DisplayWeather(FigureCanvas):
    def __init__(self, city_list, bg_color_rgb, text_color_rgb):
        self.figure = Figure(facecolor=bg_color_rgb)
        super().__init__(self.figure)
        self.axes = self.figure.add_subplot()
        self.list = city_list
        self.text_color_rgb = text_color_rgb

         

    def showWeather(self, city):
        self.axes.clear()

        # set coordinates
        lan = self.list.items[city]["latitude"]
        lon = self.list.items[city]["longitude"]

        # get a weather data
        weather_data = getWeather(lan, lon)
        current_temperature = weather_data["current"]["temperature_2m"]
        unit = weather_data["current_units"]["temperature_2m"]

        # set a weather data
        temperature = weather_data["hourly"]["temperature_2m"]
        hourly = weather_data["hourly"]["time"]
        x = [datetime.fromisoformat(d) for d in hourly]

        # plot drawing
        self.axes.plot(x,temperature, linestyle='-', color="#ffd941")
        self.axes.set_facecolor('none')

        # title
        self.axes.set_title(f'Now is {current_temperature} {unit}', color = self.text_color_rgb)

        # x axes
        self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.axes.tick_params(axis='x', color = self.text_color_rgb)
        for label in self.axes.xaxis.get_ticklabels():
            label.set_color(self.text_color_rgb)

        # y axes
        for label in self.axes.yaxis.get_ticklabels():
            label.set_color(self.text_color_rgb)

        # fill between
        y_min = self.axes.get_ylim()[0]
        self.axes.fill_between( hourly,y_min, temperature, color='#fff5cc', alpha=0.8 )

        # spines
        for spine in self.axes.spines.values():
            spine.set_visible(False)
        self.axes.spines["bottom"].set_visible(True)
        self.axes.spines["bottom"].set_color(self.text_color_rgb)

        # horizontal lines
        self.axes.yaxis.grid(True)

        # vertical line
        current_time = weather_data["current"]["time"]
        self.axes.axvline(datetime.fromisoformat(current_time), color="red")

        self.draw()