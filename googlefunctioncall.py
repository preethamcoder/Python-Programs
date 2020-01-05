import urllib

print ("Please enter the url you want to test")
urlToOpen = str(raw_input())
def googleverify(urlToOpen):
	a = urllib.urlopen(urlToOpen)
#print(a.read())
	y = a.read()
	#print (y)
#print(len(y))
	if(y.find("Google Search") != -1):
		print("This is stage 1")
		if(y.find("I'm Feeling Lucky") != -1):
			print("This is stage 2")
			if(y.find("About") != -1):
				print("This is stage 3")
				#print(y.find("Gmail"))
				if(y.find("Gmail") != -1):
					print("Yes, this is Google.")
	else:
		print("No, this is not Google.")

googleverify(urlToOpen)

#Run the program till the input is given as www.afs.com.

