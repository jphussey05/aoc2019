from shapely.geometry import LineString

def decompose(figure):
    moves = figure.split(',')
    points = []
    
    for move in moves:
        direction = move[0]
        length = int(move[1:])
        if points:
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

        points.append(LineString([prev_point, newpoint]))

    return points

if __name__ == "__main__":
    
    with open('day3.txt') as fin:
        contents = fin.readlines()

    fig1, fig2 = contents[0].strip(), contents[1].strip()
    isections = list()

    lines1 = decompose(fig1)
    lines2 = decompose(fig2)    

    for line_a in lines1:
        for line_b in lines2:
            result = line_a.intersection(line_b)
            if result:
                isections.append(result)

    min_length = None
    
    for i in isections[1:]:
        man_dist = abs(i.bounds[0]) + abs(i.bounds[1])
        if not min_length or man_dist < min_length:
            min_length = man_dist
            min_point = i

    print(f'Minimum manhattan distance is {min_length} to {min_point}')

    # TODO take all of the intersections and step through the decomposed line strings calculating the length all the way. Find minimum.