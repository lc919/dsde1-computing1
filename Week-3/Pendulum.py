import math


L = int(input('Length of pendulum:'))
g = int(input('Value of g:'))
def pendulum(L, g):
    period = 2 * math.pi * math.sqrt((L/g))
    return period
print(pendulum(L, g))

if __name__=='__main__':
    pendulum()