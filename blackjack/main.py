import random
from art import logo
from replit import clear

def deal_card():
  """Gives cards to user and computer"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
  
def calculate_score(cards):
  """Takes a list of cards and returns score calculated from cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(user_score,computer_score):
  if user_score==computer_score:
    return "draw🥺"
  elif user_score==0:
    return "You win with a blacjack😍"
  elif computer_score==0:
    return "You lose opponent has a blackjack😬"
  elif user_score>21:
    return "You went over,you lose"
  elif computer_score > 21:
    return "You win, opponent went over😣"
  elif user_score>computer_score:
    return  "You win😎"
  else:
    return "You lose"

def play_game(): 
  print(logo)  
  user_cards=[]
  computer_cards=[]
  is_game_over=False

  #Giving user and computer 2 cards each
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    
    print(f"Your cards are: {user_cards} and current score is: {user_score}")
    print (f"Computers first card is: {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True

    else:
      user_should_deal=input("Type 'y' to get another card, type 'n' to pass.")
      if user_should_deal=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True

  while computer_score !=0 and  computer_score < 17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(f"Your final hand is: {user_cards} and final score is: {user_score}.")
  print(f"Computer final hand is: {computer_cards} and computers final socre is: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play another game of blackjack? type 'y' if yes or 'n' if no: ")=='y':
  clear()
  play_game()