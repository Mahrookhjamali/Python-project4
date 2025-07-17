import random
choices=["Rock","Paper","Scissor"]
computer=random.choice(choices)
player=input("Choose Rock,Paper,Scissor:")
if player==computer:
    print("It's a tie")
elif(player=="Rock"and computer=="Scissor") or (player=="Paper"and computer=="Rock") or (player=="Scissor"and computer=="Paper"):
    print("You win!")
else:
    print("Computer wins!")