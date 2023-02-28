import math
from random import randint



#define a random number between 1 and 100
number = randint(1,100)
atempt = 0
minn = 1
maxx = 100
midd = math.floor(int(minn + maxx) / 2)
print(str(number))
guess = int(input("Guess a number between 1 and 100 "))
while minn <  maxx:
    atempt += 1
    print("Range " + str(minn) + " and " + str(maxx))
    if guess == number:
        print("You Got it, with " + str(atempt) + " atempts")
        break
    else:
        if(guess > number):
            maxx = midd
            print("Tentativa " + str(atempt))
            midd = math.floor(int(minn + maxx) / 2)
            guess = int(input("Too high, Try " + str(midd) + " "))
        elif(guess < number):
            minn = midd
            midd = math.floor(int(minn + maxx) / 2)
            print("Tentativa " + str(atempt))
            guess = int(input("Too Low, Try " + str(midd) + " "))




