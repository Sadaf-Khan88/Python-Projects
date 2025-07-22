
name = input("Enter your name: ")
print("Hi!" , name, ", Welcome to the Adventure Game.")

answer = input("You are walking on a mud road and it has come to an end, You have two Choices to go (Left/Right) : ").lower()

if answer == "left":
    answer = input("Now you are on a bridge , Enter walk to walk across or swim to swim through the  bridge : ").lower()
    if answer == "walk":
        answer = input("After crossing the bridge you come across a stranger. Enetr (Talk / Igore) : ").lower()
        if answer == "talk":
            print("Good, the stanger is impressed by you and gave you a piece of gold.")
            print("You Won this Adventure game!")
        
        elif answer == "ignore":
            print("You were made the person angry and he kill you!")
            print("You lost the game!")
    elif answer == "swim":
        print("You were eaten by the Alligator")
        print("You were lost the game!")

    else:
        print("Not a valid answer!")

elif answer == "right":
    answer = input("Now you are on a clean road and you saw there is a gun on the road. Dou you want to pick that gun or not? Enter (Pick / Ignore): ").lower()
    if answer == "pick":
        answer = input ("You saw a killer going to kill a boy do you save the boy by your gun or ignore him and win the game. Enter (Ignore / Kill) : ")
        if answer == "ignore":
            print ("The killer saw you were crossing the road and shoot you from your back!")
            print("You were lost the game!")
        elif answer == "kill":
            print("You were save that boy and crooss the road successfully!")
            print("You were win the Game!")

        else:
            print("Not a valid answer!")

    elif answer == "ignore":
        print("Now you come across a Killer and it willer kill you!")
        print("You were lost the game!")

    else:
        print("Not a valid answer!")

else: 
    print("Not a valid answer!")

print("Thank you for trying ",name)
