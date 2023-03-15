# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


DECK = ['A♥','K♥','Q♥','J♥','10♥','9♥','8♥','7♥','6♥','5♥','4♥','3♥','2♥',
        'A♠','K♠','Q♠','J♠','10♠','9♠','8♠','7♠','6♠','5♠','4♠','3♠','2♠',
        'A♦','K♦','Q♦','J♦','10♦','9♦','8♦','7♦','6♦','5♦','4♦','3♦','2♦',
        'A♣','K♣','Q♣','J♣','10♣','9♣','8♣','7♣','6♣','5♣','4♣','3♣','2♣']

random.shuffle(DECK)

def computer_cards():
    computer_cards = DECK[0:5]
    print(computer_cards)
    return computer_cards
   
def person_cards():
    person_cards = DECK[5:10]
    print(person_cards)
    return person_cards
    
comp_card = computer_cards()

pers_card = person_cards()
 
card_number = [i[0]for i in comp_card]   
card_symbol = [i[-1]for i in comp_card]


def check(data, symbol):
    """
    computer discards cards, if he has same cards 
    he will leave them and change others to try to get 
    something better, if he has no pairs he will leave 
    one color where he has most cards to try to get flush
    """
    remove_hand = []
    for i in data:
        if data.count(i) < 2:
            ind = data.index(i)
            remove_hand.append(comp_card[ind])
    for card in remove_hand:
        comp_card.remove(card)
        
    if len(comp_card) == 0:
        suit_hand = []
        set_suit = set(symbol)
        most_common = None
        qty_most_common = 0
        for i in set_suit:
            qty = symbol.count(i)
            if qty > qty_most_common:
                qty_most_common = qty
                most_common = i
        for x, element in enumerate(symbol):
            if element == most_common:
                suit_hand.append(DECK[x])
                
        if len(suit_hand) < 3:
            print(len(suit_hand))
            if 'A' in data:
                ind = data.index('A')
                
                comp_card.append(DECK[ind])
                
            if 'K' in data:
                ind2 = data.index('K') 
                comp_card.append(DECK[ind2])  
            
        else:
            comp_card.append(suit_hand)
    print(comp_card)
 
new_list = check(card_number, card_symbol)   

#my_suit_list = [i[:-1]for i in comp_card]
#print(my_suit_list)


"""
def winning_evaluation(hand, symbol):
    
    Go trought all combination to evaluate winner in playing hand
   
    if card_number = ['A','K','O','J','1'] and symbol.count
    """