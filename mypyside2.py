import sys
from PySide2 import QtCore, QtWidgets, QtGui

class Window(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Hello World")
        self.setAlignment(QtCore.Qt.AlignHCenter)
        self.resize(800,600)

class Coin(QtCore.QObject):
    new_line = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.window = Window()
        self.new_line.connect(self.window.setText)
        self.new_line.emit("dlroW olleH")
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    coin = Coin()
    sys.exit(app.exec_())
