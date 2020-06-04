print('Exercise 5: Guess my number')
"""
Generate a random number between 0 and 20
Ask for the user to input a try until he guesses the number
Give him a hint for every wrong try ("Go higher", "Go lower", "Hot", "Cold", ...)
When he guesses the number, congratulate him with a nice message
"""

#Generate a random number between 0 and 20
from random import randint
random_value = randint(0, 20)
print(random_value)
#Ask for the user to input a try until he guesses the number
number= int(input('Enter any number'))
while number!=random_value:
  if(random_value==number+5):
    print('Add 5 to the previous number')
  elif (random_value==number-5):
    print('subtract 5 from the previous number')
  elif (random_value==number-2):
    print('subtract 2 from the previous number')
  elif (random_value==number+2):
    print('Add 2 to the previous number')
  elif(number > random_value):
    print("Go lower ")
  else:
    print("Go Higher")
  number= int(input('Enter any number'))
print('Congratulations you have entered the right value')
print()

"""
#method 2
print('Exercise 5: Guess my number')
#Generate a random number between 0 and 20
from random import randint
random_value = randint(0, 20)
print(random_value)
#Ask for the user to input a try until he guesses the number
number= int(input('Enter any number'))
while number!=random_value:
  if(number > random_value):
    print("Go lower ") 
  else:
    print('Go Higher')
  number= int(input('Enter any number'))
print('Congratulations you have entered the right value')
print()
"""

"""
#method 3
print('Exercise 5: Guess my number')
#Generate a random number between 0 and 20
import random
random_value = random.randint(0, 20)
print(random_value)
#Ask for the user to input a try until he guesses the number
number= int(input('Enter any number'))
while number!=random_value:
  if(number > random_value):
    print("Go lower ") 
  else:
    print('Go Higher')
  number= int(input('Enter any number'))
print('Congratulations you have entered the right value')
"""
