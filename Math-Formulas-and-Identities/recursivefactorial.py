x = int(input())
def fac(x):
	if(x == 0):
		return 1
	elif(x < 0):
		return("You need to enter a positive number")
	else:
		return(x * fac(x - 1))


print(fac(x))