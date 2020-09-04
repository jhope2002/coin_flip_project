from random import randint
from time import sleep

def get_choice():
    choice = input("\n>>> ")
    choice_title = choice.title()
    return choice_title

def flip_coin():
    print("\n    Flipping coin...")
    for i in range(3):
        sleep(1)
        print("    .")                     
    return randint(1, 2)  

def program_start():
    print("\n***Welcome to Coin Flipper!***")
    while True:
        print("\n    Would you like to:\n\n\t1. Flip a Coin?\n\t2. Roll a Die?\n\t3. Quit?")
        choice = get_choice()
        if choice == "1" or "Flip" in choice:
            coin_flipper()
        elif choice == "2" or "Roll" in choice:
            die_roll()
        elif choice == "3" or "Quit" in choice:
            print("\nThanks for Playing Coin Flipper!")
            print("\nGoodbye!\n")
            exit(0)
        else:
            print("\nI do not understand. Please try again.")

def coin_flipper():
    print("\n***Get ready to flip a coin!***")
    total_flips = 0
    total_heads = 0
    total_tails = 0
    total_wins = 0
    total_losses = 0    
    while True:
        print("\n    What is your guess?\n\n\t1. Heads\n\t2. Tails\n\n\t3. Exit to Main Menu")
        choice = get_choice()
        if choice == "3" or "Exit" in choice or "Menu" in choice:
            program_start()        
        coin_flip = flip_coin() 
        if coin_flip == 1:
            print("\nThe coin flip came up **Heads**!")
            if choice == "1" or "Heads" in choice:                                
                print("Congratulations, your guess was CORRECT!")
                total_flips += 1
                total_heads += 1
                total_wins += 1
            elif choice == "2" or "Tails" in choice:
                print("Sorry, your guess was INCORRECT...")
                total_flips += 1
                total_tails += 1
                total_losses += 1
            else:
                print("Something went wrong...")
        elif coin_flip == 2:
            print("\nThe coin flip came up **Tails!**")
            if choice == "1" or "Heads" in choice:
                print("Sorry, your guess was INCORRECT...")
                total_flips += 1
                total_tails += 1
                total_losses += 1
            if choice == "2" or "Tails" in choice:                                
                print("Congratulations, your guess was CORRECT!")
                total_flips += 1
                total_heads += 1
                total_wins += 1
        print(f"""
    ******************************
        Total Flips: {total_flips}
        Total Heads: {total_heads}
        Total Tails: {total_tails}
        Correct Guesses: {total_wins}
        Incorrect Guesses: {total_losses}
        Win Percentage: {round(total_wins / total_flips * 100, 2)}%
    ******************************
""")

def die_roll():
    print("\nDie Roller Feature coming soon!")        

program_start()