import random
print("Welcome to Rock,paper,scissor Game")
n=int(input("Enter num of turns you want to play :"))
sc_user=0
sc_comp=0
for i in range(n):
    user_input=int(input("Enter your choice\n0 for Rock,1 for paper,2 for scissor:"))
    if(user_input)>2 or (user_input)<0:
        print("invalid input")
        print("please start game again")
        break;
    else:
        comp_input=random.randint(0,2)
        print(f"comp_choice {comp_input}")
        if(comp_input==user_input):
            sc_comp+=0
            sc_user+=0
            print(f"your score {sc_user}")
            print(f"comp score {sc_comp}")
        elif(comp_input==0 and user_input==2):
            sc_comp+=1
            print(f"your score {sc_user}")
            print(f"comp score {sc_comp}")
        elif(comp_input==2 and user_input==0):
            sc_user+=1
            print(f"your score {sc_user}")
            print(f"comp score {sc_comp}")
        elif(comp_input>user_input):
            sc_comp+=1
            print(f"your score {sc_user}")
            print(f"comp score {sc_comp}")
        elif(comp_input<user_input):
            sc_user+=1
            print(f"your score {sc_user}")
            print(f"comp score {sc_comp}")
if(sc_user > sc_comp):
    print("Congratulations you won the game")
    print(f"You win with {sc_user-sc_comp} points")
elif(sc_user < sc_comp):
    print("You lost the game,Better Luck next time")
    print(f"comp win with {sc_comp-sc_user} points")
        
        
