# lists 
points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
shorthand_names = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ["SPADES", "DIAMONDS", "HEARTS", "CLUBS"]
suit_icons = ["♣", "♠", "♦", "♥"]

# dictionaries
names_to_shorthand = dict(zip(names, shorthand_names))

suits_to_icons = dict(zip(suits, suit_icons))

points_per_name = dict(zip(names, points))


# general value constants 

max_score = 21

house = "HOUSE"

player = "PLAYER"