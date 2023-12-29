###################
Loop- If,Elif and Else
########################

# Find out how good you are at a game based on your score
# Insert your score
score = input("Enter your score: ")
print('Score obtained:', score)

# Score Conditions
if int(score) >= 90:
    print('Pro Level: Outstanding Player')
elif 70 <= int(score) < 90:
    print('Intermediate Level: Skilled Player')
elif 50 <= int(score) < 70:
    print('Beginner Level: Getting there')
else:
    print('Novice Level: Keep practicing')
