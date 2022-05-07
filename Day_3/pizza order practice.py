# 🚨 Don't change the code below 👇
a = 'hugo'
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S" :
    small = 15
    if add_pepperoni == "Y":
        small += 2
    if extra_cheese == "Y" :
        small += 1
        print(f"Your final bill is: {small}.")
    else:
        print(f"Your final bill is: {small}.")
        
if size == "M":
    medium = 20
    if add_pepperoni =="Y":
        medium += 3
    if extra_cheese == "Y":
        medium += 1
        print(f"Your final bill is: {medium}.")
    else: 
        print(f"Your final bill is: {medium}.")

if size == "L":
    large = 25
    if add_pepperoni =="Y":
        large += 3
    if extra_cheese =="Y":
        large += 1
        print(f"Your final bill is: {large}.")
    else: 
        print(f"Your final bill is: {large}.")

a = 'hugo'






























