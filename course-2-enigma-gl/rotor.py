ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Rotor:
    def __init__(self, mapping):
        self.mapping = mapping
        # for i in range(0, 26):
        #     self.mapping[ALPHABET[i]] = mapping[i]

    def value_from_key(self, key):
        return self.mapping[key]

    def key_from_value(self, value):
        key = [k for k, v in self.mapping.items() if v == value]
        return key[0]
