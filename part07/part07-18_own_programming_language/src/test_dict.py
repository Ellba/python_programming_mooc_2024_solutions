import string
registers = {char: 0 for char in string.ascii_uppercase}
parts = "MOV A B".split(' ')

def get_value(operand, registers):
    print(operand in registers)
    return registers[operand] if operand in registers else int(operand)

def handle_mov(parts, registers):
    registers[parts[1]] = get_value(parts[2], registers)

print(f"registers: {registers.get("A")}")
print(f"parts: {parts}")

handle_mov(parts, registers)

print(f"registers: {registers.get("A")}")
