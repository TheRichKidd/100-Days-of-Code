'''
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
'''
# 🚨 Don't change the code below 👇
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line
white_list = []
temporal_List = white_list.extend(names)
random_system = random.randint(0,15)
print(random_system)

if random_system == 1:
    print(f"{white_list[0]} is going to buy the meal today!")

elif random_system == 2:
    print(f"{white_list[1]} is going to buy the meal today!")

elif random_system >= 3:
    print(f"{white_list[2]} is going to buy the meal today!")

elif random_system >= 5:
    print(f"{white_list[3]} is going to buy the meal today!")

elif random_system >= 7:
    print(f"{white_list[4]} is going to buy the meal today!")

elif random_system >= 8:
    print(f"{white_list[5]} is going to buy the meal today!")

elif random_system >= 10:
    print(f"{white_list[6]} is going to buy the meal today!")

elif random_system >= 11:
    print(f"{white_list[7]} is going to buy the meal today!")

elif random_system >= 15:
    print(f"{white_list[8]} is going to buy the meal today!")

else:
    print("ohohoh, that's great lucky, try again")
























