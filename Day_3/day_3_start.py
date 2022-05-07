print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("how old are you? "))
    if age < 12:
        bill = 5
        print("child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("youth ticket are $7")   
    if age > 18:
        bill = 12
        if age >=45 and age <=55:
            bill -= bill
            print("You pass free") 
        else:
            print("adult ticket are $12.")
            
    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "y": 
        bill +=3
        print(f"Your pay ${bill}")

    else:
        print(f"your pay {bill}")

else: 
    print("Sorry, you have to grow taller before you can ride.")




