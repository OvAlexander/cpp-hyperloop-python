# Created by Yash Karwal
# Import random lib
import random
# Generate random integer
num = random.randint(1,100)
# Loop declaration
play = True
while play:                                 # Loop as long as play is true
    guess = int(input())                    # Take in user input as guess
    if guess == num:                        # Check if guess is equal to random number if so let user know and end loop
        print("The guess is correct!")
        play = False
    elif guess > num:                       # Check if guess is greater than random number if so let user know
        print("The guess is too high >:(")
    else:                                   # Check if guess is less than random number if so let user know
        print("The guess is too low >:(")
print("XD")