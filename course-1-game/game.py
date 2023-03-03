import requests

r = requests.get('https://7w298.wiremockapi.cloud/labyrinth')
if r.status_code == 200:
    print(r.status_code)
    data = r.json()
    print(data['name'])
    print(data['description'])

    start_node = ""

    for location in data['maze']:
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
        next_node = input(f"Where would you like to move? The available nodes are: {current_node['nodes']}")

        current_node = data['maze'][next_node]

    print(current_node['description'])
else:
    print(f"Sorry, something went wrong! The status code: {r.status_code} ")


