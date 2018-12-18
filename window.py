from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QObject, pyqtSignal
import sys

class Window(QLabel):
    def __init__(self):
        super().__init__()
        
        self.text = "Some dummy text..."
        
        self.setMinimumSize(500,500)
        self.setAlignment(Qt.AlignCenter)
        self.setText(self.text)

class Coin(QObject):
    new_line = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        
        self.window = Window()
        self.window.show()
        
        self.new_line.connect(self.window.setText)
        
        self.new_line.emit("Some new dummy text just emitted")

def main():
    app = QApplication(sys.argv)
    coin = Coin()
    sys.exit(app.exec_())


main()
