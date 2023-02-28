import math
from random import randint



#define a random number between 1 and 100
number = randint(1,100)
attempt = 0
minn = 1
maxx = 100
#set the middle of range
guess = int(input("Guess a number between 1 and 100 "))
while minn <  maxx:
    attempt += 1
    if(guess > number):
        maxx = guess
        midd = math.floor(int(minn + maxx) / 2)
        print("Attempt " + str(attempt))
        guess = int(input("Too high, Try " + str(midd) + " "))
    elif(guess < number):
        minn = guess
        midd = math.floor(int(minn + maxx) / 2)
        print("Attempt " + str(attempt))
        guess = int(input("Too Low, Try " + str(midd) + " "))
    if guess == number:
        print("You Got it, with " + str(attempt) + " attempts")
        break





