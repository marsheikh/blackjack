import requests 
from constants import points_per_name, max_score

class Card: 
    def __init__(self, deck_id, name, points, suit):
        self.deck_id = deck_id 
        self.name = name
        self.points = points
        self.suit = suit
    
    @staticmethod
    def calculate_points(current_score, name):
        if name != "ACE":
            points = points_per_name[name]
        else: 
            if current_score >= 11:
                points = 1
            else:
                points = 11
        
        return points
    
    def print_card(self):
    # print a pretty card with the suit and name
        print("+---+")
        print(f"|{self.suit}  |")
        print(f"| {self.name} |")
        print(f"|  {self.suit}|")
        print("+---+")




