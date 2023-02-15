town = input('Which town do you live in? ').lower()
bedrooms = int(input('How many bedrooms do you have? '))

council_tax = 0

# if town in ('london', 'manchester') and bedrooms <= 2:
#     council_tax = 10
# elif town == 'birmingham':
#     council_tax = 7
# else:
#     council_tax = 5

# print(council_tax)

city_not_many_bedrooms = False

if town in ('london', 'manchester') and bedrooms <= 2:
    council_tax = 10
    city_not_many_bedrooms = True
elif town == 'birmingham':
    council_tax = 7
else:
    council_tax = 5
    
print(council_tax)

if city_not_many_bedrooms:
    print("I'm in London or Manchester with 2 bedrooms or less!")
else:
    print("I'm not in London or Manchester!")
