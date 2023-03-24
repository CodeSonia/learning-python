import requests


class Reflector:
    def __init__(self, id):
        self.id = id

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

    def config(self, rotor_setting, reflector_setting):
        self.rotor_setting = rotor_setting
        self.reflector_setting = reflector_setting

    def encode_char(self, letter):
        for rotor in self.rotor_setting:
            letter = rotor.value_from_key(letter)
        letter = self.reflector_setting.value_from_key(letter) 

        for rotor in reversed(self.rotor_setting):
            letter = rotor.key_from_value(letter)  
        return letter 
    
     


mappings = requests.get('https://7w298.wiremockapi.cloud/enigma/mappings/long')
mapping_data = mappings.json()

rotor_setting = ["I", "II", "III"]


r = Reflector("A")
x = Rotor("I")
y = Rotor("II")
z = Rotor("III")

machine = Machine()
machine.config([x, y, z], r)

print(machine.encode_char("H"))


# print(x.value_from_key("H"))
# print(x.key_from_value("Q"))
# print(y.value_from_key("H"))
# print(y.key_from_value("Q"))
# print(z.value_from_key("H"))
# print(z.key_from_value("Q"))
# print(r.value_from_key("H"))
# print(r.key_from_value("Q"))
