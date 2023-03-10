import requests

def convert_direction(current_node, current_location):
    nodes = current_node['nodes']
    can_go = []
    for node in nodes:
        x = int(node[0])
        y = int(node[2])

        current_node_x = int(current_location[0])
        current_node_y = int(current_location[2])


        if x == current_node_x and y > current_node_y:
            can_go.append("n")

        if x == current_node_x and y < current_node_y:
            can_go.append("s")

        if x < current_node_x and y == current_node_y:
            can_go.append("w")

        if x > current_node_x and y == current_node_y:
            can_go.append("e")
    print(can_go)
    return can_go

    #same x but y is higher = north
    #same x but y is lower = south
    #x is lower and y is the same = west
    #x is higher and y is the same = east

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
        next_node = input(f"Where would you like to move? The available nodes are: {convert_direction(current_node, current_location)}")

        current_node = data['maze'][next_node]

    print(current_node['description'])
else:
    print(f"Sorry, something went wrong! The status code: {r.status_code} ")
