#Exercise 5
#Create a list of that contains different types of elements: strings, integers, floats, more lists... You can use this one as example:
#['abc', 4, 3.2, [19, 1, 23], '12', 2, 2, 1.0]
print('Exercise 5')
print('A list including all datatypes')
newvar=['abc', 4, 3.2, [19, 1, 23], '12', 2, 2, 1.0]

#For every element on this list, check its type.
#If it's an integer, then calculate the power of 2 (x²) and save it to a new list. Output: [16, 4, 4]
print('Checking Type')
newvar1=[]
for element in newvar:
  print(f'Element {element} type is {type(element)}')
  if type(element) is int:
    newvar1.append(element*element)   
print(f'newvar1={newvar1}')
print('Done')
print()

#OPTIONAL: you can try to do it using list comprehension as well.
print('Exercise 5 list comprehension')
print('A list including all datatypes')
newvar=['abc', 4, 3.2, [19, 1, 23], '12', 2, 2, 1.0]
newvar2=[element*element for element in newvar if type(element) is int]
print(f'newvar2={newvar2}')
print('Done')
print()