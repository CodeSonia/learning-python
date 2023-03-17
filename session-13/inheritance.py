# Parent class
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print("I am a dog")

# Child class
class Pomeranian(Dog):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    def __str__(self):
        super().__str__()
        return "I am a pomeranian"


pegasus = Pomeranian("pegasus", "tiny")
# print(pegasus.size)
# tiny

print(pegasus)
# I am a dog
# I am a pomeranian