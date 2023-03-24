import requests
from enigma import Enigma

mapping_url = "https://7w298.wiremockapi.cloud/enigma/mappings/long"
# mapping_url = "https://7w298.wiremockapi.cloud/enigma/mappings/short"
response = requests.get(mapping_url)
data = response.json()
rotors = data["rotors"]
reflectors = data["reflectors"]

reflector_setting = "A"
rotor_setting = ["I", "II", "III"]
# rotor_setting = ["II", "I", "III"]
# rotor_setting = ["III", "I", "II"]
enigma = Enigma(rotors, reflectors)
enigma.configure(rotor_setting, reflector_setting)

text = "Hello world, and how are you?"
encoded_text = enigma.encode_string(text)
decoded_text = enigma.encode_string(encoded_text)
print(f'Plain text: {text}')
print(f'Encoded: {encoded_text}')
print(f'Decoded: {decoded_text}')
