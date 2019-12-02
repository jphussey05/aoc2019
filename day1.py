def calc_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)

with open('day1.txt') as fin:
    contents = fin.readlines()

fuel_costs = [calc_fuel(int(module.strip())) for module in contents]

print(sum(fuel_costs)) 