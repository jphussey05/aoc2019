def get_nums(cursor, num_items):

    answer = []
    print(f'Reading {num_items} parameter(s) in')
    for num in range(1, num_items + 1):
        answer.append(opcodes[cursor + num])
        print(f'Parameters are now {answer}')

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
        print(f'{para} has mode {modes[i]}')
        if int(modes[i] == 1):  # immediate mode
            print(f'value becomes {para}')
            values.append(int(para))
        else:
            print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))

    if values[0] == 0:
        return cursor + 2
    
    if int(modes[1]) == 1:  #check if the mode is 1 and use absolute value
        return int(values[1])
    else:  # otherwise mode is 2 and its a reference value
        return int(opcodes[values[1]])

def jump_if_false(cursor, modes):
    '''
    get two parameters;
    return instruction pointer with value of 2nd if 1st is zero;
    else do nothing
    '''
    parameters = get_nums(cursor, 2)
    values = []

    for i, para in enumerate(parameters):
        print(f'{para} has mode {modes[i]}')
        if int(modes[i] == 1):  # immediate mode
            print(f'value becomes {para}')
            values.append(int(para))
        else:
            print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))
   

    if values[0] != 0:
        return cursor + 2

    if int(modes[1]) == 1:  #check if the mode is 1 and use absolute value
        return int(values[1])
    else:  # otherwise mode is 2 and its a reference value
        return int(opcodes[values[1]])


def less_than(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:  # immediate mode
            print(f'value becomes {para}')
            values.append(int(para))
        else:  # position mode
            print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))

    num1, num2, idx = values
    print(f'Checking if {num1} is less than {num2} and storing in {idx}')

    if num1 < num2:
        opcodes[idx] = 1
    else:
        opcodes[idx] = 0

    return cursor + 4

def equals(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:  # immediate mode
            print(f'value becomes {para}')
            values.append(int(para))
        else:  # position mode
            print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))

    num1, num2, idx = values
    print(f'Checking if {num1} equals {num2} and storing in {idx}')
    if num1 == num2:
        opcodes[idx] = 1
    else:
        opcodes[idx] = 0

    return cursor + 4

def add(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:
            print(f'value becomes {para}')
            values.append(int(para))
        else:
            print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))

    num1, num2, idx = values
    print(f'adding {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 + num2
    return cursor + len(parameters) + 1

def multiply(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        print(f'{para} has mode {modes[i]}')
        if i == len(parameters) - 1:
            print(f'parameter for storage, making it positional')
            values.append(para)
        elif int(modes[i]) == 1:
            print(f'value becomes {para}')
            values.append(para)
        else:

            print(f'value becomes {opcodes[para]}')
            values.append(int(opcodes[para]))
       

    num1, num2, idx = values
    print(f'multiplying {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 * num2
    return cursor + len(parameters) + 1


def save(cursor, modes):
    idx = get_nums(cursor, 1)
    print(f'Saving input at {idx}')

    opcodes[idx[0]] = int(input('Please enter your input: '))
    
    return cursor + 2
    


def output(cursor, modes):
    idx = get_nums(cursor, 1)
    print(f'Outputing the value at {idx}')

    print(opcodes[idx[0]])
    return cursor + 2

def stop(cursor, modes):
    print(f'Stopping')
    raise SystemExit

if __name__ == "__main__":

    with open('day5.txt') as fin:
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
    cursor = 0 

    while cursor is not None:
        print(f'Opcodes are {opcodes}')
        parameter = str(opcodes[cursor])
        op = parameter[-2:]
        op = ('0' + op) if len(op) == 1 else op
        modes = parameter[:-2][::-1] + '000' # flips the modes so they are left to right
        print(f'Opcode is {op} and modes are {modes}, calling {switch_dict[op]}')
        cursor = switch_dict[op](cursor, modes)
        print(f'cursor has been changed to {cursor}')