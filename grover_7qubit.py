from qiskit import QuantumCircuit, execute, Aer

qc = QuantumCircuit(14, 7)

#
# Step 1: initialization
#
qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
qc.h(4)
qc.h(5)
qc.h(6)
qc.x(13)
qc.h(13)

#
# Repeat steps 2-3 8 times
#
for _ in range(8):
	# Step 2: an oracle that sign-invert the all-one state, assuming that it is the target item
	qc.ccx(0,1,7)
	qc.ccx(2,7,8)
	qc.ccx(3,8,9)
	qc.ccx(4,9,10)
	qc.ccx(5,10,11)
	qc.ccx(6,11,13)
	qc.ccx(5,10,11)
	qc.ccx(4,9,10)
	qc.ccx(3,8,9)
	qc.ccx(2,7,8)
	qc.ccx(0,1,7)

	# Step 3: amplitude amplification that reflects the states around their collective mean
	qc.h(0)
	qc.h(1)
	qc.h(2)
	qc.h(3)
	qc.h(4)
	qc.h(5)
	qc.h(6)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.x(3)
	qc.x(4)
	qc.x(5)
	qc.x(6)
	qc.ccx(0,1,7)
	qc.ccx(2,7,8)
	qc.ccx(3,8,9)
	qc.ccx(4,9,10)
	qc.ccx(5,10,11)
	qc.ccx(6,11,12)
	qc.cz(12,6)
	qc.ccx(6,11,12)
	qc.ccx(5,10,11)
	qc.ccx(4,9,10)
	qc.ccx(3,8,9)
	qc.ccx(2,7,8)
	qc.ccx(0,1,7)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.x(3)
	qc.x(4)
	qc.x(5)
	qc.x(6)
	qc.h(0)
	qc.h(1)
	qc.h(2)
	qc.h(3)
	qc.h(4)
	qc.h(5)
	qc.h(6)

#
# Measure the data qubits and store the results in classical bits
#
qc.measure(0,0)
qc.measure(1,1)
qc.measure(2,2)
qc.measure(3,3)
qc.measure(4,4)
qc.measure(5,5)
qc.measure(6,6)

#
# Run simulations and print out results as instructed previously
#
result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result()
print(result.get_counts(qc))