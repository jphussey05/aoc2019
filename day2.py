def get_nums(cursor):
    return opcodes[opcodes[cursor + 1]], opcodes[opcodes[cursor + 2]], opcodes[cursor + 3]

def add(cursor):
    num1, num2, idx = get_nums(cursor)
    
    # print(f'adding {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 + num2
    return cursor + 4


def multiply(cursor):
    num1, num2, idx = get_nums(cursor)

    # print(f'multiplying {num1} and {num2}, storing at index {idx}')
    opcodes[idx] = num1 * num2
    return cursor + 4


def stop(cursor):
    print(f'Final list: {opcodes[0]}')

    if opcodes[0] == 19690720:
        print(100 * opcodes[1] + opcodes[2])
        raise SystemExit
    else:
        return


if __name__ == "__main__":

    with open('day2.txt') as fin:
        contents = fin.read()    
    
    switch_dict = {
        '1': add,
        '2': multiply,
        '99': stop
    }
    
    for noun in range(0, 100):
        for verb in range(0, 100):
            print(f'Testing {noun} and {verb}')
            opcodes = []
            opcodes = list(map(int, contents.split(',')))
            
            #specified overwrites
            opcodes[1] = noun
            opcodes[2] = verb
            cursor = 0

            while cursor is not None:
                op = str(opcodes[cursor])
                cursor = switch_dict[op](cursor)