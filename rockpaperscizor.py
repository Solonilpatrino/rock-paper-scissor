import computerchoice
from tkinter import *

player_count = 0
computer_count = 0

root = Tk()

root.geometry("600x250")

root.title("Rock Paper Scissor")

def gameplay(user):
    computer = computerchoice.selection()

    global player_count
    global computer_count

    fight_label.config(text = "" + user + " VS " + computer + "" )

    if user == "rock":
        if computer == "paper":
             computer_count = computer_count + 1
             computer_score.config(text = computer_count)
        elif computer == "scissor":
             player_count = player_count + 1
             player_score.config(text = player_count)
    elif user == "paper":
        if computer == "scissor":
             computer_count = computer_count + 1
             computer_score.config(text = computer_count)
        elif computer == "rock":
             player_count = player_count + 1
             player_score.config(text = player_count)
    else:
        if computer == "rock":
             computer_count = computer_count + 1
             computer_score.config(text = computer_count)
        elif computer == "paper":
             player_count = player_count + 1
             player_score.config(text = player_count)
    


player_frame = Frame(root)
player_frame.pack(pady = 20)

player_label = Label(player_frame, text = "Player: ", font = 10)
player_label.pack(side = LEFT, padx = 10)

player_score = Label(player_frame, text = 0, font = "normal 10 bold")
player_score.pack(side = LEFT)

computer_frame = Frame(root)
computer_frame.pack(pady = 5)

computer_label = Label(computer_frame, text = "Computer: ", font = 10)
computer_label.pack(side = LEFT, padx = 10)

computer_score = Label(computer_frame, text = 0, font = "normal 10 bold")
computer_score.pack(side = LEFT)

title_label = Label(root, text = "Player VS Computer", font = 20).pack(pady = 5)

fight_label = Label(root, text = "", font = "normal 20 bold", bg = "white", width = 15, borderwidth = 2, relief = "solid")
fight_label.pack(pady = 5)

buttons_frame = Frame(root)
buttons_frame.pack(pady = 10)

rock = Button(buttons_frame, text = "Rock", font = 10, width = 7, command = lambda: gameplay("rock"))
rock.pack(side = LEFT, padx = 10)
 
paper = Button(buttons_frame, text = "Paper", font = 10, width = 7, command = lambda: gameplay("paper"))
paper.pack(side = LEFT, padx = 10)
 
scissor = Button(buttons_frame, text = "Scissor", font = 10, width = 7, command = lambda: gameplay("scissor"))
scissor.pack()
 

root.mainloop()

