import requests

# r = requests.get('http://api.open-notify.org/astros.json')
# r.status_code
# print(r.status_code)

# print(r.json())

star_wars = requests.get('http://swapi.dev/api/planets/1/')
print(star_wars.status_code)

print(star_wars.json())


