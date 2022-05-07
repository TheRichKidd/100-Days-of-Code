import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

random_logic = random.randint(0,2)
elective_player = int(input("rock'0', paper'1'or scissors'2'!!!\n"))
list_art = [rock,paper,scissors]



##################################################################################
#EMPATE
##################################################################################
print(f"\n{random_logic}")
#Rock
if random_logic ==0 and elective_player ==2:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\nYour lose")
if random_logic ==0 and elective_player ==1:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\nYour win")
if random_logic ==0 and elective_player == 0:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\n is It's a draw")
#paper
if random_logic ==1 and elective_player ==0:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\nYour lose")
if random_logic ==1 and elective_player ==2:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\nYour win")
if random_logic ==1  and elective_player == 1:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\n is It's a draw")
#scissors
if random_logic ==2 and elective_player ==0:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\nYour win")
if random_logic ==2 and elective_player ==1:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\nYour lose")
if random_logic ==2 and elective_player == 2:
    print(f"{list_art[elective_player]}\nComputer chose:\n{list_art[random_logic]}\n is It's a draw")    
#################################################################################










































