from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QLineEdit
from CityList import CityList
from LeftMenuButtons import LeftMenuButtons
from PySide6.QtCore import Signal


class LeftMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.city_list = CityList()
        self.text_box = QLineEdit()
        self.buttons = LeftMenuButtons()

        self.buttons.add_city_signal.connect(self.handleAddCity)
        self.buttons.remove_city_signal.connect(self.handleRemoveCity)

        self.initUi()


    def initUi(self):
        layout = QVBoxLayout()

        layout.addWidget(self.city_list)
        layout.addWidget(self.text_box)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def handleAddCity(self):
        city_name = self.text_box.text().strip().title()
        if city_name:
            self.city_list.addCity(city_name)
            self.text_box.setText("")

    def handleRemoveCity(self):
        city_id = self.city_list.currentRow()
        self.city_list.removeCity(city_id)