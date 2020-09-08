from random import randint
from time import sleep

def get_choice():
    choice = input("\n>>> ")
    choice_title = choice.title()
    return choice_title

def flip_coin():
    print("\n    Flipping coin...")
    for i in range(2):
        sleep(1)
        print("    .")                     
    return randint(1, 2)  

def roll_die(number_of_sides):
    print(f"\n    Rolling d{number_of_sides}...")
    for i in range(2):
        sleep(1)
        print("    .")
    return randint(1, number_of_sides)

def program_start():
    print("\n***Welcome to Coin Flipper!***")
    while True:
        print("\n    Would you like to:\n\n\t1. Flip a Coin?\n\t2. Roll a Die?\n\t3. Quit?")
        choice = get_choice()
        if choice == "1" or "Flip" in choice or "Coin" in choice:
            coin_flipper()
        elif choice == "2" or "Roll" in choice or "Die" in choice:
            die_roller()
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
    total_heads_guesses = 0
    total_tails = 0
    total_tails_guesses = 0
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
                total_heads_guesses += 1
                total_wins += 1
            elif choice == "2" or "Tails" in choice:
                print("Sorry, your guess was INCORRECT...")
                total_flips += 1
                total_heads += 1
                total_tails_guesses += 1
                total_losses += 1
            else:
                print("Something went wrong...")
        elif coin_flip == 2:
            print("\nThe coin flip came up **Tails!**")
            if choice == "1" or "Heads" in choice:
                print("Sorry, your guess was INCORRECT...")
                total_flips += 1
                total_tails += 1
                total_heads_guesses += 1
                total_losses += 1
            elif choice == "2" or "Tails" in choice:                                
                print("Congratulations, your guess was CORRECT!")
                total_flips += 1
                total_tails += 1
                total_tails_guesses += 1
                total_wins += 1
            else:
                print("Something went wrong...")
        print(f"""
    ******************************
        Total Flips: {total_flips}
        Total Heads: {total_heads}
        Total Heads Guesses: {total_heads_guesses}
        Total Tails: {total_tails}
        Total Tails Guesses: {total_tails_guesses}
        Correct Guesses: {total_wins}
        Incorrect Guesses: {total_losses}
        Win Percentage: {round(total_wins / total_flips * 100, 2)}%
    ******************************""")

def die_roller():
    print("\n***Get ready to roll a die!!***")  
    die_sides = None    
    total_rolls = 0      
    total_wins = 0
    total_losses = 0
    while die_sides == None:                  
        print("\n    What type of die would you like to roll?\n\n\t1. Enter Number of Sides (3 - 100)\n\tE. Exit to Main Menu")
        choice = get_choice()
        if choice == "E" or "Exit" in choice or "Menu" in choice:
            program_start()
        try:            
            if int(choice) in range(3, 101):
                die_sides = int(choice)
                print(f"\n***Rolling a d{str(die_sides)}!***")            
            else:
                print("\nPlease enter a valid number of sides.")
        except ValueError:
            print("\nThis is not a valid choice.  Please try again.")
    while True:        
        print(f"\n    What is your guess?\n\n\t1. Enter Guess (1 - {str(die_sides)})\n\tE. Exit to Main Menu")
        choice = get_choice()
        if choice == "E" or "Exit" in choice or "Menu" in choice:
            program_start()
        try:
            guess = int(choice)
            if guess in range(1, die_sides + 1):
                roll = roll_die(die_sides)
                print(f"\nYou rolled a **{str(roll)}**!")            
                if guess == roll:
                    print(f"Congratulations, your guess was CORRECT!")
                    total_rolls += 1
                    total_wins += 1
                elif guess != roll:
                    print(f"Sorry, your guess was INCORRECT...")
                    total_rolls += 1
                    total_losses += 1 
                print(f"""
        ******************************
            Die Type: d{str(die_sides)}
            Total Rolls: {total_rolls}        
            Correct Guesses: {total_wins}
            Incorrect Guesses: {total_losses}
            Win Percentage: {round(total_wins / total_rolls * 100, 2)}%
        ******************************""")
            else:
                print("\nPlease select a valid guess.")
        except ValueError:
            print("\nThis is not a valid choice.  Please try again.")

program_start()
