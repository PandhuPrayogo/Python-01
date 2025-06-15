import random as r

# Program mini game: rock scissors paper
#function to generate computer's choice
def game_operation(user_choice):
    computer_option = r.randint(1, 3)

    # Printing computer's choice
    if computer_option == 1:
        print("Computer chose Rock!")
    elif computer_option == 2:
        print("Computer chose Scissors!")
    else:
        print("Computer chose Paper!")

    if (computer_option == user_choice):
        print("It's a tie!")
    elif (computer_option == 1 and user_choice == "2") or \
        (computer_option == 2 and user_choice == "3") or \
        (computer_option == 3 and user_choice == "1"):
        print("You lose!")
    else:
        print("You win!")


# Main Program Loop
while True:
    print("Welcome to our mini game!\nChoose your option:\n1. Rock\n2. Scissors\n3. Paper\n4. Exit")
    user_choice = input("Input your choice: ")

    # input codition 
    if user_choice == "1":
        print("You chose Rock!")
        game_operation(user_choice)
    elif user_choice == "2":
        print("You chose Scissors!")
        game_operation(user_choice)
    elif user_choice == "3":
        print("You chose Paper!")
        game_operation(user_choice)
    elif user_choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input, please try again.")
        continue
    
    # Option to play again
    user_input = input("Do you want to play again? (y/n): ")
    if (user_input == "y"):
        print("\n")
        continue
    elif (user_input == "n"):
        print("Thanks for playing!")
        break
    else:
        print("Invalid input, chose correct input.")
        continue

