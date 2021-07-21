x = int(input("Enter the base"))
n = int(input("Enter the exponent"))
def power(n):
	if(n == 0):
		return 1
	else:
		return(x * power(n - 1))

print(power(n))
