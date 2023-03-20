# PROJECT : GUESS THE NUMBER

from art import logo
import random
"Make logo and explain the game"
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
"Mode choice"
game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
"Make number of list"
list_of_number = list(range(1, 101))
# print(list_of_number)
think_number = random.choice(list_of_number)
# print(think_number)


def easy_mode():

  game_finish = False
  count = 10

  while not game_finish:

    guess_number = int(input("make a guess: "))

    if count < 1:
      game_finish = True

    if guess_number > think_number:
      count -= 1
      print("Too high")
      print("Guess again")
      print(f"You have {count} attempts remaining to guess the number.")

    elif guess_number < think_number:
      count -= 1
      print("Too low")
      print("Guess again")
      print(f"You have {count} attempts remaining to guess the number.")

    elif count == 1 and guess_number > think_number:
      game_finish = True
      print("Too high")
      print("You've run out of guesses, you lose.")

    elif count == 1 and guess_number < think_number:
      game_finish = True
      print("Too low")
      print("You've run out of guesses, you lose.")

    elif guess_number == think_number:

      print(f"You got it! The answer was {guess_number}. ")
      game_finish = True


def hard_mode():

  game_finish = False
  count = 5

  while not game_finish:

    guess_number = int(input("make a guess: "))

    if count < 1:
      game_finish = True

    if guess_number > think_number and count > 1:
      count -= 1
      print("Too high")
      print("Guess again")
      print(f"You have {count} attempts remaining to guess the number.")

    elif guess_number < think_number and count > 1:
      count -= 1
      print("Too low")
      print("Guess again")
      print(f"You have {count} attempts remaining to guess the number.")

    elif count == 1 and guess_number > think_number:
      game_finish = True
      print("Too high")
      print("You've run out of guesses, you lose.")

    elif count == 1 and guess_number < think_number:
      game_finish = True
      print("Too low")
      print("You've run out of guesses, you lose.")

    elif guess_number == think_number:

      print(f"You got it! The answer was {guess_number}. ")
      game_finish = True


if game_mode == "easy":
  print("You have 10 attempts remaining to guess the number. ")
  easy_mode()

if game_mode == "hard":
  print("You have 5 attempts remaining to guess the number. ")
  hard_mode()
