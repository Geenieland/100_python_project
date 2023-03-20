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

#Write your code below this line 👇


x = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
game_name = ["rock", "paper", "scissors"]

pick = game_name[int(x)]
if pick == "rock":
  print(rock)
elif pick == "paper":
  print(paper)
else:
  print(scissors)

computer_choice = random.choice(game_name)

print("Computer chose:")

if computer_choice == "rock":
  print(rock)
elif computer_choice == "paper":
  print(paper)
else:
  print(scissors)

if pick == computer_choice:
  print("draw")
elif pick == "rock" and computer_choice == "paper": 
  print("You Lose")
elif pick == "paper" and computer_choice == "scissors":
  print("You Lose")
elif pick == "scissors" and computer_choice == "rock":
  print("You Lose") 
else:
  print("You Win")

print("This repl has exited, run again?")



or



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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
