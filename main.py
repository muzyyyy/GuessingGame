import random

number = random.randint(1, 10)

playerName = input("Hello Whats your name? ")
numberOfGuesses = 0
print('Hello! '+ playerName + ', I am guessing a number between 1 to 10')

#The loop
while numberOfGuesses < 5 :
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