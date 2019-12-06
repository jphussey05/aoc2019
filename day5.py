def get_nums(cursor, num_items):

    answer = []
    print(f'Reading {num_items} parameter(s) in')
    for num in range(1, num_items + 1):
        answer.append(opcodes[num])
        print(f'Parameters are now {answer}')

    return answer


def add(cursor, modes):
    num1, num2, idx = get_nums(cursor, 3)
    
    # print(f'adding {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 + num2
    return cursor + 4


def multiply(cursor, modes):
    parameters = get_nums(cursor, 3)
    values = []

    for i, para in enumerate(parameters):
        print(f'{para} has mode {modes[i]}')
        if modes[i] == 0:
            print(f'value becomes {opcodes[para + 1]}')
            values.append(opcodes[para + 1])
        else:
            print(f'value becomes {para}')
            values.append(para)

    num1, num2, idx = values
    print(f'multiplying {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 * num2
    return cursor + 4


def save(cursor, modes):
    idx = get_nums(cursor, 1)
    print(f'Saving input at {idx}')

    opcodes[idx[0]] = input('Please enter your input: ')
    
    print(f'Incrementing the cursor to {cursor + 2}')
    return cursor + 2
    


def output(cursor, modes):
    idx = get_nums(cursor, 1)
    print(f'Outputing the value at {idx}')

    print(opcodes[idx[0]])
    return cursor + 2

def stop(cursor):
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
        '99': stop
    }
    
    opcodes = list(map(int, contents.split(',')))
    cursor = 0 

    while cursor is not None:
        print(f'Opcodes are {opcodes}')
        parameter = str(opcodes[cursor])
        op = parameter[-2:]
        modes = parameter[:-2][::-1] + '000' # flips the modes so they are left to right
        print(f'Opcode is {op} and modes are {modes}, calling {switch_dict[op]}')
        cursor = switch_dict[op](cursor, modes)