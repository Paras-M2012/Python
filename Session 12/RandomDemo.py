import random

'''
this will print random number from this 1 to 100
'''
num=random.randint(1,20)

while True:
    guess=int(input("Guess a Number Between 1 to 20 : "))
    if guess==num:
        print("You Guessed A Correct Number")
        break
    elif guess>num:
        print("You Guessed A Greater Number")
    elif guess<num:
        print("You Guessed A Smaller Number")
