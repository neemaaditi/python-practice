#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
let = random.sample(letters, nr_letters)
letter =  ''
for l in let:
    letter += l
sym = random.sample(symbols, nr_symbols)
symbol =  ''
for s in sym:
    symbol += s
num = random.sample(numbers, nr_numbers)
number =  ''
for n in num:
    number += n
pw = letter+""+symbol+""+number
pw_list = list(pw)

random.shuffle(pw_list)
password = ''.join(pw_list)
print(password)
