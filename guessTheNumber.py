#This is the guess number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')



# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())



if guess < secretNumber:
    print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
        else:
            break #this condition is correct guess!
        if guess == secretNumber:
            print('Good job! you guesssed my number in '+str(guessesTaken)+' guesses!')
            else:
                print('Nope. The number i was thinking was '+str(secretnumber))
