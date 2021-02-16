from card import Card
from constants import suits_to_icons, names_to_shorthand
import requests 

class Deck:
    def __init__(self, deck_id, remaining_cards):
        self.deck_id = deck_id
        self.remaining_cards = remaining_cards
        self.shuffle()

    @classmethod
    def load(cls): 
        response = requests.get("https://deckofcardsapi.com/api/deck/new/")
        
        try: 
            response.raise_for_status()
            values = response.json()
            return cls(values["deck_id"], values["remaining"])
        except Exception as err: 
            print(f"Error fetching deck: {err}")

    def shuffle(self):
        response = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/shuffle/")

        try: 
            response.raise_for_status()
        except Exception as err:
            print(f"Error shuffling deck: {err}")
    
    def draw_card(self): 
        #come back here to change count if we want to extend functionality for drawing more cards in the future

        response = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=1")

        try: 
            response.raise_for_status()
            values = response.json()
            self.remaining_cards = values["remaining"]

            list_of_drawn_cards = values["cards"]

            drawn_card = next((card for card in list_of_drawn_cards if card["value"]), None) 
            points = Card.calculate_points(0, drawn_card["value"])
            suit = suits_to_icons[drawn_card["suit"]]

            shorthand_name = names_to_shorthand[drawn_card["value"]]
            new_card = Card(   self.deck_id,
                                    shorthand_name,
                                    points,
                                    suit)
            return new_card
        except Exception as err: 
            print(f"Error drawing card: {err}")
        
        

# deck = Deck.load()
# card = deck.draw_card()    
# print(deck.deck_id, deck.remaining_cards, card.name, card.points)