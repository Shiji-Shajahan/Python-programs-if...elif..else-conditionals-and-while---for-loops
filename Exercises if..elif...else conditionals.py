#if...else
#Minimum of two numbers
print('Example 1')
number1= int(input("Enter First Number:"))
number2= int(input("Enter Second Number:"))
if number1<number2:
  print(f'Number1 is minimum:{number1}')
else:
  print(f'Number 2 is minimum:{number2}')
print('Done')
print()

print('Example 2')
#For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.

#Try to use the cascade if-elif-else for it.
number3=int(input("Enter any integer X:"))
if number3>0:
  print('1')
elif number3==0:
  print('0')
else:
  print('-1')
print('finish')
print()

print('Example3')
#Given a three-digit integer X consisting of three different digits, print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.
num=input('Please enter a three digit integer consisting of different digits:')
if num[0]<num[1]<num[2]:
  print('YES')
else:
  print('NO')
print('Finish')
print()

print('Example 4')
#Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.
month=int(input("please enter any month in integer format in the year 2017"))
if month==1:
  print('January: no of days is 31')
elif month==2:
  print('February: no of days is 28')
elif month==3:
  print('March: no of days is 31')
elif month==4:
  print('April: no of days is 30')
elif month==5:
  print('May: no of days is 31')
elif month==6:
  print('June: no of days is 30')
elif month==7:
  print('July: no of days is 31')
elif month==8:
  print('August: no of days is 31')
elif month==9:
  print('September: no of days is 30')
elif month==10:
  print('October: no of days is 31')
elif month==11:
  print('November: no of days is 30')
else:
  print('December: no of days is 31')
print('Done')
print()

print("Example 5")
#while
#Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the maximum of the sequence.  
i=  "user given integer"
while i!=0:
  i=int(input('Enter a sequence of non-negative integer'))
  if i>0:
    print(i)
  else:
    print('done')
print('Thankyou')