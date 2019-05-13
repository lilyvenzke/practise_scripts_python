#what is the numbe rof people on the bus?
# a list with tuples are received. First  digit represents number of people getting on the bus.
#second in tuple represents how many peole get Off bus. at each stop. Each tuple represents busstops
#resource: Codewars
def  number(bus_stops):
    people = 0
    total = 0
    for stop in bus_stops:
        people = stop[0] - stop[1]
        total = total + people
    return total

myinput = [[3,0], [9, 1],[4, 10], [12, 2], [6, 1], [7, 10]]
print(number(myinput))
