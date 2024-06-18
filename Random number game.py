import random

def Game_start(Start, Finish):
    Choosen_number = random.randint(Start, Finish)
    Player_Number = int(0)
    Wrong = int(0)
    
    while True:
        Player_Number == int(input("Choose: ", ))
        if Player_Number != Choosen_number:
            print("Wrong")
            print(Choosen_number)
            Wrong += 1
        if Player_Number == Choosen_number:
            print("You Won\n")
            print("You number of attempts: ", Wrong)
            exit() 
        if Wrong == 10:
            print(f"Hint: its Bettwen {Choosen_number - 10} and {Choosen_number + 10}")
        

Game_start(1, 100)
