#Exercise 4
#Write a program that takes a set of numbers and prints the highest number among them without using the max() function. For example:
#{2, 56, 4, 29, 7}  → 56
print('Exercise 4')
#without for Loop
print('without for loop')
number={2, 56, 4, 29, 7}
#Transform set to list
number_1=list(number)
number_1.sort()
print('Print Highest number in the set',number_1[-1])
print()

#Method 2
print('Exercise 4 Method 2')
##using for loop with sort()
number={2, 56, 4, 29, 7}
number_1=[]
for i in number:
  print(i)
  number_1.append(i)
print(number_1)
number_1.sort()
print('Print Highest number in the set',number_1[-1])
print()  

#Method 3
print('Exercise 4 Method 3')
number={2, 56, 4, 29, 7}
number_1=list(number)
high=number_1[0]
#using for loop without sort()
for i in number_1:
  if i>high:
    high=i
print(high)
print('Print Highest number in the set',high)
print()