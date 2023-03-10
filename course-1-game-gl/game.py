import requests
import json
from position import *

# Load the maze, from a file
# file = open("api/labyrinth.json")
# data = json.loads(file.read())
# file.close()

# Load the maze, from an API
api_url = "https://7w298.wiremockapi.cloud/labyrinth"
response = requests.get(api_url)
data = response.json()

# Print the name and description
print("--------------------------------------------------------------------------------")
print(data["name"].upper())
print(data["description"])
print("--------------------------------------------------------------------------------\n")

# Find the entrance
for key in data["maze"]:
    node = data["maze"][key]
    if node["entrance"]:
        current_position = key
        current_node = node

# Keep going until you die or make it out
while current_node["alive"] and not current_node["exit"]:
    print(current_node["description"])
    print()
    print("You can go...")
    print(can_go(current_position, current_node["nodes"]))
    old_current_position = current_position
    old_current_node = current_node

    try:
        direction = input("Direction? ")
        if direction == "n":
            current_position = north(current_position)
        if direction == "s":
            current_position = south(current_position)
        if direction == "e":
            current_position = east(current_position)
        if direction == "w":
            current_position = west(current_position)
        current_node = data["maze"][current_position]
    except KeyError:
        print("You can't go that way!")
        current_position = old_current_position
        current_node = old_current_node

# You're dead or you've made it out alive
print(current_node["description"])
