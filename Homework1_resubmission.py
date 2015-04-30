name= input("What is your name?")
print("Hello" +'\t'  + name + '\t' + "Lets play a Game") 
print("Guess a random number between 1 - 100, and I'll try to guess it.")
numberOfGuess =0
max = 100
min = 0
number =0
guess = (max + min)/2

while True:
	numberOfGuess +=1
	print("Is it " + str(guess))
	answer = input("Yes/No")
	if answer == No:
		print("Is it greater" + str(guess))
		numberOfGuess +=1
	if answer == No:
		guess1 = (guess - min)/2
		print("Is it " + str(guess1))
		numberOfGuess +=1
		if answer == No:
			print("Is it greater" + str(guess1))
			numberOfGuess +=1
		if answer == Yes:
			print("Is it 27")
			numberOfGuess +=1
		if answer == Yes:
			print("I got it right " + numberOfGuess)
			numberOfGuess =0
		print("Do you want to play again")
		if answer == Yes:
			print("Is it " + str(guess))
			numberOfGuess += 1
		if answer == No:
			print("Is it greater" + str(guess))
			numberOfGuess += 1
		if answer == Yes:
			guess2 = (guess + max)/2
			print("Is it " + str(guess2))
			numberOfGuess += 1
		if answer == No:
			print("Is it greater than" + str(guess2))
			numberOfGuess += 1
		if answer == Yes:
			print("Is it 88")
			numberOfGuess += 1
		if answer == Yes:
			print("I got it right" + numberOfGuess)
			numberOfGuess = 0
			print("Do you want to play again ?")
		else answer == No:
			print("Bye Bye!! See you again!!")








