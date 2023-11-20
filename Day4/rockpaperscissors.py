import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
end = False
while not end:
    userChoice = int(input("What do you choice ? Type 0 for rock, 1 for paper, 2 for scissors."))
    if userChoice >= 3 or userChoice < 0:
        print("You typed an invalid number, you lose!")

    print("You choosed ")
    print(choices[userChoice])
    AIchoice = random.randint(0, 2)
    print("AI choosed\n" + choices[AIchoice])

    if userChoice == 0 and AIchoice == 2:
        print("You win!")
        end = True
    elif AIchoice == 0 and userChoice == 2:
        print("You lose")
        end = True
    elif AIchoice > userChoice:
        print("You lose")
        end = True

    elif userChoice > AIchoice:
        print("You win!")
        end = True
    elif AIchoice == userChoice:
        print("It's a draw")
##
