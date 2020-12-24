import math
print("We are going to explore the distinct permutations of this specific string")
a = str(input())
uniquelet = set(a.lower())
perm = math.factorial(len(a))
for i in uniquelet:
    x = a.count(i)
    perm /= math.factorial(x)
    
print("There are "+str(int(perm))+" possible permutations of the word " + a + ".")