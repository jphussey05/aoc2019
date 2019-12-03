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
    print(f'Final list: {opcodes}')
    raise SystemExit


if __name__ == "__main__":

    with open('day2.txt') as fin:
        contents = fin.read()

    opcodes = list(map(int, contents.split(',')))
    
    #specified overwrites
    opcodes[1] = 12
    opcodes[2] = 2

    switch_dict = {
        '1': add,
        '2': multiply,
        '99': stop
    }

    cursor = 0
    while True:
        op = str(opcodes[cursor])
        cursor = switch_dict[op](cursor)