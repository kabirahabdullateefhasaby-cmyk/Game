import random

choices = ["rock","paper","scissors"]
computer = random.choice(choices)
player = input("choose rock, paper, scissors: ") 
print(computer)

if player == "rock" or player == "paper" or player == "scissors":
    print("you win!")
elif player == computer:
    print("it a tie!")
else:
    print("computer win!")


while True:
    player = input("Enter your choices (rock paper scissor) or 'q' to quit: ").lower().strip()

    if player == "q":
        print("thanks for playing")
        break
    if player not in choices:
        print("Invalid choices. please try again.\n")
        continue
    computer = random.choice(choices)
    print(computer)
    if player == computer:
        print("it a tie")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("computer win!")
    else:
        print("you win!")

        

   
  


       