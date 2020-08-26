dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

# for breed in dog_breeds:
#     # print(breed)

# More examples:
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

# for game in board_games:
#   print(game)

# for sports in sport_games:
#   print(sports)

# Using Range:
promise = "I will not chew gum in class"
# for i in range(5):
#   print(promise)

#Avoiding Infinite Loops:
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for x in students_period_A:
  students_period_B.append(x)
  # print(x)

#Break Functionality:
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dogs in dog_breeds_available_for_adoption:
  # print(dogs)
  if dogs == dog_breed_I_want:
    # print("They have the dog I want!")
    break

# Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for a in ages:
  if a < 21:
    continue
  # print(a)

#While Loops:
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
# print(students_in_poetry)

#Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for i in sales_data:
  for j in i:
    scoops_sold += j

# Nested Loop Syntax
# for i in sales_data:
#   for j in i:
#      print(j)

# List Comprehension:
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [celsius_values * 9/5 + 32 for celsius_values in celsius]

# Review:
single_digits = range(10)
squares = []
for x in single_digits:
  print(x)
  squares.append(x ** 2)

print(squares)

cubes = [single_digit_values ** 3 for single_digit_values in single_digits]
print(cubes)