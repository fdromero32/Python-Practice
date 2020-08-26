def divisible_by_ten(nums):
  counter = 0
  for x in nums:
   if x % 10 == 0:
      counter += 1
  return counter

# print(divisible_by_ten([20, 25, 30, 35, 40]))

def add_greetings(names):
  greeting = []
  for g in names:
    greeting.append(f'Hello, {g}')
  return greeting

# print(add_greetings(["Owen", "Max", "Sophie"]))

def delete_starting_evens(lst):
  while len(lst) >= 1 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(delete_starting_evens([4, 8, 10]))

def odd_indices(lst):
  lst = lst[1::2]
  return lst
  # DIFFICULT DIFFICULT DIFFICULT

# print(odd_indices([4, 3, 7, 10, 11, -2])) 

def exponents(bases, powers):
  new_lst = []
  for x in bases:
    for y in powers:
      new_lst.append(x ** y)
  return new_lst

# print(exponents([2, 3, 4], [1, 2, 3])) 

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for x in lst1:
    sum1 += x
  for y in lst2:
    sum2 += y

  if sum1 > sum2:
    return lst1
  elif sum2 > sum1:
    return lst2
  elif sum1 == sum2:
    return lst1

# print(larger_sum([1, 9, 5], [2, 3, 7]))

def over_nine_thousand(lst):
  total_sum = 0

  for x in lst:
    total_sum += x
    if total_sum > 9000:
      break
  return total_sum

# print(over_nine_thousand([8000, 900, 120, 5000]))

def max_num(nums):
  maximum = 0
  for x in nums:
    if x > maximum:
      maximum = x
  return maximum

# print(max_num([50, -10, 0, 75, 20]))


def same_values(lst1, lst2):
  new_lst = []
  for x in range(len(lst1)):
    if lst1[x] == lst2[x]:
      new_lst.append(x)
  return new_lst

# print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

def reversed_list(lst1, lst2):
  if lst1 == lst2[::-1]:
    return True
  else:
    return False

# print(reversed_list([1, 2, 3], [3, 2, 1]))
# print(reversed_list([1, 5, 3], [3, 2, 1]))