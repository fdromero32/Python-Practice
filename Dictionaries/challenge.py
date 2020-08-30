def sum_values(my_dictionary):
  sum_values = 0
  for x in my_dictionary.values():
    sum_values += x
  return sum_values

# print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# print(sum_values({10:1, 100:2, 1000:3}))

# Challenge #2
def sum_even_keys(my_dictionary):
  sum_values = 0
  for key, value in my_dictionary.items():
    if key % 2 == 0:
      sum_values += value
  return sum_values

# print(sum_even_keys({1:5, 2:2, 3:3}))
# print(sum_even_keys({10:1, 100:2, 1000:3}))

# Challenge 4:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

# print(add_ten({1:5, 2:2, 3:3}))
# print(add_ten({10:1, 100:2, 1000:3}))

# Challenge #5
def values_that_are_keys(my_dictionary):
  same = []
  for value in my_dictionary.values():
    for key in my_dictionary.keys():
      if value == key:
        same.append(key)
  return same

# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

# Challenge 6:
def max_key(my_dictionary):
  max_value = 0
  max_key_value = 0
  for key, value in my_dictionary.items():
    if value > max_value:
      max_value = value
      max_key_value = key
  return max_key_value

# print(max_key({1:100, 2:1, 3:4, 4:10}))
# print(max_key({"a":100, "b":10, "c":1000}))

# Challenge #7:
def word_length_dictionary(words):
  new_dict = {}
  for word in words:
    new_dict[word] = len(word)
  return new_dict

# Challenge 8:
def frequency_dictionary(words):
  new_dict = {}
  for word in words:
    new_dict[word] = words.count(word)
  return new_dict

# print(frequency_dictionary(["apple", "apple", "cat", 1]))
# print(frequency_dictionary([0,0,0,0,0]))

# Challenge #9:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# print(unique_values({0:3, 1:1, 4:1, 5:3}))
# print(unique_values({0:3, 1:3, 4:3, 5:3})) 

# Challenge 10:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters