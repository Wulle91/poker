# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random



DECK = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥',
        '3♥', '2♥', 'A♠', 'K♠', 'Q♠', 'J♠', '10♠', '9♠', '8♠', '7♠', '6♠',
        '5♠', '4♠', '3♠', '2♠', 'A♦', 'K♦', 'Q♦', 'J♦', '10♦', '9♦', '8♦',
        '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣',
        '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']

random.shuffle(DECK)


def computer_cards():
    computer_cards = DECK[0:5]
    return computer_cards


def person_cards():
    person_cards = DECK[5:10]
    print("Your cards:")
    print(person_cards)
    return person_cards


comp_card = computer_cards()

pers_card = person_cards()

card_number = [i[0]for i in comp_card]   
card_symbol = [i[-1]for i in comp_card]


def check(data, symbol):
    """
    computer has to discard cards, if he has some pairs, 
    three of a kind or poker he will leave them and change 
    others to try to get something better, if he has no pairs he 
    will leave one color where he has most cards to try to get flush,
    if there are only three colors he will search for 5 straght cards or 
    if there are less tha 4 for straight he will leave all cards over 8, 
    """
    # here cod is looking if there is a card without pair and removes it
    remove_hand = []
    for i in data:
        if data.count(i) < 2:
            ind = data.index(i)
            remove_hand.append(comp_card[ind])
    for card in remove_hand:
        comp_card.remove(card)
    # if there are no pairs, code leaves the same colors    
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
            high_list = ['A', 'K', 'Q', 'J', '1', '9']
            for x in data:
                if x in high_list:
                    ind = data.index(x)
                    comp_card.append(DECK[ind])
        else:
            for x in suit_hand:
                comp_card.append(x)
    # if PC has just one high card or just tree colors he will search flush
        if len(comp_card) == 1 or len(suit_hand) < 3:
            scale_list = ['A', 'K', 'Q', 'J', '1', '9', '8', '7', '6', '5',
                          '4', '3', '2', 'A']
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
            if 5-len(rest) <= 3:
                ind = data.index(rest[0])
                scale_hand.remove(DECK[ind])
                comp_card.clear()
                for x in scale_hand:
                    comp_card.append(x)

    return comp_card


new_list = check(card_number, card_symbol)


def user_input():

    while True:
        print('Enter card numbers you wish to change')
        print("Data should be numbers from 1-5, separated by commas.")
        print("Example: 1, 3, 5\n")

        player_input = input("Enter your data here:\n")

        player_card_index = player_input.split(',')
        player_card_index.sort(reverse=True)

        if validate_user_input(player_card_index):
            for i in player_card_index:               
                del pers_card[int(i)-1]
            comp_add = 5 - len(comp_card)
            new_card_comp = DECK[10:10+int(comp_add)]
            for i in new_card_comp:
                comp_card.append(i)
            pers_add_cards = 5 - len(pers_card)
            pers_add = comp_add + pers_add_cards
            new_card_pers = DECK[10+int(comp_add):10+int(pers_add)]
            for i in new_card_pers:
                pers_card.append(i)
            break
    print(f'Computer cards are: {comp_card}')
    print(f'Your cards are:     {pers_card}')
    

def validate_user_input(values):
    """
    convert strings in integers and valuate if it meet criteria
    we've set for input, raises error if not correct
    """
    try:
        [int(value) for value in values]
        if len(values) > 6:
            raise ValueError(f"You have only 5 cards, you provided {len(values)}")
    except ValueError as e:
        print(f'Invalid data {e} please try again.\n')
        return False
    return True


user_input()


def winning_evaluation(player):
    """
    Go trought all combination to evaluate winner in playing hand
    """
    scale_list = ['A', 'K', 'Q', 'J', '1', '9', '8', '7',
                  '6', '5', '4', '3', '2', 'A']
    c_num = [i[0]for i in player]   
    c_sym = [i[-1]for i in player]
    points = 0
    if c_num == ['A', 'K', 'O', 'J', '1']:
        for x in c_sym:
            if x == x:
                points = 20
    for x in range(len(scale_list)-2):
        five_cards = scale_list[x:x+5]
        x += 0
        if c_num == five_cards:
            points = 190
    for x in range(len(c_num)-1):
        poker = c_num[x:x+4]
        x += 0
        if list(dict.fromkeys(c_num)) == poker:
            points = 180
    if len([x for n, x in enumerate(c_num) if x in c_num[:n]]) == 1:
        duplicates = [x for n, x in enumerate(c_num) if x in c_num[:n]]
        for x in duplicates:
            points = x
            if x == '1':
                points = 10
            if x == 'J':
                points = 11
            if x == 'Q':
                points = 12
            if x == 'K':
                points = 13
            if x == 'A':
                points = 14
    if len([x for n, x in enumerate(c_num) if x in c_num[:n]]) == 2:
        dubles = [x for n, x in enumerate(c_num) if x in c_num[:n]]
        letters = sorted([i for i in dubles if not str(i).isdigit()])
        numbers = sorted([i for i in dubles if str(i).isdigit()], reverse=True)
        sort_dubles = letters + numbers
        if dubles[0] != dubles[1]:

            if sort_dubles[0] == '1':
                points = 23
            elif sort_dubles[0] == 'J':
                points = 24
            elif sort_dubles[0] == 'Q':
                points = 25
            elif sort_dubles[0] == 'K':
                points = 26
            elif sort_dubles[0] == 'A':
                points = 27 
            else:
                points = int(sort_dubles[0]) + 13
        if dubles[0] == dubles[1]:
        
            if sort_dubles[0] == '1':
                points = 36   
            elif sort_dubles[0] == 'J':
                points = 37
            elif sort_dubles[0] == 'Q':
                points = 38
            elif sort_dubles[0] == 'K':
                points = 39
            elif sort_dubles[0] == 'A':
                points = 40
            else:
                points = int(sort_dubles[0]) + 26
    for x in range(len(scale_list)-4):
        five_cards = scale_list[x:x+5]
        x += 0
        hand_without_dubles = list(dict.fromkeys(c_num))
        if len([x for x in five_cards + hand_without_dubles if x in five_cards]) == 10:
            print(five_cards[0])
            if five_cards[0] == '1':
                points = 47
            elif five_cards[0] == 'J':
                points = 48
            elif five_cards[0] == 'Q':
                points = 49
            elif five_cards[0] == 'K':
                points = 50
            elif five_cards[0] == 'A':
                points = 51 
            else:
                points = int(five_cards[0]) + 39
    return points




points_c = winning_evaluation(comp_card)   
points_p = winning_evaluation(pers_card) 
print(f'Computer got {points_c} points')   
print(f'You got {points_p} points')  


