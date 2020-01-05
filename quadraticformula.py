import math


def quadsoln(a,b,c):	
	if(a == 0):
		print("This is not a quadratic function. Please try again.")
	elif(((b*b) - (4*a*c)) < 0):
		print("There are no real solutions to this equation.")
	elif(((b*b) - (4*a*c)) == 0):
		print("Your solution is: " +str((-0.5 * b/a)))
	else:
		print("Your solutions are: " +str(((-0.5* b/a)+(0.5 * (math.sqrt(((b*b) - (4*a*c))))/a))) + " and " + str(((-0.5*b/a)+(-0.5 * (math.sqrt(((b*b) - (4*a*c)))))/a)))


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
