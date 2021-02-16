import card
from player import Player
from constants import house, player
from deck import Deck
import os

# os.system("clear")

def print_intro():
    # print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    # print("Welcome to Swyft Blackjack")
    # print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("Welcome to:")
    print("""
    
.------..------..------..------..------.     .------..------..------..------..------..------..------..------..------.
|S.--. ||W.--. ||Y.--. ||F.--. ||T.--. |.-.  |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :/\: || :/\: || (\/) || :(): || :/\: ((5)) | :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| :\/: || :\/: || :\/: || ()() || (__) |'-.-.| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'S|| '--'W|| '--'Y|| '--'F|| '--'T| ((1)) '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'`------'`------'`------'`------'`------'
""")                                                                                                                                                                

def main():    

    dealer, player_1, deck = new_game()

    while True:

        while(player_1.play != "S"):

            player_1.play = input("\n(H)it or (S)tay?\n").upper()

            if (player_1.play == "H"):
                player_1.hit(deck)
                print_hands(dealer, player_1)

            elif (player_1.play == "S"):
                if player_1.current_score > dealer.current_score:
                    print("YOU WIN.")
                    print("WE'LL SEE YOU OUT BACK.")
                    # wanted to create a general calculate winner method 
                    # had to ignore DRY this time https://imgur.com/9wSmA8G
                    another_round = input("\nPress ENTER for another round\n")
                    dealer, player_1, deck = new_game()

            

            if player_1.current_score > 21:
                print("YOU LOSE.")
                print("HOUSE WINS. THE HOUSE ALWAYS WINS.")

                another_round = input("\nPress ENTER for another round\n")
                dealer, player_1, deck = new_game()
                continue



def new_game():
    print_intro()
    dealer = Player(house)
    player_1 = Player(player)

    deck = Deck.load()

    # set up each hand 

    dealer.set_up_hands(deck)
    player_1.set_up_hands(deck)

    print_hands(dealer, player_1)

    return dealer, player_1, deck

def print_hands(dealer, player_1):
    # if i had more time, i'd make this look prettier and avoid having to pass dealer and player

    # print(""" 
    # _   _   _   _   _   _  
    # / \ / \ / \ / \ / \ / \ 
    # ( D | e | a | l | e | r )
    # \_/ \_/ \_/ \_/ \_/ \_/ 
    # """)

    print("-----Dealer-----")
    dealer.print_hand()
    print(f"House Score: {dealer.current_score}")

    print("-----Player 1-----")
    player_1.print_hand()
    print(f"Player Score: {player_1.current_score}")



if __name__ == "__main__":
    main()