def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"

# Enter a user name here, make sure to make it a string
user_name = "Becky"

print(dave_check(user_name))

def greater_than(x, y):
  if x > y:
    return x
  elif y > x:
    return y
  else:
    return "These numbers are the same"

def graduation_reqs(gpa, credits):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"
  elif gpa >= 2.0 and not credits >=120:
    return "You do not have enough credits to graduate."
  elif credits >=120 and not gpa >=2.0:
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet either requirement to graduate!"

print(graduation_reqs(0.0, 0.0))

def graduation_mailer(gpa, credits):
  if credits >= 120 or gpa >= 2.0:
    return True

def grade_converter(grade):
  if grade >= 4.0:
    return "A"
  elif grade >= 3.0:
    return "B"
  elif grade >=2.0:
    return "C"
  elif grade >= 1.0:
    return "D"
  elif grade >= 0.0:
    return "F"

def raises_value_error():
  raise ValueError
  
try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")

def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."