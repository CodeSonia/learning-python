#Example adapted from https://www.programiz.com/python-programming/decorator

def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        print(func().upper())
    # return the inner function
    return inner

#This will pass ordinary() into make_pretty where it will become func
@make_pretty
def ordinary():
    return "I am ordinary"

ordinary()

