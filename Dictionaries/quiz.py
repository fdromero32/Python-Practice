combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
# print(combo_meals[2])

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print("the peacemaker" in inventory)
# Checks for existence of "the peacemaker as a key in the dictionary"

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
# print(combo_meals[3])

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars:
  print(element)

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory)
# Prints false because it checks for 12 as a key and it is a value.

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

raffle.pop(561721, "No Value")
print(raffle)