import random

number = random.randint(1, 20)

playerName = input("Hello Whats your name? ")
numberOfGuesses = 0
print('Hello! ' + playerName +', I will be generating a number between 1-20 and you will be given 10 tries to guess the number!')

#The loop
while numberOfGuesses < 10 :
    print('Guess the number')
    guess = int(input())
    numberOfGuesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your number is too high')
    if guess == number:
        print('GREAT!! You did it')
        print('You took ' + str(numberOfGuesses) + ' tries!' )
        break

#Lose statement
else:
    print('You did not guess the number, The number was ' + str(number))