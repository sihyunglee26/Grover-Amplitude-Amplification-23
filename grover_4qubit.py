from qiskit import QuantumCircuit, execute, Aer

qc = QuantumCircuit(8, 4)

#
# Step 1: initialization
#
qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
qc.x(7)
qc.h(7)

#
# Repeat steps 2-3 3 times
#
for _ in range(3):
	# Step 2: an oracle that sign-invert the all-one state, assuming that it is the target item
	qc.ccx(0,1,4)
	qc.ccx(2,4,5)
	qc.ccx(3,5,7)
	qc.ccx(2,4,5)
	qc.ccx(0,1,4)

	# Step 3: amplitude amplification that reflects the states around their collective mean
	qc.h(0)
	qc.h(1)
	qc.h(2)
	qc.h(3)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.x(3)
	qc.ccx(0,1,4)
	qc.ccx(2,4,5)
	qc.ccx(3,5,6)
	qc.cz(6,3)
	qc.ccx(3,5,6)
	qc.ccx(2,4,5)
	qc.ccx(0,1,4)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.x(3)
	qc.h(0)
	qc.h(1)
	qc.h(2)
	qc.h(3)

#
# Measure the data qubits and store the results in classical bits
#
qc.measure(0,0)
qc.measure(1,1)
qc.measure(2,2)
qc.measure(3,3)

#
# Run simulations and print out results as instructed previously
#
result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result()
print(result.get_counts(qc))