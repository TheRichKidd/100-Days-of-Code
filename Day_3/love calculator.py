'''
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times 
the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.
'''
# 🚨 Don't change the code below 👇
from itertools import count
from sys import call_tracing

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name11 = name1.lower()
name22 = name2.lower()

t_1 = name11.count('t')  ;   l_1 = name11.count('l')
r_1 = name11.count('r')   ;  o_1 = name11.count('o')
u_1 = name11.count('u')   ;  v_1 = name11.count('v')
e_11 = name11.count('e')   ;  e_1 = name11.count('e')

t_2 = name22.count('t')  ;   l_2 = name22.count('l')
r_2 = name22.count('r')   ;  o_2 = name22.count('o')
u_2 = name22.count('u')   ;  v_2 = name22.count('v')
e_22 = name22.count('e')   ;  e_2 = name22.count('e')

call_t = t_1 + t_2 ;  call_l = l_1 + l_2
call_r = r_1 + r_2 ;  call_o = o_1 + o_2
call_u = u_1 + u_2 ;  call_v = v_1 + v_2
call_e = e_11 + e_22; call_e2 = e_1 + e_2

sum_true = ((call_t + call_r + call_u + call_e)*10)
sum_love = call_l + call_o + call_v + call_e2
sum_total_love = sum_true + sum_love

if sum_total_love <10 or sum_total_love >90:
    print(f"Your score is {sum_total_love}, you go together like coke and mentos.")
elif sum_total_love >= 40 and sum_total_love <= 50:
    print(f"Your score is {sum_total_love}, you are alright together.")
else: 
    print(f"Your score is {sum_total_love}.")

























