from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, Signal


class LeftMenuButtons(QWidget):
    add_city_signal = Signal(str)
    remove_city_signal = Signal(str)
    def __init__(self):
        super().__init__()
        self.add_item = QPushButton('Add City')
        self.remove_item = QPushButton('Remove City')

        self.initUI()

        self.add_item.clicked.connect(self.addEmitSignal)
        self.remove_item.clicked.connect(self.removeEmitSignal)

    def initUI(self):
        layout = QHBoxLayout()
        layout.addWidget(self.add_item)
        layout.addWidget(self.remove_item)
        self.setLayout(layout)

    def addEmitSignal(self):
        self.add_city_signal.emit("")

    def removeEmitSignal(self):
        self.remove_city_signal.emit("")

