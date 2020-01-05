import math

def quadsoln(a,b,c):	
	x = ((b*b) - (4*a*c))
	y = str((-0.5 * b/a))
	z = str(((-0.5* b/a)+(0.5 * (math.sqrt(((b*b) - (4*a*c))))/a)))
	v = str(((-0.5*b/a)+(-0.5 * (math.sqrt(((b*b) - (4*a*c)))))/a))
	if(a == 0):
		print("This is not a quadratic function. Please try again.")
	elif(x < 0):
		print("There are no real solutions to this equation.")
	elif(x == 0):
		print("Your solution is: " + y)
		return(y)
	else:
		print("Your solutions are: " + z + " and " + v)
		return (z, v)

#Call the fucntinoi from here.

#Pass a, b c as prameters ot thie fucntion.

#read the params from the main program
if __name__ == "__main__":
	print("Hi! You are going to work with a quadratic root calculator today.")
	print("As you know, a typical quadratic equation is ax^2 + bx + c.")
	print("Please enter the value of a")
	a = float(raw_input())
	print("please enter the value of b")
	b = float(raw_input())
	print("please enter the value of c")
	c = float(raw_input())
	quadsoln(a,b,c)
#    Call the fcntion here.
