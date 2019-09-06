'''
This program stores a random number between 0 and 1023 and asks the user to
guess the number of skittles. It will promt the user if their guess is too high
or too low to make it easier. Once the user guesses the correct number, the
program will stop. 
'''
#Miki Ando

import random
skittles = random.randint(0,1024)

print("I'm thinking of a number between 0 and 1023. What is it?")
while True:
    guess = int(input("Enter number: "))
    if guess < skittles:
        print ("Too low!")
    if guess > skittles:
        print ("Too High!")
    if guess == skittles:
        print ("Correct!")
        break
