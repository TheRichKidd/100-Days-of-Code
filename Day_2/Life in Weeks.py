'''
Create a program using maths and f-Strings that tells us how many days,
weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message 
with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
'''
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year_base = 90
year_day = 365
year_weeks = 52
year_months = 12
age_now = (year_base - int(age))
totaldays = (year_day * age_now)
totalweeks = (year_weeks * age_now)
totalmonths = (year_months * age_now)
print(f"You have {totaldays} days, {totalweeks} weeks, and {totalmonths} months left.")

