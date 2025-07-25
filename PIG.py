import random 

def roll():
    min_val = 1
    max_val = 6

    Random_val = random.randint(min_val , max_val)

    return Random_val

while True:
    players = input ("Enter number of players (2-4): ")
    if players.isdigit():
        players = int (players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 !")
    else:
        print("Invalid! try again!")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer " , player_idx + 1 , " turn has just started.")
        print("Your Total score is : ", player_score[player_idx])
        curr_score = 0

        while True:
            should_roll = input("Would you like to roll ? Enter y for yes : ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You roll 1!, Turn done.")
                curr_score = 0
                break
            else:
                curr_score += value
                print("You roll a : " , value)
            print("Your score is : " , curr_score)
        player_score[player_idx] += curr_score
        print("Your Total Score is : ", player_score[player_idx])


max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("Player number " , winning_idx + 1 , "is Winner with score : ",max_score)