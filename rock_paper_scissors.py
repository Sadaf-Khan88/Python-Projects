import random

user_win = 0
computer_win = 0

options = ["rock" , "paper", "scissor"]

while True:
    user_input = input("Type : Rock/Paper/Scissor or q to quit : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    Random = random.randint(0,2)

    computer_pick = options[Random]
    print("Computer picked ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_win += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_win += 1
    
    elif user_input == computer_pick:
        print("Both pick same option")

    else:
        print ("You Lost!")
        computer_win += 1

print ("You Win", user_win, "times.")
print("Computer Win", computer_win, "times.")

print("Goodbye!")