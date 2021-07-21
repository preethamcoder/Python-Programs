import math, time
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return(n * factorial(n-1))
x1 = lambda a, b : int(math.comb(a,b))
def pascaltriangle():
    print("Enter the last row of Pascal's Triangle you would like to see: ")
    pascalrow = int(input())
    ans = "1\n"
    t1 = time.time()
    for i in range(1, pascalrow+1):
        for j in range(i):
            y = x1(i,j)
            #y = int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
            ans += str(y) + " "*4
            #ans = (i-j)*" " + ans
        ans += "1\n"
    print()
    ab = ans.split("\n")
    i = 0
    for n in ab:
        n = (len(ab)-2-i)*"  " + n
        i += 1
        print(n)
    #print(ans.split("\n"))
    t2 = time.time()
    print("Runtime for this algorithm is " + str(t2-t1) + " seconds!")
pascaltriangle()