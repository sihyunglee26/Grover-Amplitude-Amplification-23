from qiskit import QuantumCircuit, execute, Aer

qc = QuantumCircuit(18, 9)

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
qc.h(7)
qc.h(8)
qc.x(17)
qc.h(17)

#
# Repeat steps 2-3 17 times
#
for _ in range(17):
	# Step 2: an oracle that sign-invert the all-one state, assuming that it is the target item
	qc.ccx(0,1,9)
	qc.ccx(2,9,10)
	qc.ccx(3,10,11)
	qc.ccx(4,11,12)
	qc.ccx(5,12,13)
	qc.ccx(6,13,14)
	qc.ccx(7,14,15)
	qc.ccx(8,15,17)
	qc.ccx(7,14,15)
	qc.ccx(6,13,14)
	qc.ccx(5,12,13)
	qc.ccx(4,11,12)
	qc.ccx(3,10,11)
	qc.ccx(2,9,10)
	qc.ccx(0,1,9)

	# Step 3: amplitude amplification that reflects the states around their collective mean
	qc.h(0)
	qc.h(1)
	qc.h(2)
	qc.h(3)
	qc.h(4)
	qc.h(5)
	qc.h(6)
	qc.h(7)
	qc.h(8)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.x(3)
	qc.x(4)
	qc.x(5)
	qc.x(6)
	qc.x(7)
	qc.x(8)
	qc.ccx(0,1,9)
	qc.ccx(2,9,10)
	qc.ccx(3,10,11)
	qc.ccx(4,11,12)
	qc.ccx(5,12,13)
	qc.ccx(6,13,14)
	qc.ccx(7,14,15)
	qc.ccx(8,15,16)
	qc.cz(16,8)
	qc.ccx(8,15,16)
	qc.ccx(7,14,15)
	qc.ccx(6,13,14)
	qc.ccx(5,12,13)
	qc.ccx(4,11,12)
	qc.ccx(3,10,11)
	qc.ccx(2,9,10)
	qc.ccx(0,1,9)
	qc.x(0)
	qc.x(1)
	qc.x(2)
	qc.x(3)
	qc.x(4)
	qc.x(5)
	qc.x(6)
	qc.x(7)
	qc.x(8)
	qc.h(0)
	qc.h(1)
	qc.h(2)
	qc.h(3)
	qc.h(4)
	qc.h(5)
	qc.h(6)
	qc.h(7)
	qc.h(8)

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
qc.measure(7,7)
qc.measure(8,8)

#
# Run simulations and print out results as instructed previously
#
result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result()
print(result.get_counts(qc))