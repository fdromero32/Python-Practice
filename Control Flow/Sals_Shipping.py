premium_shipping = 125.00

def ground_shipping(weight):
  if weight <= 2.0 and weight >= 0:
    return '{:.2f}'.format((weight * 1.50) + 20)
  elif weight > 2.0 and weight <= 6.0:
    return '{:.2f}'.format((weight * 3.00) + 20)
  elif weight > 6.0 and weight <= 10.0:
    return '{:.2f}'.format((weight * 4.00) + 20)
  elif weight > 10:
    return '{:.2f}'.format((weight * 4.75) + 20)
  else:
    return "Your package doesn't weigh anything!"

def drone_shipping(weight):
  if weight <= 2.0 and weight >= 0:
    return '{:.2f}'.format(weight * 4.50)
  elif weight > 2.0 and weight <= 6.0:
    return '{:.2f}'.format(weight * 9.00)
  elif weight > 6.0 and weight <= 10.0:
    return '{:.2f}'.format(weight * 12.00)
  elif weight > 10:
    return '{:.2f}'.format(weight * 14.25)
  else:
    return "Your package doesn't weigh anything!"

def cheapest_shipping(weight):
  if float(ground_shipping(weight)) < float(drone_shipping(weight)) and float(ground_shipping(weight)) < premium_shipping:
    return f'The cheapest shipping method is ground shipping. It would cost ${ground_shipping(weight)} to ship your item.'
  elif float(drone_shipping(weight)) < float(ground_shipping(weight)) and float(drone_shipping(weight)) < premium_shipping:
    return f'The cheapest shipping method is drone shipping. It would cost ${drone_shipping(weight)} to ship your item.'
  elif premium_shipping < float(ground_shipping(weight))  and premium_shipping < float(drone_shipping(weight)):
    return f'The cheapest shipping method is premium shipping. It would cost ${"%2.2f" % premium_shipping} to ship your item.'
  else:
    return "Error. You have input an invalid weight."


# print(cheapest_shipping(4.8))
# print(cheapest_shipping(41.5))

