class SimpleCPU:                        # Step 1: Simulate Memory and Registers
    def _init_(self):
 # Initialize memory with specific values
        self. Memory = {
            940: 5,   # Example values in memory
            941: 10,  # This will be modified
            942: 15   # Additional memory locations if needed
 }
        self.PC = 0  # Program Counter
        self.AC = 0  # Accumulator
        self.IR = None  # Instruction Register
        self.instructions = []  # To hold instructions

    def load_instruction(self, instruction):
         self.instructions.append(instruction)          # """Load a sequence of instructions."""

    def fetch(self):
         if self.PC < len(self.instructions):           # """Fetch the next instruction based on the Program Counter."""
            self.IR = self.instructions[self.PC]
            self.PC += 1  # Increment the Program Counter

    def execute(self):
        opcode, address = self.IR
        if opcode == "LOAD":
            self.AC = self.memory[address]
        elif opcode == "STORE":
            self.memory[address] = self.AC
        elif opcode == "ADD":
            self.AC += self.memory[address]
        else:
            print(f"Unknown opcode: {opcode}")

    def print_state(self):
         print(f"PC: {self.PC - 1}, IR: {self.IR}, AC: {self.AC}")      # """Print the current state of the CPU."""
         print(f"Memory: {self.memory}")

    def execute_cycle(self):
        self.fetch()                       # """Run the fetch-execute cycle."""
        self.print_state()  # Print before execution
        self.execute()
        self.print_state()  # Print after execution

cpu = SimpleCPU()           # Step 2: Initialize Memory and Registers

 # Step 3: Simulate the Given Instruction Sequence
cpu.load_instruction(("LOAD", 940))  # Load value from memory address 940 into AC
cpu.load_instruction(("ADD", 941))    # Add value from memory address 941 to AC
cpu.load_instruction(("STORE", 941))  # Store the result back in memory address 941

 # Step 4: Trace the Execution
 # Execute the instruction cycle for each instruction
for _ in range(len(cpu.instructions)):
    cpu.execute_cycle()