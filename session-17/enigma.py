import requests
import re


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
        rotors_reversed = list(reversed(self.rotor_setting))

        for rotor in self.rotor_setting:
            letter = rotor.value_from_key(letter)
        letter = self.reflector_setting.value_from_key(letter)

        for rotor in rotors_reversed:
            letter = rotor.key_from_value(letter)
        return letter

    def encode_string(self, message):
        message = self.sanitise_message(message)
        encoded_message = []
        for letter in [*message.upper()]:
            encoded_message.append(self.encode_char(letter))
        return "".join(encoded_message)

    def sanitise_message(self, message):
        return re.sub(r"[^A-Za-z]*", "", message)

mappings = requests.get('https://7w298.wiremockapi.cloud/enigma/mappings/long')
mapping_data = mappings.json()

r = Reflector("C")
x = Rotor("IV")
y = Rotor("II")
z = Rotor("V")

machine = Machine()
machine.config([x, y, z], r)

encode_message = machine.encode_string("Have you enjoyed learning Python?")
decode_message = machine.encode_string(encode_message)
print(encode_message)
print(decode_message)


# READ A FILE, ENCODE IT AND WRITE TO A FILE, THEN DECODE AND WRITE TO A FILE!
# stream = open('moby-dick.txt')
# output = open('output.txt', 'w')
# book = stream.readlines()
# for line in book:
#     output.writelines(machine.encode_string(line))

# stream = open('output.txt')
# output = open('decoded.txt', 'w')
# book = stream.readlines()
# for line in book:
#     output.writelines(machine.encode_string(line))



        # input = open('output.txt', "w")
        # decoded_message = input.readlines()
        # for line in decoded_message:
        #     self.encode_string(line)




# print(machine.encode_char("H"))
# print(x.value_from_key("H"))
# print(x.key_from_value("Q"))
# print(y.value_from_key("H"))
# print(y.key_from_value("Q"))
# print(z.value_from_key("H"))
# print(z.key_from_value("Q"))
# print(r.value_from_key("H"))
# print(r.key_from_value("Q"))
