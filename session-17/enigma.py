import requests

class Reflector:
    def __init__(self, id):
        self.id = id
        pass

    def value_from_key(self, key):  
        return self.get_key_setting()[key]

    def key_from_value(self, value):
        key = [k for k, v in self.get_key_setting().items() if v == value]
        return key[0]
        
    def get_key_setting(self):
        return mapping_data["reflectors"][self.id]

class Rotor(Reflector):
    def __init__(self, id):
        super().__init__(id)
        pass

    def get_key_setting(self):
        return mapping_data["rotors"][self.id]

class Machine:
    def __init__(self):
        
      pass



mappings = requests.get('https://7w298.wiremockapi.cloud/enigma/mappings/long')

mapping_data = mappings.json()

rotor_setting = ["I","II","III"]


r = Reflector("A")   
x = Rotor("I")
y = Rotor("II")
z = Rotor("III")

print(x.value_from_key("H"))  
print(x.key_from_value("Q")) 
print(y.value_from_key("H"))  
print(y.key_from_value("Q"))  
print(z.value_from_key("H"))  
print(z.key_from_value("Q"))   
print(r.value_from_key("H"))  
print(r.key_from_value("Q"))   