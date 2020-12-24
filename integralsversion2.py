import math
from scipy import integrate
def f(x):
    return math.sqrt(math.sin(x))/(math.sqrt(math.sin(x))+math.sqrt(math.cos(x)))

#def bounds_y():
    #return [0, 0.5]

def bounds_x():
    return [0, math.pi/4]

xa = integrate.nquad(f, [bounds_x])
print(xa)