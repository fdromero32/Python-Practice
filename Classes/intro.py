class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(type(facade_1_type))

#Class Variables
class Grade:
  minimum_passing = 65

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

class Circle:
  pi = 3.14

  def __init__(self, diameter):
    print(f'New Circle with diameter: {diameter}')

  def area(self, radius):
    return self.pi * radius ** 2

teaching_table = Circle(36)

# pizza_area = circle.area(6)
# teaching_table_area = circle.area(18)
# round_room_area = circle.area(5730)

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ice"

#Attribute Functions
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# Self
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
  
  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# Everything is an object!
number = 5
dir(number)

def this_function_is_an_object():
  return 'This bussy'

# print(dir(this_function_is_an_object))

# String Representation:
  def __repr__(self):
    return (f'Circle with radius {self.radius}')

# Review:
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade) 

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)
pieter.add_grade(Grade(100))
