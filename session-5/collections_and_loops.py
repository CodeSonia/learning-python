''' Using lists '''

names = ['Rosa', 'Sonia', 'Alex'] 

names.append('Graham')

names.sort()

# print(names)

''' Using array'''

from array import array 

age = array('i')

age.append(29)
age.append(30)
age.append(31)

# print(age[0:2])

'''Using dictionaries'''

uxm_devs = []
alex = {"first": "Alex", "last": "Newton"}
rosa = {"first": "Rosa", "last": "Fox"}
sonia = {"first": "Sonia", "last": "Hussain"}

uxm_devs.append(alex)
uxm_devs.append(rosa)
uxm_devs.append(sonia)

# print(uxm_devs)

''' Using loops '''

for name in names:
    print(name)

for x in range(0, 5):
    print(x)

index = 0 
while index <= 10:
    print(index)
    index = index + 1