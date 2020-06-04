#Exercise 1: Healthy Food Check
#Define a list with some fruits
#Define a list with vegetables
#Ask the user to write a food
#Is it a fruit? Is it a vegetable? If not, it’s probably unhealthy, don’t eat it!


print("Exercise 1: Healthy Food Check")
#Define a list with some fruits
fruits=["apple","orange","grapes"]
#Define a list with vegetables
vegetables=["onion","carrot","tomato"]
#Ask the user to write a food
food=input('Please enter name of any food:').lower()
#Is it a fruit? Is it a vegetable? If not, it’s probably unhealthy, don’t eat it!
if food in fruits:
  print(f'{food} is a fruit')
elif food in vegetables:
  print(f'{food} is a vegetable')
else:
  print(f'{food} it’s probably unhealthy, don’t eat it!')
print("Thankyou for entering food item")
print()