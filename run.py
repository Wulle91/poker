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
    #here cod is looking if there is a card without pair and removes it itf does
    remove_hand = []
    for i in data:
        if data.count(i) < 2:
            ind = data.index(i)
            remove_hand.append(comp_card[ind])
    for card in remove_hand:
        comp_card.remove(card)
    #if there are no pairs, code leaves the same colors    
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
    # if there are less than three colors, coputer leaves high cards            
        if len(suit_hand) < 3:
            high_list = ['A','K','Q','J','1','9']
            for x in data:
                if x in high_list:
                    ind = data.index(x)
                    comp_card.append(DECK[ind])  
        else:
            for x in suit_hand:
                comp_card.append(x)
    # if PC has just one hight card or just tri color he will iterate to search flusch
        if len(comp_card) == 1 or len(suit_hand) < 3:
            scale_list = ['A','K','Q','J','1','9','8','7','6','5','4','3','2','A']
            scale_hand = DECK[0:5]
            rest = []
            for x in range(len(scale_list)-2):
                five_cards = scale_list[x:x+5]
                x += 0
                res = [x for x in five_cards + data if x not in five_cards]

                if len(res) < 2:
                    rest.append(res[0])
            if five_cards == scale_hand:
                comp_card.clear()
                for x in scale_hand:
                    comp_card.append(x)
            if 5-len(rest) <= 4:
                ind = data.index(rest[0])
                scale_hand.remove(DECK[ind])
                comp_card.clear()
                for x in scale_hand:
                    comp_card.append(x)
    print(comp_card,'this')
 
new_list = check(card_number, card_symbol)   

#my_suit_list = [i[:-1]for i in comp_card]
#print(my_suit_list)


"""
def winning_evaluation(hand, symbol):
    
    Go trought all combination to evaluate winner in playing hand
   
    if card_number = ['A','K','O','J','1'] and symbol.count
    """
    