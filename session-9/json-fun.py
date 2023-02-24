import requests
import json

def astros_in_space(records):
  astros_on_craft = {}

  for record in records:
    print(f"{record['name']} is on {record['craft']}")
    # put people in array, keyed by craft...
    # if record['craft'] not in astros_on_craft:
    #   astros_on_craft[record['craft']] = []
    # astros_on_craft[record['craft']].append(record['name'])
    # print(astros_on_craft)

r = requests.get('http://api.open-notify.org/astros.json')

data = r.json()
astros_in_space(data['people'])
print(f"There are [{data['number']}] people in space!")

devs_in_space = [
  {"name": "Rosa", "craft": "ISS"},
  {"name": "Sonia", "craft": "Shenzhou 15"},
  {"name": "Graham", "craft": "Moonraker"}
]

# print(json.dumps(devs_in_space))
astros_in_space(devs_in_space)
