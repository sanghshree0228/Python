
class Animal:
    def __init__(self, name):
        self.name = name

    def guess_who_am_i(self):
        i = 1
        for hint in (hint_data[self.name]):
            print ("\tHint "+str(i)+": "+hint)
            answer = input ("\tWho am I?\t")
            if answer== self.name:
                print ("\tYou're smart! I am a "+self.name)
                break
            else:
                print ("\tMaybe, the next hint will help you\n")
                i +=1
            if i > 3:
                print("\tSorry, I am out of hints")
                print ("\tThe answer was "+self.name)
            
hint_data = {"elephant": ["I have exceptional memory", "I am the largest land-living mammal in the world", "I have a trunk"],"tiger":["I am the biggest cat", "I come in black and white or orange and black", "I am a carnivore"],"bat":["I use echo-location", "I can fly", "I see well in dark"]}
e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

print ("\t\t""I will give you 3 hints, guess what animal I am")

print ("\n\nGuess the first Animal:")
e.guess_who_am_i()
print ("\n\nGuess the second Animal:")
t.guess_who_am_i()
print ("\n\nGuess the thrid Animal:")
b.guess_who_am_i()
