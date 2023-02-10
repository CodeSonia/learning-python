# Dates

# from datetime import datetime, timedelta

# today = datetime.now()

# two_days = timedelta(days=2)
# print(today + two_days)

# birthday = input('When is your birthday: ')

# print('My birthday is ' + str(datetime.strptime(birthday, "%d %m %y")))

# Error handling

# x = 10
# y = 0
# try:
#     print(x / y)
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("else!!!")
# finally:
#     print("this is done")

# Conditional logic

# Fix the mistakes in this code and test based on the description below
# If I enter 2.00 I should see the message "Tax rate is: 0.07"
# If I enter 1.00 I should see the message "Tax rate is: 0.07"
# If I enter 0.50 I should see the message "Tax rate is: 0"

price = float(input('how much did you pay? '))

if price >= 1.00:
    tax = .07
    bonus = 2.00
elif price == 0.99:
    tax = 1.00
else:
    tax = 0
    bonus = 3.00
print('Tax rate is: ' + str(tax))

