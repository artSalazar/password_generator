#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = [] #empty list

for i in range(nr_letters): #adds all the letters together
    i = random.choice(letters)
    password.append(i)
    
for i in range(nr_numbers): #adds all the numbers together
    i= random.choice(numbers)
    password.append(i)
    
for i in range(nr_symbols): #adds all the symbols together
    i=random.choice(symbols)
    password.append(i)
    
random.shuffle(password) #mixes up the list elements 
print("Here is your password:",''.join(password)) #join converts list into string object

"""

Welcome to the PyPassword Generator!
How many letters would you like in your password?
3
How many symbols would you like?
8
How many numbers would you like?
2
Here is your password: 88(!)u%)NT++)
"""
