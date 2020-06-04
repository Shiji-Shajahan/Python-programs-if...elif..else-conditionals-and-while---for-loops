#Exercise 2: Encyclopedia
#Ask the user to input a country
#Return capital of the country, by using:
#If, elif, else
#Using a dictionary: 
#Check if country doesnt exist (if not in)
#… else (return value from dictionary)


print("Exercise 2: Encyclopedia")
print('using a dictionary')
country_capital={"India":"New Delhi","UK":"London","Germany":"Berlin","Nigeria":"Abuja","France":"Paris"}
#Ask the user to input a country
country= input('Pick a country:')
if country not in country_capital:
  print(f"Sorry, I don’t know the capital of {country}")
else:
  print(f'The capital city of {country} is',country_capital[country])
print('Thank you entering country name')
print()

print("Exercise 2: Encyclopedia")
print('using if,elif,else')
#Ask the user to input a country
country_name= input('Pick a country:')
if country_name =="India":
  print('The capital city of India is New delhi')
elif country_name == "UK":
  print('The capital city of UK is London')
elif country_name =="Germany":
  print('The capital city of Germany is Berlin')
elif country_name == "Nigeria":
  print('The capital city of Nigeria is Abuja')
elif country_name == "France":
  print('The capital city of France is Paris')
else:
  print(f"Sorry, I don’t know the capital of {country}")
print('Thank you entering country name')
print()
