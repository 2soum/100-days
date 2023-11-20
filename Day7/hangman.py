#Step 1
import random
print("Welcome to the Hangman Game")
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
replace_word = len(chosen_word) * "_"
print(chosen_word)
print(replace_word)
end = False
lives = 5
while not end:
    print("You have " + str(lives) +" lives")
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print("Right")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                replace_word = replace_word[:i] + guess + replace_word[i+1:]
        print(replace_word)
        if replace_word == chosen_word:
            end = True
            print("You won")
    else:
        print("Wrong")
        lives -= 1
