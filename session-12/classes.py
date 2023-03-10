# class Dog():
#     def __init__(self, breed):
#         self.breed = breed
    
#     def speak(self):
#         return "Woof!"

# husky = Dog("husky")
# # print(husky.breed)
# # returns husky
# print(husky.speak())
# # returns Woof!

class Cat():
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    
    @property
    def breed(self):
        print("I'm in the getter breed!")
        return self.__breed
    
    @breed.setter
    def breed(self, value):
        print("I'm in the setter breed!")
        self.__breed = value
    
    @property
    def name(self):
        print("I'm in the getter name!")
        return self.__name
    
    @name.setter
    def name(self, value):
        print("I'm in the setter name!")
        self.__name = value

loki = Cat("tabby", "loki")
print(f"{loki.name} is a {loki.breed}")

