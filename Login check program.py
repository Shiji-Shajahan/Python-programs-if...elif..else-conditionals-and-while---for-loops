"""
print('Login Check Program')
#Exercise1

print('Exercise 1')
#1. Create a list of 4 users: Ahmed, Yong, Sudhir, Julie
user=['ahmed','yong','sudhir','julie']
#2. Ask a user to enter her/his name
user_input=input('Please Enter user name:')
#3. Check if the name exists in the users list
#4. if the name exists, print a welcome message
#5. if the name does not exists, print a sorry message
if user_input.lower() in user:
  print('Welcome',user_input)
else:
  print(f'Sorry {user_input}, your name is not in the list')
print()



print('Exercise 2')
#Extend the code in Exercise 1 to handle the below case:
#If the input name is not in the users list, print a sorry message and ask the user to try again. 
#You should keep asking the user to retry until s/he enters a name that belongs to the list :)
#Hint: use while
user=['ahmed','yong','sudhir','julie']
user_input=input('Please Enter user name:')
while True:
  if user_input.lower() in user:
    print('Welcome',user_input)
    break
  else:
    print(f'Sorry {user_input}, your name is not in the list and please try again')
    user_input=input('Please Enter user name:')
print()


print('Exercise 3')
#Extend the code in Exercise 2 to handle the below case:
#Now for each user, add a given password:
#e.g. 'Ahmed': 's1234' # use a data structure that you have seen in previous lessons ;)
user=['ahmed','yong','sudhir','julie']
user_password={'ahmed':'a123','yong':'b456','sudhir':'c789','julie':'d369'}

#Now if the input name is correct, ask for the password.
#If the password is correct, print a welcome message
#Otherwise print a sorry message explaining that the password was wrong

while True:
  user_input=str(input('Please Enter user name:'))
  if user_input.lower() in user:
    password=input('please enter the password')
    if password==user_password[user_input]:
      print('Welcome',user_input)
      break
    else:
      print('You have entered a wrong password')
  else:
    print(f'Sorry {user_input}, your name is not in the list and please try again')
print()

"""
print('Exercise 4')
#Extend the code in Exercise 3 to handle the below case:
#If the user enters a wrong password, give her/him another chances.
#If after 3 times the password is wrong add the user name into a new list called "blocked_users" and tell the user that her/his account is now blocked.
#If the same user tries to log again, print a message that his account have been temporarily locked.

user=['ahmed','yong','sudhir','julie']
user_password={'ahmed':'a123','yong':'b456','sudhir':'c789','julie':'d369'}
blocked_users=[]

while True:
  user_input=str(input('Please Enter user name:'))

  while user_input.lower() not in user_password:
    user_input=str(input('Sorry Try again'))

  if user_input.lower() in blocked_users:
    print('sorry you have entered wrong password for three times and your account is now blocked')
    continue

  password=input('please enter the password')
  trial=0
  max_trial=2

  while user_password[user_input] !=password:
    password=input('Sorry,enter the correct password')
    trial+=1
    if trial > max_trial:
      print('Sorry you have failed for three times and account is blocked')
      break

  else:
    print(f'Welcome {user_input}')
    break


print('Exercise 5')
#Extend the code in Exercise 4 to handle the below case:
#If user enters a name that does not exists in the user lists, print a sorry message and ask if s/he would like to register. 
#If user enters 'y', 
#- save her/his name
#- ask user to enter a password
#(Optional: ask the user to enter it twice and only accept if first and second matches)
#If user enter different character than 'y', program should start the flow and ask user to enter username

user=['ahmed','yong','sudhir','julie']
user_password={'ahmed':'a123','yong':'b456','sudhir':'c789','julie':'d369'}
blocked_users=[]

while True:
  user_input=str(input('Please Enter user name:'))

  if user_input.lower() in blocked_users:
    print('your account is blocked')
    continue
    
  if user_input not in user_password:
    register = input('sorry your name is not in the list and would you like to register then type y:')
    if register != 'y':   
      print("Thankyou:)")
      continue
        
    new_user_input = input('Please enter your user name:')
    new_password_1 = input('Enter your password:')
    new_password_2 = input('Repeat your password:')
        
    while (new_password_1 != new_password_2):
      print('Passwords are not matching')
      new_password_1 = input('Enter your password')
      new_password_2 = input('repeat your password')
        
    user_password[new_user_input] = new_password_1
    print('Succefully registerd. Now you should be able to log with your credentials')
    continue

  password=input('please enter the password')
  trial=0
  max_trial=2

  while user_password[user_input] !=password:
    password=input('Sorry,enter the correct password')
    trial+=1
    if trial > max_trial:
      print('Sorry you have failed for three times and account is blocked')
      break

  else:
    print(f'Welcome {user_input}')
    break