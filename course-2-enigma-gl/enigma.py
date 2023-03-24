import re

from rotor import Rotor

class Enigma:
    def __init__(self, rotor_mappings, reflector_mappings):
        self.rotor_mappings = rotor_mappings
        self.reflector_mappings = reflector_mappings
        self.rotors = {}
        self.reflector = ""
        self.rotor_setting = []
        self.rotor_setting_reversed = []
        self.reflector_setting = ""

    def configure(self, rotor_setting, reflector_setting):
        self.rotor_setting = rotor_setting
        self.rotor_setting_reversed = list(reversed(rotor_setting))
        self.reflector_setting = reflector_setting
        self.reflector = Rotor(self.reflector_mappings[reflector_setting])
        for rotor in self.rotor_setting:
            self.rotors[rotor] = Rotor(self.rotor_mappings[rotor])

    def encode_char(self, letter):
        for rotor_id in self.rotor_setting:
            rotor = self.rotors[rotor_id]
            letter = rotor.value_from_key(letter)

        letter = self.reflector.value_from_key(letter)

        for rotor_id in self.rotor_setting_reversed:
            rotor = self.rotors[rotor_id]
            letter = rotor.key_from_value(letter)

        return letter

    def encode_string(self, plain_text):
        cypher_text = []
        plain_text = re.sub(r"[^A-Za-z]*", "", plain_text)

        for char in [*plain_text.upper()]:
            encoded_char = self.encode_char(char)
            cypher_text.append(encoded_char)

        return "".join(cypher_text)
