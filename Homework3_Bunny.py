#Bunny Program

def isEven(value):
	if(value%2==0):
		return True;
	else:
		return False;

def bunnyEars2(value):
	if(value == 0): 
		return 0
	elif(isEven(value)):
		return bunnyEars2(value - 1) + 3
	else:
		return bunnyEars2(value - 1) + 2

lineNumber = int(input("What is the line position: "))
print("Total Ears: " + str(bunnyEars2(lineNumber)))
