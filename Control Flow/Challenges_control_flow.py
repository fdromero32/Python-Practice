# Challenge #1:
def large_power(base, exponent):
  if (base ** exponent) > 5000:
    return True
  else:
    return False

# print(large_power(2, 13))
# print(large_power(2, 12))


# Challenge #2:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < (food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False

# print(over_budget(100, 20, 30, 10, 40))
# print(over_budget(10, 5, 5, 10, 10))

def twice_as_large(num1, num2):
  if num1 > (num2 * 2):
    return True
  else:
    return False
print(twice_as_large(10, 5))
print(twice_as_large(11, 5))

def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

print(divisible_by_ten(20))
print(divisible_by_ten(25))


def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False

print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5,5))

#Article #2
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False

print(in_range(10, 10, 10))
print(in_range(5, 10, 20))

#Same Name
def same_name(your_name, my_name):
  if str(your_name) == str(my_name):
    return True
  else:
    return False

print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))

# Always False
def always_false(num):
  if num <= 0 or num >= 0:
    return False
  else:
    return False

print(always_false(0))
print(always_false(-1))
print(always_false(1))

# Movie Review
def movie_rating(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  elif rating >= 9:
    return "Outstanding!"
  else:
    return "Please input a valid rating"

print(movie_review(9))
print(movie_review(4))
print(movie_review(6))

# Def Max Number
def max_num(x,y,z):
  if x > y and x > z:
    return x
  elif y > z and y > x:
    return y
  elif x == y or x == z or y == z:
    return "It's a tie!"
  else:
    return z

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))