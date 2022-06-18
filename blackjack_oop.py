import random
from xml.dom import INDEX_SIZE_ERR

x = 0
cards = {"card": ['♣1', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣11', '♣12', '♣13', '♦1', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦11', '♦12', '♦13', '♥1', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥11', '♥12', '♥13', '1♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', '11♠', '12♠', '13♠'], 'value': [x, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, x, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, x, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, x, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]}

player_cards = []
dealer_hidden = []
dealer_showing = []
account_value = 100
player_value = 0
dealer_value = 0
dealt_card = ''
dealt_card_value = 0
current_bet = 0
player_cash = 100
idx = 0

print("""
Have a seat. You have purchased $100 in chips.  Good luck!""")

class Cards:
    global dealt_card, dealt_card_value, player_value, dealer_value, current_bet, player_cash, account_value, idx
    def __init__(self):
        self.dealt_card = (random.choice(cards['card']))
        self.idx = cards['card'].index(self.dealt_card)
        self.dealt_card_value = cards['value'][self.idx]
        

def player_begin():
    global dealt_card, dealt_card_value, player_value, dealer_value, current_bet, player_cash, account_value, idx
    player_value = 0
    dealer_value = 0
    player_cards = []
    dealer_hidden = []
    dealer_showing = []

    bet_allowed = False
    while bet_allowed == False:
        current_bet = int(input("Type in the value of your bet: "))
        if current_bet > player_cash:
            print("You don't have enough chips.  Enter a smaller bet.")
        else:
            bet_allowed = True
    
    player_card_1 = Cards()
    print(player_card_1.dealt_card)

    player_cards.append(dealt_card)
    if dealt_card_value == x:
        if player_value < 11:
            player_value += 11
        else:
            player_value += 1
    else:
        player_value += dealt_card_value
    Cards()
    player_cards.append(dealt_card)
    if dealt_card_value == x:
        if player_value < 11:
            player_value += 11
        else:
            player_value += 1
    else:
        player_value += dealt_card_value
    Cards()
    dealer_hidden.append(dealt_card)
    if dealt_card_value == x:
        if dealer_value < 11:
            dealer_value += 11
        else:
            dealer_value += 1
    else:
        dealer_value += dealt_card_value
    Cards()
    dealer_showing.append(dealt_card)
    if dealt_card_value == x:
        if dealer_value < 11:
            dealer_value += 11
        else:
            dealer_value += 1
    else:
        dealer_value += dealt_card_value

    print(f"""
Account Value: ${account_value}""")
    print(f"Player cards: {player_cards} - Player has: {player_value}")
    print(f"Dealer showing: {dealer_showing}")
    if player_value == 21:
        print("Blackjack! You win!")
        account_value += current_bet
        play_again()
    elif player_value < 21 and dealer_value == 21:
        print("Dealer has blackjack.  You lose.")
        account_value -= current_bet
        play_again()
    else:
        choice()


def choice():

    global dealt_card, dealt_card_value, player_value, dealer_value, current_bet, player_cash, account_value
    choice = input(
        "What do you want to do? Type: 'Hit', 'Stay', or 'Double' ").lower()
    if choice == 'hit':
        Cards()
        print(f"Player gets a {dealt_card}.")
        player_cards.append(dealt_card)
        if dealt_card_value == x:
            if player_value < 11:
                player_value += 11
            else:
                player_value += 1
        else:
            player_value += dealt_card_value

        if player_value == 21:
            print("Player stays with 21.")
        elif player_value < 21:
            print(f"Player has {player_value}.")
            choice()
        elif player_value > 21:
            print("Bust. You lose.")
            account_value -= current_bet
            play_again()

    elif choice == 'stay':
        print(f"Player stays with {player_value}.")
        dealer_turn()

    elif choice == 'double':
        current_bet *= 2
        Cards()
        player_cards.append(dealt_card)
        if dealt_card_value == x:
            if player_value < 11:
                player_value += 11
            else:
                player_value += 1
        else:
            player_value += dealt_card_value

        if player_value > 21:
            print("Player busts.  You lose.")
            account_value -= current_bet
            play_again()
        else:
            print(f"Player stays with {player_value}.")
            dealer_turn()


def play_again():

    global dealt_card, dealt_card_value, player_value, dealer_value, current_bet, player_cash, account_value
    print(f"Player has ${account_value}. ")
    again = input(
        "Play again? Type 'yes' to play again or 'no' to leave the table.").lower()
    if again == 'yes':
        player_begin()
    else:
        print("See ya. May the odds always be in your favor.")


def check_status():
    global dealt_card, dealt_card_value, player_value, dealer_value, current_bet, player_cash, account_value
    if player_value == 21:
        print("Player stays with 21.")
        account_value += current_bet
        play_again()
    elif player_value < 21:
        print(f"Player has {player_value}.")
        choice()
    elif player_value > 21:
        print("Bust. You lose.")
        account_value -= current_bet
        play_again()


def dealer_turn():
    global dealt_card, dealt_card_value, player_value, dealer_value, current_bet, player_cash, account_value
    dealer_done = False
    while dealer_done == False:
        print(f"Dealer has {dealer_value}.")
        if dealer_value > 16:
            dealer_done = True
            print(f"Dealer stays with {dealer_value}.")
        else:
            Cards()
            dealer_showing.append(dealt_card)
            if dealt_card_value == x:
                if dealer_value < 11:
                    dealer_value += 11
                    print(
                        f"Dealer takes a card. Dealer gets an ace. Dealer has {dealer_value}.")
                else:
                    dealer_value += 1
                    print(
                        f"Dealer takes a card. Dealer gets an ace. Dealer has {dealer_value}.")
            else:
                dealer_value += dealt_card_value
                print(
                    f"Dealer takes a card. Dealer gets a {dealt_card_value}. Dealer has {dealer_value}.")

        if dealer_value < 17:
            pass
        elif dealer_value > 21:
            print("Dealer busts. You win!")
            account_value += current_bet
            dealer_done = True
            play_again()
        else:

            dealer_done = True
            if player_value > dealer_value:
                print("You win!")
                account_value += current_bet
                play_again()
            elif player_value == dealer_value:
                print("It's a push.")
                play_again()
            else:
                print("You lose!")
                account_value -= current_bet
                play_again()


player_begin()
