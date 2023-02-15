# Function without a parameter
def say_hello():
  print("hello!!")

say_hello

# Function with a parameter
def say_hello(name):
  print("hello " + name)

say_hello('Alex')

# Function with 2 parameters, one has a default value of true
def get_initial(name, force_uppercase=True):
  if force_uppercase:
    initial = name[0:1].upper()
  else:
    initial = name[0:1]
  return initial

# Function which we use to call get_initial() and then print all the initials
def all_name_intials():
  first_name = input('What is your first name? ')
  # Don't specify True as its the default value in get_initial()
  first_name_intial = get_initial(first_name)

  middle_name = input('What is your middle name? ')
  # Specify False as its not the default value in get_initial()
  middle_name_initial = get_initial(middle_name, False)

  last_name = input('What is your last name? ')
  # Call the function using named parameters, this means we can put them in any order //
  # and its easier to read
  last_name_initial = get_initial(force_uppercase = False, name = last_name)

  print(first_name_intial + middle_name_initial + last_name_initial)

all_name_intials()