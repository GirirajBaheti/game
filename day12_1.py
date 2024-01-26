# print("WELCOME TO THE NUMBER GUESSING GAME ")
# print("I am thinking of a no b/w 1 to 100")
# import random
# answer=random.randint(1,101)
# type=input("Type difficulty level : 'Easy' or 'Hard'\n")
# if type=="Easy":
#     print("You have total 10 attempts to guess the number")
# elif type=="Hard":
#     print("You have 5 attempts to guess the number")
# else:
#     print("You choose an invalid type of string please play again")

# def user_guess():
#     for new_user_guess in num():
#       user_guess=input("Make a guess:\n")
#       if user_guess>num:
#          print("Too high")
#       elif user_guess<num:
#         print("Too low")
#       elif user_guess==num:
#         print("You guessd the right number")

# while 
import random 

EASY_LEVEL_TUEN=10
HAED_LEVEL_TURN=5

def check_answer(guess,answer,turns):
     if guess>answer:
          print("Too high")
          return turns -1
     elif guess<answer:
          print("Too low")
          return turns -1
     else:
          print(f"You guessd the right number , The answer was {answer}")

def set_difficulty():
      level=input("Type difficulty level : 'easy' or 'hard'\n")
      if level=="easy":
           return EASY_LEVEL_TUEN
      else:
           return HAED_LEVEL_TURN

def game():
  print("WELCOME TO THE NUMBER GUESSING GAME ")
  print("I am thinking of a no b/w 1 to 100")
  answer=random.randint(1,101)
  turns=set_difficulty()
#   print(f"You have {turns} attempt ")
  guess=0
  while guess!=answer:
   print(f"You have {turns} attempt ")
   guess=int(input("Make a guess"))
   turns=check_answer(guess,answer,turns)
   if turns==0:  
     print("You have run out of guess you lose")
     return
   elif guess!=answer:
       print("Guess again")
   
  
   

game()