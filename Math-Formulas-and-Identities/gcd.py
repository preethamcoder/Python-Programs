import time
a = int(input())
b = int(input())
def gcdret(a, b):
    if(a == 1 or b == 1):
        return 1
    while(a > 0 and b > 0):
        if a > b:
            a -= b
        else:
            b -= a
    return (max(a,b))
def lcm(x,y):
    if(x == 1 or y == 1):
        return x*y
    return((x*y)//gcdret(x,y))

x = time.time()
#print(x)
xa = gcdret(a,b)
xb = lcm(a,b)
y = time.time()
#print(y)
print("The GCD is " + str(xa) + " and the LCM is: " + str(xb) + "\nThe time it took to run is: " + str(y-x) + " seconds.")