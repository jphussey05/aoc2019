from shapely.geometry import LineString
from shapely.ops import split
from shapely.geometry import Point

def decompose(figure):
    moves = figure.split(',')
    points = [(0,0)]
    
    for move in moves:
        direction = move[0]
        length = int(move[1:])
        if len(points) > 1:
            prev_point = newpoint
        else:
            prev_point = (0,0)
        prev_x, prev_y = prev_point

        if direction == 'R':
            newpoint = prev_x + length, prev_y
        elif direction == 'L':
            newpoint = prev_x - length, prev_y
        elif direction == 'D':
            newpoint = prev_x, prev_y - length
        elif direction == 'U':
            newpoint = prev_x, prev_y + length
        else:
            print(f'Encountered an incorrect direction, {direction}, bailing!')
            raise SystemExit

        points.append(newpoint)

    return LineString(points)

if __name__ == "__main__":
    
    # read in instructions
    with open('day3.txt') as fin:
        contents = fin.readlines()
        fig1, fig2 = contents[0].strip(), contents[1].strip()

    # create LineFigures from instructions and then find intersections
    lines1 = decompose(fig1)
    lines2 = decompose(fig2)    
    isections = lines1.intersection(lines2)

    min_length = None
    min_steps = None
    for i in isections:
        if i == Point((0,0)):  # guarding clause for origin point
            continue

        man_dist = abs(i.bounds[0]) + abs(i.bounds[1])
        
        # split figures at each intersection and total length of first halves 
        partial_line1 = split(lines1, i)
        partial_line2 = split(lines2, i)
        steps = partial_line1[0].length + partial_line2[0].length

        if not min_length or man_dist < min_length:
            min_length = man_dist
            min_point = i
        if not min_steps or steps < min_steps:
            min_steps = steps
            min_step_point = i

        print(f'{i} - Manhattan distance is {man_dist}, Steps are {steps}')

    print(f'Minimum Manhattan distance is {min_length} to {min_point}')
    print(f'Minimum steps to an intersection are {min_steps} to {min_step_point}')
