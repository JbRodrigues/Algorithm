from random import randint


guess = int(input("Guess a number between 1 and 15 "))
number = randint(1,15)
atempt = 0
minimum = 1
maximum = number
guessing = bool(True)


while guessing != bool(False):

    if guess == number:
        atempt = 1;
        print("You Got it, the number is: " + str (number))
        guessing = bool(False)
    else:
        if(guess > number):
            maximum = guess - 1
            average = int((minimum  + maximum) / 2)
            guess = int(input("Too high, guess again between "+str(minimum) +"and"+str(average)+" "))
        elif(guess < number):
            minimum = guess + 1
            average = int((minimum  + maximum) / 2)
            guess = int(input("Too low, guess again between "+str(average) +" and "+str(maximum)+" "))




