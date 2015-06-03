from random import randrange

def results(user_ans,ans):
    if user_ans == int(ans):
        print("Brilliant, You're right!!!")
    else:
        print ("Incorrect, You'll get better with practice!!! The correct answer was",int(ans))

    
choice = "Y"
while (choice.upper()=="Y"):
    a = randrange(10)
    b = randrange(10)
    try:
        ans = (a/b)
    except ZeroDivisionError: #if division by zero error occurs 
        pass
    try:
        if int(ans)==float(ans):
            user_ans = input (str(a)+"/"+str(b)+"=")
            user_ans = int(user_ans)
            results(user_ans, ans)
            choice =input("Play again? (y/n)   ")

    except ValueError:#if user enters strings or float
        print("Please enter integers only!")
