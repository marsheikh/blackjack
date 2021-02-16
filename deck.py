import card 
import requests 

class Deck:
    def __init__(self, deck_id, remaining_cards):
        self.deck_id = deck_id
        self.remaining_cards = remaining_cards

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
            points = calculate_points(drawn_card["value"])
            new_card = card.Card(   self.deck_id,
                                    drawn_card["value"],
                                    points,
                                    drawn_card["suit"])

        except Exception as err: 
            print(f"Error drawing card: {err}")

deck = Deck.load()

print(deck.deck_id, deck.remaining_cards)