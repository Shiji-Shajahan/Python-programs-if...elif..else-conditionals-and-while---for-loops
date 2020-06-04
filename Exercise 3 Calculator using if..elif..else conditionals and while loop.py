print('Exercise 3: Calculator')
"""
possible_operations = ["sum", "difference", "multiplication", "division"]
Ask user which operation he wants
Check if operation is available in possible_operations list
Ask for first number
Ask for second number
Return result (depending on operation)
Which operation would you like to do? sum
What’s the first number? 2
What’s the second number? 4
The result of your operation is 6
"""


#method1

possible_operations = ["sum", "difference", "multiplication", "division"]
#Ask user which operation he wants
operation=input('Which operation would you like to do?')
#Check if operation is available in possible_operations list
if operation in possible_operations:
  print(f'{operation} is available in the list')
else:
  print(f'{operation} is not avilable in the list')
number1=int(input("What's the first number?"))
number2=int(input("What's the second number?"))
if operation=="sum":
  print('The result of your Sum operation is',(number1+number2))
elif operation=="difference":
   print('The result of your difference operation is',(number1-number2))
elif operation=="multiplication":
   print('The result of your multiplication operation is',(number1*number2))
else:
  print('The result of division operation is', number1/number2)
print()



print('Exercise 3: Calculator')
#method 2

possible_operations = ["sum", "difference", "multiplication", "division"]
#Ask user which operation he wants
operation=input('Which operation would you like to do?')
#Check if operation is available in possible_operations list
if operation in possible_operations:
  number1=int(input("What's the first number?"))
  number2=int(input("What's the second number?"))
  if operation=="sum":
    print('The result of your Sum operation is',(number1+number2))
  elif operation=="difference":
    print('The result of your difference operation is',(number1-number2))
  elif operation=="multiplication":
    print('The result of your multiplication operation is',(number1*number2))
  else:
    print('The result of division operation is', number1/number2)
else:
  print(f'{operation} is not avilable in the list')
print()



print('Exercise 3: Calculator')
#method 3 using while loop

possible_operations = ["sum", "difference", "multiplication", "division"]
#Ask user which operation he wants
operation="operation in calculator"
while operation!="close":
  operation=input('Which operation would you like to do?')
  #Check if operation is available in possible_operations list
  if operation in possible_operations:
    number1=int(input("What's the first number?"))
    number2=int(input("What's the second number?"))
    if operation=="sum":
      print('The result of your Sum operation is',(number1+number2))
    elif operation=="difference":
      print('The result of your difference operation is',(number1-number2))
    elif operation=="multiplication":
      print('The result of your multiplication operation is',(number1*number2))
    else:
      print('The result of division operation is', number1/number2)
  else:
    print(f'{operation} is not avilable in the list')
print("Close calculator")