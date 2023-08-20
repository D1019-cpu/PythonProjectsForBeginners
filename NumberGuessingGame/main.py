import random
import math


# taking inputs
# and handling when lower greater than upper
while True:
    lower = int(input("Enter lower bound:-"))
    upper = int(input("Enter upper bound:-"))
    if lower < upper and lower >= 0 and upper >= 0: break
    else:
        print("Lower must be less than Upper and lower, upper are greater than or equal to 0!!!")

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

    # condition testing
    if x == guess:
        print("Congratulations you did it in", count, "try.")
        break
    elif x > guess:
        print("You guessed too small!")
    else:
        print("You guessed too high!")
    

    if count >= maximum_number_guess:
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next Time!")

    