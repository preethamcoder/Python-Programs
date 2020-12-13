import math, time
from math import *
#from scipy.integrate import quad
intervals = int(input("How many times do you want to compute the sum? (Larger number = more accuracy!) "))
upp = float(input("Enter upper bound: "))
low = float(input("Enter lower bound: "))
x = time.time()
def integrand(x):
    a = 1/x
    return(a)
value1 = 0
value2 = 0
for i in range(1, intervals+1):
    value1 += integrand(low+((i-1/2))*((upp-low)/intervals))
value2 = ((upp-low)/intervals)*value1
y = time.time()
print("------------------------------------------------------------------------------")
print("Here is your answer: ")
print(value2)
print("Runtime of this algorithm was: " + str(y-x) + " seconds!")