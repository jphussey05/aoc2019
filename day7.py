from itertools import permutations


def get_nums(cursor, num_items):

    answer = []
    # print(f'Reading {num_items} parameter(s) in')
    for num in range(1, num_items + 1):
        answer.append(opcodes[cursor + num])
        # print(f'Parameters are now {answer}')

    return answer


def jump_if_true(cursor, modes):
    '''
    get two parameters;
    return instruction pointer with value of 2nd if 1st is non-zero;
    else do nothing
    '''
    parameters = get_nums(cursor, 2)
    values = []

    for i, para in enumerate(parameters):
        # print(f'{para} has mode {modes[i]}')
        if int(modes[i]) == 1:  # immediate mode
            # print(f'value becomes {para} via immediate mode')
            values.append(int(para))
        else:
            # print(f'value becomes {opcodes[para]} via position mode')
            values.append(int(opcodes[para]))

    if values[0] == 0:
        # print(f'First parameter was zero, increasing cursor and bailing')
        return cursor + 3
    else:
        return int(values[1])


def jump_if_false(cursor, modes):
    '''
    get two parameters;
    return instruction pointer with value of 2nd if 1st is zero;
    else do nothing
    '''
    parameters = get_nums(cursor, 2)
    values = []

    for i, para in enumerate(parameters):
        # print(f'{para} has mode {modes[i]}')
        if int(modes[i]) == 1:  # immediate mode
            # print(f'value becomes {para} via immediate mode')
            values.append(int(para))
        else:
            # print(f'value becomes {opcodes[para]} via position mode')
            values.append(int(opcodes[para]))
   

    if values[0] != 0:
        # print(f'First parameter was not zero, increasing cursor and bailing')
        return cursor + 3
    else:
        return int(values[1])



def less_than(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        # print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            # print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:  # immediate mode
            # print(f'value becomes {para}')
            values.append(int(para))
        else:  # position mode
            # print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))

    num1, num2, idx = values
    # print(f'Checking if {num1} is less than {num2} and storing in {idx}')

    if num1 < num2:
        opcodes[idx] = 1
    else:
        opcodes[idx] = 0

    return cursor + 4

def equals(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        # print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            # print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:  # immediate mode
            # print(f'value becomes {para}')
            values.append(int(para))
        else:  # position mode
            # print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))

    num1, num2, idx = values
    # print(f'Checking if {num1} equals {num2} and storing in {idx}')
    if num1 == num2:
        opcodes[idx] = 1
    else:
        opcodes[idx] = 0

    return cursor + 4

def add(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        # print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            # print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:
            # print(f'value becomes {para}')
            values.append(int(para))
        else:
            # print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))

    num1, num2, idx = values
    # print(f'adding {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 + num2
    return cursor + len(parameters) + 1

def multiply(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        # print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            # print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:
            # print(f'value becomes {para}')
            values.append(para)
        else:
            # print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))
       
    num1, num2, idx = values
    # print(f'multiplying {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 * num2
    return cursor + len(parameters) + 1


def save(cursor, modes, in_val):
    idx = get_nums(cursor, 1)
    # print(f'Saving {in_val} at {idx}')
    # opcodes[idx[0]] = int(input('Please enter your input: '))  # wih day 7
    opcodes[idx[0]] = in_val
    
    return cursor + 2
    

def output(cursor, modes):
    idx = get_nums(cursor, 1)
    if int(modes[0]) == 1:
        # print(f'Mode was immediate, value is {idx[0]}')
        return cursor + 2, idx[0]
    else:
        # print(f'Mode was positional, value is {opcodes[idx[0]]}')
        return cursor + 2, opcodes[idx[0]]


def stop(cursor, modes):
    print(f'Stopping')
    raise SystemExit

if __name__ == "__main__":

    # perms = permutations([5,6,7,8,9])
    perms = [(9,8,7,6,5)]

    with open('day7.txt') as fin:
        contents = fin.read()    
    
    switch_dict = {
        '01': add,
        '02': multiply,
        '03': save,
        '04': output,
        '05': jump_if_true,
        '06': jump_if_false,
        '07': less_than,
        '08': equals,
        '99': stop
    }
    
    opcodes = list(map(int, contents.split(',')))


    max_thruster_signal = 0
    max_thruster_sequence = None
    cur_thruster_signal = 0   #first time through amplifier input is just zero

    for perm in perms:
        # print(f'Checking {perm}')
        for idx, input_instr in enumerate(perm):
            first_input = True
            cursor = 0 
            while cursor is not None:
                # print(f'Opcodes are {opcodes}')
                parameter = str(opcodes[cursor])
                op = parameter[-2:]
                op = ('0' + op) if len(op) == 1 else op
                modes = parameter[:-2][::-1] + '000' # flips the modes so they are left to right
                # print(f'Opcode is {op} and modes are {modes}, calling {switch_dict[op]}')
                if op == '04':   # output condition
                    cursor, cur_thruster_signal = switch_dict[op](cursor, modes)
                elif op == '03' and first_input:  # first input, send the phase
                    cursor = switch_dict[op](cursor, modes, input_instr)
                    first_input = False
                elif op == '03' and not first_input: # sec input, send last amp
                    cursor = switch_dict[op](cursor, modes, cur_thruster_signal)
                elif op == '99':
                    break
                else:
                    cursor = switch_dict[op](cursor, modes)
                # print(f'cursor has been changed to {cursor}')

        if not max_thruster_sequence:
            max_thruster_signal = cur_thruster_signal
            max_thruster_sequence = perm
        elif cur_thruster_signal > max_thruster_signal:
            max_thruster_signal = cur_thruster_signal
            max_thruster_sequence = perm
    

    print(f'Max thruster was {max_thruster_signal} from {max_thruster_sequence}')