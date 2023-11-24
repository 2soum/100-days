import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
answer = random.randint(1, 1000)
trysuser = 0


def check(number):
    if number > answer:
        print("Trop grand")
    elif number < answer:
        print("Trop petit")
    else:
        print("Bravo !")
        return True


print("Welcome to the Juste Prix Game")
print("Try to guess the number between 1 and 1000")
print("Choose your difficulty level")
print("1. Easy (10 tries)")
print("2. Hard (5 tries)")
difficulty = input()
if difficulty == "1":
    trysuser = 10
else:
    trysuser = 5
while trysuser > 0:
    trysuser -= 1
    print(answer)
    guess = int(input("Make a guess: "))

    if check(guess):
        break
    print(f"You have {trysuser} tries")
