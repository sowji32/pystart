import random
n=100
print("WELCOME TO NUMBER GUESSING GAME")
ran_num=random.randint(1,100)
level=(input("Enter level of difficulty Hard/Medium/Easy:"))
chances=0
if(level=="Hard"):
    chances=5
elif(level=="Medium"):
    chances=10
elif(level=="Easy"):
    chances=15
else:
    print("Enter valid input")
    level=(input("Enter level of difficulty Hard/Medium/Easy:"))
    if(level=="Hard"):
        chances=5
    elif(level=="Medium"):
        chances=10
    elif(level=="Easy"):
        chances=15
count=0
print(f"You have {chances} chances")
for i in range(chances):
    if(count==chances-1):
        print("You have only last one chance")
    user_input=int(input(f"Enter your guess number in range {n}:"))
    if(user_input<0) or(user_input>100):
        print("Invalid Input")
        break;
    if(user_input==ran_num):
        print("You won the game")
        print("CONGRATULATIONS!!!")
        break;
    if(count==chances-1):
        print("sorry you lost the game")
        print("please,Try again")
        break;
    elif(user_input>ran_num):
        print("your number is greater than lucky number")
        count+=1
    elif(user_input<ran_num):
        print("your number is Less than lucky number")
        count+=1
    
    
    



