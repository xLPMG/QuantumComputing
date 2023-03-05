import numpy as np
from qiskit import *
from qiskit.providers.aer import QasmSimulator

circuit = QuantumCircuit(4, 2)

# init states
circuit.h(0)
circuit.h(1)
circuit.h(2)

# gates
circuit.toffoli(0, 1, 3);
circuit.cx(0, 1);
circuit.toffoli(1, 2, 3);
circuit.cx(1, 2);
circuit.cx(0, 1);

circuit.measure([2,3], [0,1]);

simulator = QasmSimulator()
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()

counts = result.get_counts(compiled_circuit)
print("{output : number of shots} = ",counts)
