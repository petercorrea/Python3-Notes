def square(value): 
    """This function will square any number"""
    new_value = value ** 2
    print(new_value)
    
?def raised_to_power(num1, num2):
    """This function takes two parameters; a base, and the power."""
    new_value = num1 ** num2
    print(new_value)
    
raised_to_power(4,2)

#Returning mutiple values
def raise_both(val1, val2):
    '''This will return each argument raised by the other'''
    num1 = val1 ** val2
    num2 = val2 ** val1
    
    new_tuple = (num1, num2)
    
    print(new_tuple)
    
raise_both(4,3)

#Default values for arguments
#You can still a specific value in place of the default, but when spcification is absent
#Python will utilize the default

def power_in_tens(value, power=10):
    new_value = value ** power
    print(new_value)
    
power_in_tens(2)
power_in_tens(2, 2)

#Flexible arguments
def sum_all(*args): #Allows you to take in an undefined amount of variables 
    
    #Initialize a zero value
    sum_all = 0
    
    #Loop through the arguments
    for values in args:
        sum_all += values
    print(sum_all)
    
sum_all(1,2,3)
sum_all(1,2,3,4,5)

#Keyword Arguments
def print_all(**kwargs): #same as *args but with keyworded variables
    for key, value in kwargs.items():
        print(key + ": " + value)

print_all(name = "Peter Correa", instrument = "Saxophone")

#Lambda Functions
#quick way to write functions

raise_to_power = lambda x,y : x**y
raise_to_power(2,4)

#map function
#Two parameters; a function and a sequence 

seq = [2,4,6,8]
square_all = map(lambda num : num ** 2, seq)
list(square_all)

# Lambdas are anonymous fucntions. Lambdas can't contain new lines (outside of containers) or assignments.

lambda x, y: x + y

meals = [
    {'name': 'cheeseburger',
     'calories': 750},
    {'name': 'cobb salad',
     'calories': 250},
    {'name': 'large pizza',
     'calories': 1500},
    {'name': 'burrito',
     'calories': 1050},
    {'name': 'stir fry',
     'calories': 625}
]

high_cal = filter(lambda meal: meal['calories'] > 1000, meals)
list(high_cal)

from functools import reduce

strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven know and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]

longest = reduce(lambda string1, string2: string1 if len(string1) >  len(string2) else string2 , strings)
longest

# Partials allow us to create functions with an incomplete (or partial) list of arguments.
# Currying allows us to return an alternate versions of our function, from inside the function based on the number of arguments we passed.

from functools import partial


def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))
