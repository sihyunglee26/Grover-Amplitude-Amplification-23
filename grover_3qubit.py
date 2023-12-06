from qiskit import QuantumCircuit, execute, Aer

qc = QuantumCircuit(6, 3)

#
# Step 1: initialization
#
qc.h(0)
qc.h(1)
qc.h(2)
qc.x(5)
qc.h(5)

#
# Repeat steps 2-3 2 times
#
for _ in range(2):
	# Step 2: an oracle that sign-invert the all-one state, assuming that it is the target item
	qc.ccx(0,1,3)
	qc.ccx(2,3,5)
	qc.ccx(0,1,3)

	# Step 3: amplitude amplification that reflects the states around their collective mean
	qc.h(0)
	qc.h(1)
	qc.h(2)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.ccx(0,1,3)
	qc.ccx(2,3,4)
	qc.cz(4,2)
	qc.ccx(2,3,4)
	qc.ccx(0,1,3)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.h(0)
	qc.h(1)
	qc.h(2)

#
# Measure the data qubits and store the results in classical bits
#
qc.measure(0,0)
qc.measure(1,1)
qc.measure(2,2)

#
# Run simulations and print out results as instructed previously
#
result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result()
print(result.get_counts(qc))