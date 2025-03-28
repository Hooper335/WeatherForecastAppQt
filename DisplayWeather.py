from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import random

class DisplayWeather(FigureCanvas):
    def __init__(self):
        self.figure = Figure()
        super().__init__(self.figure)

        self.axes = self.figure.add_subplot()

        data = [random.random() for i in range(25)]

        self.axes.plot(data, linestyle='dashed')
        self.axes.set_title('The Graph Title')
        self.axes.set_ylabel('Y Label')
        self.axes.set_xlabel('X Label')
        self.axes.xaxis.label.set_color('blue')
        self.axes.xaxis.set_tick_params(colors='red')
        self.axes.spines['left'].set_color('orange')
        self.draw()
