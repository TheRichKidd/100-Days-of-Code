# 🚨 Don't change the code below 👇
from cgi import print_arguments


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

high = 0
divisor = 0
#Write your code below this row 👇
for student in student_heights:
    high += student 
    divisor += 1

operation = round(high / divisor)
print(f"{operation}")





































