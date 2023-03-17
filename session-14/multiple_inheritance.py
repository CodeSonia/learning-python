class Mammal:
  def __init__(self):
    print('mammal!!')

  def mammal_speak(self):
    print("hello")


class FourLeggedFriend:
  def __init__(self):
    print('four legged friend!!')

  def four_legged_speak(self):
    print("hello from your four legged pal")

class Dog(Mammal, FourLeggedFriend):
  def __init__(self, breed):
    self.breed = breed

  # def speak(self):
  #   super().speak()


widget = Dog('spaniel')
print(widget.breed)

widget.four_legged_speak()
widget.mammal_speak()

print(isinstance(widget, Mammal))


