#Open googel.com and Verify that the site opened is google.com.
#The output of the program is "Yes" if it actauly open a google.com.
#The Output of the program is "No" if it opened some other site.

import urllib

print ("Please enter the url you want to test")
b = str(raw_input())
a = urllib.urlopen(b)
#print(a.read())
y = a.read()
print (y)
#print(len(y))
if(y.find("Google Search") != -1):
	print("This is the start")
	if(y.find("I'm Feeling Lucky") != -1):
		print("Yes, this is Google")
else:
	print("No, this is not Google.")
#for x in y:
#	print x

#print "End of the program"
