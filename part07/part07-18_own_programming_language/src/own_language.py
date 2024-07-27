# Write your solution here
import string

def handle_print(parts, registers, output):
    value = get_value(parts[1], registers)
    output.append(value)

def handle_mov(parts, registers):
    registers[parts[1]] = get_value(parts[2], registers)

def handle_add(parts, registers):
    registers[parts[1]] += get_value(parts[2], registers)

def handle_sub(parts, registers):
    registers[parts[1]] -= get_value(parts[2], registers)

def handle_mul(parts, registers):
    registers[parts[1]] *= get_value(parts[2], registers)    

def get_value(operand, registers):
    return registers[operand] if operand in registers else int(operand)

def handle_jump(parts, labels):
    return labels[parts[1]]

def handle_if(parts, registers, labels):
    condition_met = evaluate_condition(parts[1:4], registers)
    jump_location = labels[parts[-1]]
    return condition_met, jump_location

def evaluate_condition(condition_parts, registers):
    var, operator, value = condition_parts
    var_value = get_value(var, registers)
    if value in registers:
        value = registers[value]
    else:
        value = int(value)

    if operator == "==":
        return var_value == value
    elif operator == "!=":
        return var_value != value
    elif operator == "<":
        return var_value < value
    elif operator == "<=":
        return var_value <= value
    elif operator == ">":
        return var_value > value
    elif operator == ">=":
        return var_value >= value
    return False

def run(program: list) -> list:
    registers = {char: 0 for char in string.ascii_uppercase}
    output = []
    labels = {}
    pc = 0  # Program counter

    for id, line in enumerate(program):
        if ":" in line:
            label = line.split(":")[0].strip()
            labels[label] = id

    
    while pc < len(program):
        line = program[pc].strip()
        parts = line.split()
        print(f"parts: {parts}")
        if not parts:
            pc += 1
            continue

        command = parts[0]

        if command == "PRINT":
            handle_print(parts, registers, output)
        elif command == "MOV":
            handle_mov(parts, registers)
        elif command == "ADD":
            handle_add(parts, registers)
        elif command == "SUB":
            handle_sub(parts, registers)
        elif command == "MUL":
            handle_mul(parts, registers)
        elif command == "JUMP":
            pc = handle_jump(parts, labels)
            continue
        elif command == "IF":
            condition_met, jump_location = handle_if(parts, registers, labels)
            if condition_met:
                pc = jump_location
                continue
        elif command == "END":
            break
        
        pc += 1
    
    return output

            

if __name__ == "__main__":
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)