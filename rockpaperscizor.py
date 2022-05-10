import random
import userschoice

next_turn = True

while next_turn:
    u = userschoice.user_selection()
    u = u.lower()

    while u != "rock" and u != "paper" and u != "scissor" :
        print("Your choice is not correct. Your choices are rock,paper,scissor \n")
        u = userschoice.user_selection()
        u = u.lower()
    
    possible_actions = ["rock","paper","scissor"]
    machine_choice = random.choice(possible_actions)

    print("\nYou choose: " + u + "\n\n" + "Machine choose: " + machine_choice + "\n\n")
    if u == machine_choice:
        print("We got a tie!!")
    elif u == "rock":
        if machine_choice == "paper":
            print("Machine wins\n")
        elif machine_choice == "scissor":
            print("You win\n")
    elif u == "paper":
        if machine_choice == "scissor":
            print("Machine wins\n")
        elif machine_choice == "rock":
            print("You win\n")
    else:
        if machine_choice == "rock":
            print("Machine wins\n")
        elif machine_choice == "paper":
            print("You win\n")

    again = input("Do you want to play again?(y/n): ")
    while again != "y" and again != "n":
        again = again = input("Do you want to play again?(y/n): ")
    
    if again == "y":
        next_turn = True
    else:
        next_turn = False

    