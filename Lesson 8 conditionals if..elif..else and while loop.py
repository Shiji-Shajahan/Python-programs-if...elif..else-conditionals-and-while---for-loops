#Lesson 8 Conditionals and While loop
print('else if')
age=int(input("How old are you?"))
if age>18:
    print("You can go Partying")
else:
    if(age==18):
        print("You are lucky. Now you can go party!")
    else:
        print("You are too young")
print()

#Method 2
print('elif')
age=int(input("How old are you?"))
if age>18:
    print("You can go Partying")
elif age==18:
    print("You are lucky. Now you can go party!")
else:
    print("You are too young")
print()

#“Write a program that takes two numbers as inputs. Print the biggest number.”
#what if they are the same? 
number1=int(input("Enter First Number"))
number2=int(input("Enter Second Number"))
if number1>number2:
    print(f"{number1} is bigger")
elif number1==number2:
    print("Both the numbers are same")
else:
    print(f"{number2} is bigger")
print()

print('Example3')
#“Write a program that takes a number from a user and tells the user if the number is even or odd.​”
#Is zero even or odd? 
number=int(input("What's the number?"))
if number==0:
  print(f"{number} is zero")
elif number%2==0:
  print(f"{number} is even")
else:
  print(f"{number} is odd")
print()

#conditions if...in
print('conditiona if...in')
print("Example1")
shopping_list=["bread","butter","orange"]
if "bread" in shopping_list:
    print("I need to buy bread")
else:
    print("I do not need to buy that")
print()

print("Example2")
sentence = "Guten Morgen!"
if "Morgen" in sentence:
    print("Morgen? That sounds German!")
print()

print("Example3")
sentence = "Guten Morgen!"
if "morgen" in sentence.lower():
    print("Morgen? That sounds German!")
print()

print("Conditions if..not in")
print("Example 1")
number=2
my_dict={1:"one", 3:"three", 5:"five"}
if number not in my_dict:
    print("I do not know how to translate it")
print()

print("Example 2")
spoken_languages = ["english", "portuguese", "spanish", "german"]
if "russian" not in spoken_languages:
    print("Sorry sorry, kein Russisch, no Russian")
print()

print("Example 3")
name = "Max Mustermann"
if "Mustermann" not in name:
    print("We're for sure not family ...")
print()

print('While loop')
print('Example 1')
print('Print i while (as long as) i is less than 10:')
i=1
while i<10:
    print(i)
    i=i+1
print("Done")
print()

print("Example 2")
print('Write a program that sums all number from 1 to 10 (including 1 and 10)')
print('Test condition: i <= 10')
i=1
total=0
while i<=10:
    total=total+i
    i=i+1
    print(f"i={i} total={total}")
print("Total is",total)
print()

print("Example 3")
print("Write a program that asks the user to write a word, until he writes “stop”")
user_input=input("Write a word:")
while user_input!="stop":
    user_input=input("Write a word:")
print("Finish")
print()