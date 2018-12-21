import sys
from PySide2 import QtCore, QtWidgets, QtGui

class Window(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        self.setText("Hello World")
        self.setAlignment(QtCore.Qt.AlignHCenter)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Window()
    window.resize(800,600)
    window.show()

    sys.exit(app.exec_())
