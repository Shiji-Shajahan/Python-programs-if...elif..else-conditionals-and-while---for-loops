print('Exercise 4: Fizz Buzz')
#while 
#Write a program that prints the numbers from 1 to 100. 
#If it’s a multiple of 3, it should print “Fizz”. 
#If it’s a multiple of 5, it should print “Buzz”. If it’s a multiple of 3 and 5, it should print “Fizz Buzz”.

print('Print the numbers from 1 to 100')
i=1
while i<=100:
  if i%3==0 and i%5==0:
    print('Fizz Buzz')
  elif i%3==0:
    print('Fizz')
  elif i%5==0:
    print('Buzz')
  else:
    print(i)
  i=i+1
print('Done')