import random
import math


# taking inputs
lower = int(input("Enter lower bound:-"))
upper = int(input("Enter upper bound:-"))

# generating random number between the lower and upper
x = random.randint(lower,upper)

print("\n\tYou're only", round(math.log(upper - lower + 1, 2)), "chances to guess the integer!\n")

# initializing the number of guesses
count = 0

maximum_number_guess = math.log(upper - lower + 1, 2)

while count < maximum_number_guess:
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    