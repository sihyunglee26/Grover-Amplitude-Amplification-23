'''
Authored by Sihyung Lee
To run the codes, the following modeuls must be installed:
    qiskit
    qiskit-aer
'''

from qiskit import QuantumCircuit, execute, Aer
import math
import timeit

def createCodeWithDummyOracle(n):
    '''
    The function generates the amplitude-amplification step of Grover's algorithm in Python based on the Qiskit library
    The produced codes also include a dummay oracle, which assumes that the all-one state represents the target item

    Input:
        n - the number of data qubits that represent search space of size 2**n

    Output:
        Python codes in string format, which can then be executed (with exec()) or be saved into a file
    '''
    assert isinstance(n, int) and n >= 2, f"n(={n}) must be an integer >= 2"

    codes = ["from qiskit import QuantumCircuit, execute, Aer", ""]

    # Determine the number of qubits and classical bits needed for simulation
    # The first half of the qubits are data qubits and the other half are ancilla qubits
    # The classical bits are used to store the result of measurements
    codes.append(f"qc = QuantumCircuit({2*n}, {n})")
    codes.append("")
    
    codes.append("#\n# Step 1: initialization\n#")
    for i in range(n): codes.append(f"qc.h({i})")
    codes.append(f"qc.x({2*n-1})")
    codes.append(f"qc.h({2*n-1})")
    codes.append("")
    
    numIterations = math.floor(math.pi * math.sqrt(2**n) / 4)
    codes.append(f"#\n# Repeat steps 2-3 {numIterations} times\n#")
    codes.append(f"for _ in range({numIterations}):")
    codes.append("\t# Step 2: an oracle that sign-invert the all-one state, assuming that it is the target item")
    if n == 2: codes.append("\tqc.ccx(0,1,3)")
    else:
        codes.append(f"\tqc.ccx(0,1,{n})")
        for i in range(n-3): codes.append(f"\tqc.ccx({i+2},{n+i},{n+i+1})")
        codes.append(f"\tqc.ccx({n-1},{n*2-3},{2*n-1})")
        for i in reversed(range(n-3)): codes.append(f"\tqc.ccx({i+2},{n+i},{n+i+1})")
        codes.append(f"\tqc.ccx(0,1,{n})")
    codes.append("")

    codes.append("\t# Step 3: amplitude amplification that reflects the states around their collective mean")
    for i in range(n): codes.append(f"\tqc.h({i})")
    for i in range(n): codes.append(f"\tqc.x({i})")
    codes.append(f"\tqc.ccx(0,1,{n})")
    for i in range(n-2): codes.append(f"\tqc.ccx({i+2},{n+i},{n+i+1})")
    codes.append(f"\tqc.cz({2*n-2},{n-1})")
    for i in reversed(range(n-2)): codes.append(f"\tqc.ccx({i+2},{n+i},{n+i+1})")
    codes.append(f"\tqc.ccx(0,1,{n})")
    for i in range(n): codes.append(f"\tqc.x({i})")
    for i in range(n): codes.append(f"\tqc.h({i})")
    codes.append("")

    codes.append("#\n# Measure the data qubits and store the results in classical bits\n#")
    for i in range(n): codes.append(f"qc.measure({i},{i})")
    codes.append("")

    codes.append("#\n# Run simulations and print out results as instructed previously\n#")    
    codes.append("result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result()")
    codes.append("print(result.get_counts(qc))")

    return '\n'.join(codes)


if __name__ == "__main__":
    for n in range(2, 11):        
        codes = createCodeWithDummyOracle(n) # Produce codes for qubit count = n
        with open(f"grover_{n}qubit.py", 'w') as f: # Write the produced codes into a file
            f.write(codes)
        exec(codes) # Execute the produced codes

    