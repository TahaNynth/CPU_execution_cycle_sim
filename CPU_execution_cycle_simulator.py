memory = {
    940: 10,
    941: 20,
}

# CPU Registers
PC = 0  
AC = 0  
IR = None  


instructions = [("LOAD", 940), ("ADD", 941), ("STORE", 941)]


def load(address):
    global AC
    AC = memory[address]
    print(f"LOAD: AC = {AC}")

def add(address):
    global AC
    AC += memory[address]
    print(f"ADD: AC = {AC}")

def store(address):
    memory[address] = AC
    print(f"STORE: Memory[{address}] = {memory[address]}")

# Simulate fetch-execute cycle
def execute_cycle():
    global PC, IR
    while PC < len(instructions):
        # Fetch phase
        IR = instructions[PC]
        print(f"Fetching instruction {IR} at PC = {PC}")
        
        # Execute phase
        opcode, address = IR
        if opcode == "LOAD":
            load(address)
        elif opcode == "ADD":
            add(address)
        elif opcode == "STORE":
            store(address)
        
        # Move to the next instruction
        PC += 1
        # Print the state of registers and memory
        print(f"PC = {PC}, AC = {AC}, IR = {IR}")
        print(f"Memory: {memory}\n")

# Initialize registers
PC = 0
AC = 0

# Run the CPU simulation
execute_cycle()