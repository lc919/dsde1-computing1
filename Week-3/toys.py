'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''

a = int(input('enter a number:'))
b = int(input('enter another number:'))
# write a function that adds 1
# to the input and prints the result
def inc(a):
    return(a)
print ('your first number was ' + str(inc(a)))

# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    product = a + 1
    return product # hint this is incomplete
print ('your first number plus one is ' + str(inc_return(a)))

# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    product = a + b
    return product
print('your first number plus the second is ' + str(sum(a, b)))


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
print('your first number plus the second plus one is ' + str(sum(a,b)+1))


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
c = int(input('yo gimme an even number:'))
def is_even(c):
    if c%2 == 0:
        return True
    else:
        return False
if is_even(c) == True:
    print('well done')
else:
    print('nope')

# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
d = str(input('tell me a phrase:'))
e = int(input('tell me a number:'))
def string_repeat(d, e):
    product = d * e
    # hint: you can add strings together 
    # in order to concatenate them
    return product
print(string_repeat(d, e))

