def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

# print(append_sum([1, 1, 2]))

# Larger List
def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  elif len(lst1) == len(lst2):
    return lst1 [-1]
  else:
    return "Please input a List"

# print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# More than N
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Append Size
def append_size(lst):
  lst.append(len(lst))
  return lst

# print(append_size([23, 42, 108]))

# Combine Sort
def combine_sort(lst1, lst2):
  new_list = lst1 + lst2
  new_list.sort()
  return new_list

# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
def every_three_nums(start):
  if start > 100:
    return []
  else:
    return list(range(start, 101, 3))

# print(every_three_nums(91))

def remove_middle(lst, start, end):
  new_list = lst
  del new_list[start:end + 1]
  return new_list

# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# More frequent Items
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) == lst.count(item2):
    return item1
  else:
    return item2

# print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Double Index
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index]

  new_lst.append(lst[index]*2)
  new_lst = new_lst + lst[index+1:]
  return new_lst

print(double_index([3, 8, -10, 12], 2))

# Middle Item
import math

def middle_element(lst):
  mid_position = math.ceil(len(lst)/2)
  if len(lst) % 2 == 1:
    return lst[mid_position - 1]
  else:
    return (lst[mid_position] + lst[mid_position - 1]) / 2

print(middle_element([5, 2, -10, -4, 4, 5]))