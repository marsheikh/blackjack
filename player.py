from deck import Deck

class Player:
    def __init__(self, player_type):
        self.current_score = 0
        self.hand = []
        self.play = ""
        self.type = player_type

    def hit(self, deck):
        card = deck.draw_card()
        self.current_score += card.points
        self.hand.append(card)

    def set_up_hands(self, deck):
        for i in range(2):
            self.hit(deck)

    def print_hand(self):
        number_of_cards = len(self.hand)
        
        for i in range(number_of_cards):
            print("+---+ ", end="")
 
        print()
        for i in range(number_of_cards):
            card = self.hand[i]
            print("|{}  | ".format(card.suit), end="")
 
        print()
        for i in range(number_of_cards):
            card = self.hand[i]
            print("| {} | ".format(card.name), end="")
 
        print()
        for i in range(number_of_cards):
            card = self.hand[i]
            print("|  {}| ".format(card.suit), end="")
 
        print()    
        for i in range(number_of_cards):
            print("+---+ ", end="")
 