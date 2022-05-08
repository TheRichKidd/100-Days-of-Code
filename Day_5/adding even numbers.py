highest_score = 0
for score in range(0,101):
    if score % 2 == 0:
        highest_score += score
    else:
        pass
    # print(highest_score)
print(f"The highest score in the class is: {highest_score}")
