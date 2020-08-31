class HoldsFive:
  five = 5
  
five_holder = HoldsFive()

print(hasattr(five_holder, 'five'))

class User:
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "Hiya {}!".format(self.name)
  
devorah = User("Devorah")
print(devorah)