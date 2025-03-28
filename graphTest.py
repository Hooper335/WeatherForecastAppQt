from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        x = [1, 2, 3, 4, 5]
        y = [10, 15, 7, 12, 20]

        self.graphWidget.plot(x, y)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()
