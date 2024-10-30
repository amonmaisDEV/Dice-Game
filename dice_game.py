import random
import time

def roll_dice(): # a function that manages player's and computer's dice 
    play = str(input("Write 'Play' to play: ")).lower() # If you write play, the code will launch
    print(play)
    player = random.randint(1, 6) # select a fork between 1 and 6
    print(player)
    computer_choose = random.choice([1, 2, 3, 4, 5, 6]) # select a fork between 1 and 6 for the computer
    time.sleep(1)
    print(computer_choose)

    if computer_choose < player:
        print("you won")
    elif computer_choose > player:
        print("you loose")
    else:
        print("no one won")

def try_again():
    try_again_ = str(input("Try again ?: "))
    print(try_again_)
    if try_again_ == "yes":
        roll_dice()

roll_dice()
print("If you wanna quit, press Ctrl+C")
try_again()


    
