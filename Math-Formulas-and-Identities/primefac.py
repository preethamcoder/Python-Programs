x = int(input())
factors = []
div = 2

while(x >= div):
	if(x % div == 0):
		factors.append(div)
		x /= div
	else:
		div += 1

print(max(factors))