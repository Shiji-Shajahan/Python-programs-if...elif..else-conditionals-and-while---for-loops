# Check if a number exists in a list
#method 1
my_list = [1, 2, 9, -5, 5, 6, 8, 4, 3, 7, 6]
user_number = int(input('Please enter a number:'))
for number in my_list:
  if number == user_number:
    print('I found it in my list!!!')
print()

#method 2
my_list = [1, 2, 9, -5, 5, 6, 8, 4, 3, 7, 6]
user_number1 = int(input('Please enter a number:'))
[print('I found it in my list!!!')for number in my_list if number==user_number1]
print()

#method3
my_list = [1, 2, 9, -5, 5, 6, 8, 4, 3, 7, 6]
user_number2 = int(input('Please enter a number:'))
if user_number2 in my_list:
  print('I found it in my list!!!')
else:
  print('Sorry number not found')
print()

#Example2
# Check if a even number exists in a list
my_list1 = [1, 2, 9, -5, 5, 6, 8, 4, 3, 7, 6]
for number in my_list1:
  if (number % 2) == 0:
    print('I found an even number in my list1!!!')
print()

#method2
[print('I found an even number in my list1') for number in my_list1 if number%2==0]
print()

#Example2
# Check if a even number exists in a list
my_list1 = [1, 2, 9, -5, 5, 6, 8, 4, 3, 7, 6]
for number in my_list1:
  if (number % 2) == 0:
    print('I found an even number in my list1!!!',number)
    break
print()

"""
# Check if a number exists in a list
print('Hello this program helps you do multiplication :)')
first_number = int(input('Enter first number'))
second_number = int(input('Enter second number'))
result = (first_number*second_number)
print ('Multiplication result is:', result)
"""
#continue
speakers=['Wael','Sid','Ben','Ana']
for speaker in speakers:
  print('Thankyou for your intervention',speaker)
print()

#except ana we have to send a message
speakers=['Wael','Sid','Ben','Ana']
for speaker in speakers:
  if speaker == 'Ana':
    print('Sorry Ana, you are a teacher')
    continue
  print('Thankyou for your intervention',speaker)
print()

#to continuously run a program
#while True:
print('Hello this program helps you do multiplication :)')
while True:
  first_number = int(input('Enter first number'))
  second_number = int(input('Enter second number'))
  result=first_number*second_number
  print ('Multiplication result is:', result)

