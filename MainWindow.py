from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from LeftMenu import LeftMenu
from DisplayWeather import DisplayWeather

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.left_menu = LeftMenu()
        self.display_weather = DisplayWeather()


        self.createMenuBar()
        self.initUI()

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

