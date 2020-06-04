#Exercise3
#Write a program that sums all the numbers in a list, without using the sum() function. Use this list for the exercise: numbers = [54, 23, 11, 3, 20, 7]
#The output should be 118
print('Exercise 3')
print('Sum of all numbers in the List')
numbers = [54, 23, 11, 3, 20, 7]
total=0
for i in numbers:
  total+=i
print(total)
#using sum() function
print(sum(numbers))
print()