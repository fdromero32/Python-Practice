toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
# print(f'We will sell {num_pizzas} different kinds of pizza!')
pizzas = list(zip(toppings, prices))

def Sort(sub_list):
  sub_list.sort(key = lambda x: x[1])
  return sub_list

cheapest_pizza = Sort(pizzas)[0]
priciest_pizza = Sort(pizzas)[-1]
# print(cheapest_pizza)
# print(priciest_pizza)

three_cheapest = pizzas[0:3]
# print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)