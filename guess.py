import random

guessesTaken = 0

print('Welcome to my guessing game! Could you tell me your name, please?')
myName = input()

number = random.randint(1, 20)
print('Thank you, ' + myName + ', I am thinking of a number between 1 and 100.')

while guessesTaken < 15:
	print('Take a guess at the number.')
	guess = input()
	guess = int(guess)

guessesTaken = guessesTaken + 1

if guess < number:
	print('Sorry, your guess is too low.')

if guess > number:
	print('Sorry, your guess is too high.')

if guess == number:
	break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Awesome, ' + myName + '! You guessed the number in ' + guessesTaken + ' tries!')

if guess != number:
	number = str(number)
	print('Sorry, you lost. The number I was thinking of was ' + number)