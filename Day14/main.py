import art
import DATA
import random

print(art.logo)
score = 0
print("Welcome to the Higher Lower Game")
winner = True
while winner :
    first = DATA.data[random.randint(0,50)]
    if score != 0:
        first = goodanswer
    second = DATA.data[random.randint(0,50)]
    while first == second:
        second = DATA.data[random.randint(0,50)]

    print(f"Compare A : {first['name']}, a {first['description']}, from {first['country']}")
    print(art.vs)
    print(f"Against B : {second['name']}, a {second['description']}, from {second['country']}")
    if first['follower_count'] > second['follower_count']:
        if input("Who has more followers? Type 'A' or 'B': ") == 'A':
            score += 1
            goodanswer = first

            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            winner = False
    elif first['follower_count'] < second['follower_count']:
        if input("Who has more followers? Type 'A' or 'B': ") == 'B':
            score += 1
            goodanswer = second
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            winner = False


