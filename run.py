# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random



DECK = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥',
        '3♥', '2♥', 'A♠', 'K♠', 'Q♠', 'J♠', '10♠', '9♠', '8♠', '7♠', '6♠',
        '5♠', '4♠', '3♠', '2♠', 'A♦', 'K♦', 'Q♦', 'J♦', '10♦', '9♦', '8♦',
        '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣',
        '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']

scale_list = ['A', 'K', 'Q', 'J', '1', '9', '8', '7',
              '6', '5', '4', '3', '2', 'A']

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
    
    c_num = [i[0]for i in player]   
    c_sym = [i[-1]for i in player]
    points = 0
    
    def s_scales(syms):
        """
        Looks for colors in delt cards
        """
        qty = 0
        for x in syms:
            qty = syms.count(x)
            if qty == 5:          
                return True
            else:
                return False
        
    scale_syms = s_scales(c_sym)
    
    # high cards
    if len(list(set(c_num))) == 5:
        for x in c_num:
            if 'A' in c_num:
                points = 14
            elif 'K' in c_num:
                points = 13
            elif 'Q' in c_num:
                points = 12
            elif 'J' in c_num:
                points = 11
            elif '1' in c_num:
                points = 10
            else:
                points = int(x)
    
    # pairs
    if len([x for n, x in enumerate(c_num) if x in c_num[:n]]) == 1:
        duplicates = [x for n, x in enumerate(c_num) if x in c_num[:n]]
        for x in duplicates:
            if x == 'A':
                points = 27
            elif x == 'K':
                points = 26
            elif x == 'Q':
                points = 25
            elif x == 'J':
                points = 24
            elif x == '1':
                points = 23
            else:
                points = int(x)+13
    # two pairs and tree of a kind
    if len([x for n, x in enumerate(c_num) if x in c_num[:n]]) == 2:
        dubles = [x for n, x in enumerate(c_num) if x in c_num[:n]]
        numbers = sorted([i for i in dubles if str(i).isdigit()], reverse=True)
        # two pairs
        if dubles[0] != dubles[1]:
            if 'A' in dubles:
                points = 40 
            elif 'K' in dubles:
                points = 39
            elif 'Q' in dubles:
                points = 38
            elif 'J' in dubles:
                points = 37
            elif '1' in dubles:
                points = 36 
            else:
                points = int(numbers[0]) + 26
        # tree of a kind
        if dubles[0] == dubles[1]: 
            if 'A' in dubles:
                points = 53   
            elif 'K' in dubles:
                points = 52
            elif 'Q' in dubles:
                points = 51
            elif 'J' in dubles:
                points = 50
            elif '1' in dubles:
                points = 49
            else:
                points = int(numbers[0]) + 39
    # full house
    if len([x for n, x in enumerate(c_num) if x in c_num[:n]]) == 3:
        dubles = [x for n, x in enumerate(c_num) if x in c_num[:n]]
        numbers = sorted([i for i in dubles if str(i).isdigit()], reverse=True)
        print(len(dubles))
        if not any(x == y for x in dubles for y in dubles if x != y):
            if dubles.count('A') == 2:
                points = 88 
            elif dubles.count('K') == 2:
                points = 87
            elif dubles.count('Q') == 2:
                points = 86
            elif dubles.count('J') == 2:
                points = 85
            elif dubles.count('1') == 2:
                points = 84
            elif len(set(dubles)) == 2:
                points = int(numbers[0]) + 76
    # poker
    for x in c_num:
        qty = c_num.count(x)
        if qty == 4:
            if 'A' in dubles:
                points = 101
            elif 'K' in dubles:
                points = 100
            elif 'Q' in dubles:
                points = 99
            elif 'J' in dubles:
                points = 98
            elif '1' in dubles:
                points = 97
            else:
                points = int(numbers[0]) + 87
    # flush/color
    if scale_syms is True:
        numbers = sorted([i for i in c_num if str(i).isdigit()], reverse=True)
        if 'A' in c_num:
            points = 77   
        elif 'K' in c_num:
            points = 76
        elif 'Q' in c_num:
            points = 75
        elif 'J' in c_num:
            points = 74
        elif '1' in c_num:
            points = 73
        else:
            points = int(numbers[0]) + 63
    # scales
    for x in range(len(scale_list)-4):
        five_cards = scale_list[x:x+5]
        x += 0
        numbers = sorted([i for i in c_num if str(i).isdigit()], reverse=True)
        no_dubles = list(dict.fromkeys(c_num))
        if len([x for x in five_cards + no_dubles if x in five_cards])==10:
            if five_cards[0] == '1':
                points = 60
            elif five_cards[0] == 'J':
                points = 61
            elif five_cards[0] == 'Q':
                points = 62
            elif five_cards[0] == 'K':
                points = 63
            elif five_cards[0] == 'A':
                points = 64 
            else:
                points = int(five_cards[0]) + 52
        # street flush and Royal Flush, scales with same color
            if scale_syms is True:
                if 'A' in c_num:
                    points = 110
                elif 'K' in c_num:
                    points = 109
                elif 'Q' in c_num:
                    points = 108
                elif 'J' in c_num:
                    points = 107
                elif '1' in c_num:
                    points = 106
                else:
                    points = int(c_num[0]) + 96
    return points


points_c = winning_evaluation(comp_card)
points_p = winning_evaluation(pers_card)
print(f'Computer got {points_c} points')
print(f'You got {points_p} points')