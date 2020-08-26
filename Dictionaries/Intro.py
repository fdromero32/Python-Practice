# Syntax
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
print(sensors)

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# Incorrect Dictionary
# children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}
# Correct Dictionary => strings/numbers can be keys (immutable), lists cannot
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]}

# Empty Dictionary:
empty_dict = {}

animals_in_zoo ={}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({'theLooper': 138475, 'stringQueen': 85739})

# Updating Dictionary Existing Values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({'Supporting Actress': 'Viola Davis'})
oscar_winners["Best Picture"] = 'Moonlight'

# List Comprehension to Dictionaries
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = {k:v for k, v in zip(drinks, caffeine)}

# Review:
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {k:v for k, v in zip(songs, playcounts)}
plays['Purple Haze'] = 1
plays['Respect'] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
