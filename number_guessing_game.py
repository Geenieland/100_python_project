< Angela version >

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#(3번째작업) Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """!!! checks answer against guess. returns the number of turns remaining. !!!"""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns -1
  else:
    print("You got it! The answer was {answer}.")


#(4번째작업) Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    
  

    
def game():
  print(logo)
    
  #(1번째작업)Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  print(f"Pssst, the corrent answer is {answer}")
  
  turns = set_difficulty()
  
  
  #(5번째작업) Repeat the guessing functionality if they get if wrong.
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
  
  #(2번째작업) Let the user guess a number.
    guess =  int(input("Make a guess:"))
    
    
# (6번째작업) Track the number of turns and reduce by 1 if they get it wrong. 
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()







< Dongwoon version >


from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100 ")

game_mode = imput("Choose a difficulty. Type 'easy' or Type 'hard': ")

list_of_numb = list(range(1, 101))
think_num = random.choice(list_of_number)


def easy_mode():
	game_finish = False
	count = 10
	
	while not game_finish:
		geuss_num = int(input("make a guess: ")
		if count < 1:
			game_finish = True
		if guess_num > think_num:
			count -= 1
			print("Too high")
			print("Guess again")
			print(f"You have {count} attempts remaining to guess. ")
		elif guess_num < think_num:
			count -= 1
			print("Too high")
			print("Guess again")
			print(f"You have {count} attempts remaning to guess. ")
		elif count == 1 and guess_num > think_num:
			game_finish = True
			print("Too high")
			print("You've run out of guess, you lose. ")
		elif count == 1 and guess_num < think_num:
			print("Too low")
			print("You've run out fo guess, you lose. ")
		elif guess_num = think_num:
			print(f"You got it! the answer was {guess_num}. ")


def hard_mode():
	game_finish = False
	count = 5
	
	while not game_finish:
		geuss_num = int(input("make a guess: ")
		if count < 1:
			game_finish = True
		if guess_num > think_num:
			count -= 1
			print("Too high")
			print("Guess again")
			print(f"You have {count} attempts remaining to guess. ")
		elif guess_num < think_num:
			count -= 1
			print("Too high")
			print("Guess again")
			print(f"You have {count} attempts remaning to guess. ")
		elif count == 1 and guess_num > think_num:
			game_finish = True
			print("Too high")
			print("You've run out of guess, you lose. ")
		elif count == 1 and guess_num < think_num:
			print("Too low")
			print("You've run out fo guess, you lose. ")
		elif guess_num = think_num:
			print(f"You got it! the answer was {guess_num}. ")


if game_mode == "easy":
	print("YOu have 10 attempts remaining to guess the number. ")
	easy_mode()
if game_mode == "hard":
	print("You have 5 attempts remaining to guess the number. ")
	hard_mode()
