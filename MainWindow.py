from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from LeftMenu import LeftMenu
from DisplayWeather import DisplayWeather
from PySide6.QtGui import QPalette


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        palette = self.palette()
        bg_color_qt = palette.color(QPalette.Window)
        bg_color_rgb = (bg_color_qt.redF(), bg_color_qt.greenF(), bg_color_qt.blueF())

        text_color_qt = palette.color(QPalette.WindowText)
        text_color_rgb = (text_color_qt.redF(), text_color_qt.greenF(), text_color_qt.blueF())

        self.left_menu = LeftMenu()
        self.list = self.left_menu.city_list
        self.display_weather = DisplayWeather(self.list, bg_color_rgb, text_color_rgb)


        self.createMenuBar()
        self.initUI()
        self.left_menu.connect_city_signal(self.updateWeather)


    def initUI(self):
        central_widget = QWidget()
        layout = QHBoxLayout()

        layout.addWidget(self.left_menu)
        layout.addWidget(self.display_weather)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def createMenuBar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')

    def updateWeather(self, city):
        self.display_weather.showWeather(city)
