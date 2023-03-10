import numpy as np
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

qr = QuantumRegister(4, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)