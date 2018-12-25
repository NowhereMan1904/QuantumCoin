#!/usr/bin/env python3
from PyQt5 import QtWidgets, QtCore
import sys
import qiskit.circuit

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text = "Some dummy text..."
        self.setMinimumSize(500,500)
        self.label = QtWidgets.QLabel()
        self.button = QtWidgets.QPushButton('Start')
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText(self.text)

    @QtCore.pyqtSlot(str)
    def setText(self, text):
        self.text = self.text + '\n' + text
        self.label.setText(self.text)


class Coin(QtCore.QObject):
    new_line = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        
        self.window = Window()
        self.window.show()
        
        self.new_line.connect(self.window.setText)
        self.new_line.emit("Some new dummy text just emitted")
        self.window.button.clicked.connect(self.toss)

    @QtCore.pyqtSlot()
    def toss(self):
        self.init_circuit()
        self.new_line.emit('Quantum circuit:')
        for d in self.circuit.data:
            self.new_line.emit(d.qasm())
        self.get_backend()
        self.new_line.emit('Backend: ' + self.backend.name())
        job = qiskit.execute(self.circuit, self.backend)
        result = job.result()
        if result.get_counts().keys().isdisjoint('1'):
            self.new_line.emit('Result: 0')
        else:
            self.new_line.emit('Result: 1')

    def init_circuit(self):
        self.qr = qiskit.QuantumRegister(1)
        self.cr = qiskit.ClassicalRegister(1)
        self.circuit = qiskit.QuantumCircuit(self.qr,self.cr)
        self.circuit.h(self.qr)
        self.circuit.measure(self.qr,self.cr)

    def get_backend(self):
        qiskit.IBMQ.load_accounts()
        available_backends = qiskit.IBMQ.backends(operational=True, simulator=False)
        self.backend = qiskit.providers.ibmq.least_busy(available_backends)

def main():
    app = QtWidgets.QApplication(sys.argv)
    coin = Coin()
    sys.exit(app.exec_())


main()
