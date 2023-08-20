import random

words = ["Python", "JavaScript", "Network", "Computer", "Programming", "Website", 
"Mathematics", "Science", "Operating", "System", "DataBase", "Object", "Oriented"]

name = input("What is your name ?: ")
print("Good Luck!!!", name)

word = random.choice(words)
guesses = ""

print("The selected word has", len(word), "characters.")

# number of turns
turns = 12
while turns > 0:
    # count the number of times a user fails
    failed = 0

    for char in word:
        if char.lower() in guesses.lower():
            print(char, end='')
        else:
            print("_", end='')
            # every failure 1 will be incremented in failure
            failed += 1
    print()
    
    if failed == 0:
        print("You win!!!")
        print("The word is", word)
        break
    
    guess = input("Guess a character: ")
    while len(guess) > len(word):
        guess = input(f"Maximum {len(word)} characters, Please re-enter:")
    while len(guess) == 0:
        guess = input("Minimum 1 character, please re-enter: ")
    guesses += guess

    if guess.lower() not in word.lower():
        turns -= 1
        print("Wrong!!!")
        print("You have", turns, "more guess!")

        if turns == 0:
            print("You Loose.")

