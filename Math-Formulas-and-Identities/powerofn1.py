import math, time
n = int(input())
sum = 0
x = time.time() 
for i in range(n+1):
    #a = str(i)
    #b = a[len(a)-1]
    #c = int(b) % 2
    sum += math.pow(-1, i)
y = time.time()

print(sum)
print("Time to run (in seconds) is: " + str(y-x))