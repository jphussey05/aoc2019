# day6 aoc 2019

class Node(object):
    def __init__(self, name):
        self.name = name
        self.orbit = None  # things that orbit this node
        self.dist_to_com = 0
        self.path_to_com = list()

    def add_orbit(self, space_body):
        # create the thing you directly orbit
        self.orbit = space_body

    def create_path_to_com(self):
        
        if self.name == 'COM':
            return
        
        self.path_to_com.append(self.orbit.name)  # add the thing you directly orbit

        next_node = self.orbit
        while next_node.name != 'COM':
            self.path_to_com.append(next_node.orbit.name)
            next_node = next_node.orbit

        self.path_to_com.reverse()
        self.dist_to_com = len(self.path_to_com)

    def calc_dist_to_com(self):
        pass

bodies = dict()

with open('day6.txt') as fin:
    contents = fin.readlines()


# examine each orbit

for orbit in contents:
    orbit = orbit.strip()
    center, satellite = orbit.split(')')

# if either do not exist, create them
    if center not in bodies:
        bodies[center] = Node(center)
    if satellite not in bodies:
        bodies[satellite] = Node(satellite)
    
# create orbital relationship
    bodies[satellite].add_orbit(bodies[center])

orbit_sum = 0
for name, body in bodies.items():
    if name != 'COM':
        body.create_path_to_com()
        # print(f'---------{name}-----------')
        # print('-'.join(body.path_to_com))
        # print(f'# of orbits is {body.dist_to_com}')
        orbit_sum += body.dist_to_com

print(f'**********************\nTotal orbit number is: {orbit_sum}')

santa_path = bodies['SAN'].path_to_com
you_path = bodies['YOU'].path_to_com

common_path = list()
for idx, val in enumerate(santa_path):
    if val == you_path[idx]:
        common_path.append(val)
    else:
        break

print(common_path)
intersect = len(common_path)

print(len(santa_path[intersect:] + you_path[intersect:]))