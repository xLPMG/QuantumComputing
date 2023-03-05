# THIS CODE WAS NOT WRITTEN BY ME

from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('api key')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

def firstBellState():
    circuit = QuantumCircuit(q,c)

    circuit.h(q[0])
    circuit.cx(q[0],q[1])
    circuit.measure(q,c)

    print(circuit)

    job = execute(circuit, backend, shots=8192)

    job_monitor(job)
    counts = job.result().get_counts()

    print(counts)

def secondBellState():
    circuit = QuantumCircuit(q,c)

    circuit.x(q[0])
    circuit.h(q[0])
    circuit.cx(q[0],q[1])
    circuit.measure(q,c)

    print(circuit)

    job = execute(circuit, backend, shots=8192)

    job_monitor(job)
    counts = job.result().get_counts()

    print(counts)

def thirdBellState():
    circuit = QuantumCircuit(q,c)

    circuit.x(q[1])
    circuit.h(q[0])
    circuit.cx(q[0],q[1])
    circuit.measure(q,c)

    print(circuit)

    job = execute(circuit, backend, shots=8192)

    job_monitor(job)
    counts = job.result().get_counts()

    print(counts)

def fourthBellState():
    circuit = QuantumCircuit(q,c)

    circuit.x(q[1])
    circuit.h(q[0])
    circuit.z(q[0])
    circuit.z(q[1])
    circuit.cx(q[0],q[1])
    circuit.measure(q,c)

    print(circuit)

    job = execute(circuit, backend, shots=8192)

    job_monitor(job)
    counts = job.result().get_counts()

    print(counts)

print("Creating first Bell State:\n")
firstBellState()
print("\nCreating second Bell State:\n")
secondBellState()
print("\nCreating third Bell State:\n")
thirdBellState()
print("\nCreating fourth Bell State:\n")
fourthBellState()
