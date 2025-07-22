import random

top_of_range = input("Enter any number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter a number grater than 0 next time!")
else:
    print("Enter a number next time!")

random_guess = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number : ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number next time!")
        continue

    if user_guess == random_guess:
        print("Yeah! You got it.")
        break
    elif user_guess > random_guess:
        print("You were above the number!")
    else:
        print("You were below the number!")


print("You guess the correct number in " ,guesses, "guesses")