# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


DECK = ['A♥️','K♥️','Q♥️','J♥️','10♥️','9♥️','8♥️','7♥️','6♥️','5♥️','4♥️','3♥️','2♥️',
        'A♠','K♠','Q♠','J♠','10♠','9♠','8♠','7♠','6♠','5♠','4♠','3♠','2♠',
        'A♦️','K♦️','Q♦️','J♦️','10♦️','9♦️','8♦️','7♦️','6♦️','5♦️','4♦️','3♦️','2♦️',
        'A♣️','K♣️','Q♣️','J♣️','10♣️','9♣️','8♣️','7♣️','6♣️','5♣️','4♣️','3♣️','2♣️']

random.shuffle(DECK)

def deal_cards():
    print(DECK)
    computer_cards = DECK[0:5]
    player_cards = DECK[5:10]
    print(computer_cards)
    print(player_cards)
    
deal_cards() 