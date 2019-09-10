#!/usr/bin/python3

x = 15
price = 9.99
discount = 0.2
result = price * (1 - discount)
print(result)



name = "Rolf"
print(name)



name = "Bob"
#greeting = "Hello, " + name
greeting = f'Hello, {name}'
print(greeting)



longer_phrase = "Hello {}, today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)



name = input('What is your name? ')
print('Hi ' + name + ', you smell bad.')




size_input = input('How big is your house (in square feet): ')
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is {square_meters:.2f} square meters.")



user_age = input('What is your age: ')
years = int(user_age)
months = years * 12
print(f"Your age is {years} which is equal to {months} months.")



