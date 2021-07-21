def lines_are_parallel(l1, l2):
    if(l1[1] != 0 and l2[1] != 0):
        if(l1[0]/l1[1] == l2[0]/l2[1]):
            print("They are parallel")
        else:
            print("They are not parallel")
    else:
        if(l1[2]/l1[0] == l2[2]/l2[0]):
            print("The lines are parallel")
        else:
            print("The lines are not parallel")
    

print("Enter the values of a, b, and c which correspond to ax+by=c")
li1 = []
li2 = []
print("Enter values of line 1")
for i in range(3):
    li1.append(float(input()))
print("Enter values of line 2")
for i in range(3):
    li2.append(float(input()))

lines_are_parallel(li1, li2)