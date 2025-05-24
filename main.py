import random
import time


def start_game():
    streak_number = 0
    while True:
        number_of_cracks = random.randint(1, 5)
        try:
            players_guess = int(
                input("Input the number you predict! Has to be between 1-5.\n\t")
            )
        except ValueError:
            print("Thats not a number! Try again.")
            continue

        if players_guess == number_of_cracks:
            time.sleep(1)
            print("Congrats, You guessed just right!")
            streak_number += 1
            time.sleep(1)
            print("Streak:", streak_number)
        elif players_guess > number_of_cracks:
            time.sleep(1)
            print("Too much!!! Damn!!")
            time.sleep(1)
            print("The correct amount of cracks is:", number_of_cracks)
            streak_number = 0
            time.sleep(1)
            print("Streak:", streak_number)
        else:
            time.sleep(1)
            print("Oof, too little..")
            time.sleep(1)
            print("The correct amount of cracks is:", number_of_cracks)
            streak_number = 0
            time.sleep(1)
            print("Streak:", streak_number)

        
        play_again = input("Would you like to play again? Yes/No.\n").lower()
        if play_again == "no":
            time.sleep(1)
            print("Thanks for playing! Your final streak was", streak_number, ".")
            break


# Game Intro
print("Hi! \nDo you think you can predict how many cracks until the egg breaks?")
time.sleep(2)
playing = input("Would you like to start the game? Yes/No.\n").lower()

if playing == "no":
    no_game = input("Awww, are you sure? :(\n").lower()
    if no_game == "yes":
        print("Oh... okay.. i guess....")
elif playing == "yes":
    start_game()
else:
    print("Not a valid input!")
