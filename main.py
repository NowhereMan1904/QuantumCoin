from PyQt5.QtWidgets import QApplication, QLabel
from qiskit import execute, QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import IBMQ
from qiskit.backends.ibmq import least_busy
from qiskit import Aer
from time import sleep
from sys import argv

def toss_coin():
    circuit = init_circuit()
    print('Quantum Circuit:')
    for i in range(len(circuit.data)):
        print(circuit.data[i].qasm())

    backend = get_backend(True)
    print('Backend: ' + backend.name())

    job = execute(circuit, backend, shots=1)
    
    check_status(job)
    result = job.result()
    if result.get_counts().keys().isdisjoint('1'):
        print('Result: 0')
    else:
        print('Result: 1')
    

def init_circuit():
    qr = QuantumRegister(1)
    cr = ClassicalRegister(1)
    circuit = QuantumCircuit(qr,cr)
    circuit.h(qr)
    circuit.measure(qr,cr)
    return circuit

def get_backend(local=False):
    if local:
        return Aer.get_backend('qasm_simulator_py')
    IBMQ.load_accounts()
    available_backends = IBMQ.backends(operational=True, simulator=False)
    backend = least_busy(available_backends)
    return backend

def check_status(job):
    lapse = 0
    interval = 10
    while job.status().name != 'DONE':
        print('Status @ {} seconds'.format(interval * lapse))
        print(job.status())
        #print(job.queue_position())
        sleep(interval)
        lapse += 1
    print(job.status())

def main():
    print("ciao!")

    toss_coin()

    app = QApplication(argv)
    label = QLabel('¡Hola!')
    label.setMinimumSize(100,100)
    label.show()
    app.exec_()

main()
