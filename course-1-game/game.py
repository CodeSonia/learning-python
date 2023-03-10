import requests

def string_to_ints(str):
    x, y = str.split(':')
    return [int(x), int(y)]

# Convert from an x/y string (e.g. '2:1') to a compass point ('n', 's', 'e', 'w')
# same x but y is higher = north
# same x but y is lower = south
# x is lower and y is the same = west
# x is higher and y is the same = east
def convert_direction(current_node, current_location):
    nodes = current_node['nodes']
    can_go = []
    for node in nodes:
        x, y = string_to_ints(node)
        current_x, current_y = string_to_ints(current_location)

        if x == current_x and y > current_y:
            can_go.append("n")
        if x > current_x and y == current_y:
            can_go.append("e")
        if x == current_x and y < current_y:
            can_go.append("s")
        if x < current_x and y == current_y:
            can_go.append("w")

    return can_go

# Convert from a compass point ('n', 's', 'e', 'w') to a x/y string (e.g. '2:1')
def convert_compass_point(compass_point, current_location):
    x, y = current_location.split(':')
    if compass_point == 'n':
        return f'{x}:{int(y) + 1}'
    elif compass_point == 's':
        return f'{x}:{int(y) - 1}'
    elif compass_point == 'e':
        return f'{int(x) + 1}:{y}'
    elif compass_point == 'w':
        return f'{int(x) - 1}:{y}'


r = requests.get('https://7w298.wiremockapi.cloud/labyrinth')
if r.status_code == 200:
    print(r.status_code)
    data = r.json()
    print(data['name'])
    print(data['description'])

    start_node = ""
    current_location = ""
    for location in data['maze']:
        current_location = location
        node = data["maze"][location]
        if node['entrance'] == True:
            print("You are in the game!")
            start_node = node
            break
        else:
            print("You need to find the entrance... keep digging!")

    current_node = start_node

    while current_node['alive'] and not current_node["exit"]:
        print(current_node['description'])
        next_node = input(f"Where would you like to move? The available nodes are: {convert_direction(current_node, current_location)} ")

        node_key = convert_compass_point(next_node, current_location)
        current_node = data['maze'][node_key]
        current_location = node_key

    print(current_node['description'])
else:
    print(f"Sorry, something went wrong! The status code: {r.status_code} ")
