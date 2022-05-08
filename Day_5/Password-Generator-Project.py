#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if nr_letters > 1:
    randomletters = random.sample(letters,nr_letters)
if nr_numbers > 1:
    randomnumbers = random.sample(numbers,nr_numbers)
if nr_symbols > 1:
    randomsymbols = random.sample(symbols,nr_symbols)

password2 = randomletters + randomnumbers + randomsymbols
password1 =randomletters + randomnumbers + randomsymbols
random.shuffle(password1)

hardmode = ''.join(password1)
easymode = ''.join(password2)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

print(f"modo facil: {easymode}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(f"modo dificil: {hardmode}")

