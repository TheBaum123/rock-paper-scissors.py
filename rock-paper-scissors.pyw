# import
from tkinter import *
import random

# create variables
player_choice = ""
computer_choice = ""
output = ""
player_and_computer_chose = ""

# possible decisions
possible_choices = ["rock", "paper", "scissors"]


# player chose button functions
def player_choice_rock():
    global player_choice
    global computer_choice
    player_choice = "rock"
    computer_choice = random.choice(possible_choices)


def player_choice_paper():
    global player_choice
    global computer_choice
    player_choice = "paper"
    computer_choice = random.choice(possible_choices)


def player_choice_scissors():
    global player_choice
    global computer_choice
    player_choice = "scissors"
    computer_choice = random.choice(possible_choices)


# #set label to You win
def win():
    global you_won_label
    global you_lost_label
    global tie_label
    you_won_label.grid_forget()
    you_lost_label.grid_forget()
    tie_label.grid_forget()
    you_won_label.grid(row=4, column=2)


#set label to You lose
def lose():
    global you_won_label
    global you_lost_label
    global tie_label
    you_won_label.grid_forget()
    you_lost_label.grid_forget()
    tie_label.grid_forget()
    you_lost_label.grid(row=4, column=2)


#set label to tie
def tie():
    global you_won_label
    global you_lost_label
    global tie_label
    you_won_label.grid_forget()
    you_lost_label.grid_forget()
    tie_label.grid_forget()
    tie_label.grid(row=4, column=2)


#win detection
def submit():
    global player_choice
    global computer_choice
    if player_choice in possible_choices:
        if player_choice == computer_choice:
            tie()
        if player_choice == "rock":
            if computer_choice == "scissors":
                win()
            if computer_choice == "paper":
                lose()
        if player_choice == "paper":
            if computer_choice == "rock":
                win()
            if computer_choice == "scissors":
                lose()
        if player_choice == "scissors":
            if computer_choice == "paper":
                win()
            if computer_choice == "rock":
                lose()
        print(player_choice, computer_choice)
        player_choice = ""
        computer_choice = ""


# create window
window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("600x300")

# Heading
heading = Label(window, text="Pick one!")
heading.grid(row=1, column=2)

# choose buttons
rock_button = Button(window, text="rock", command=player_choice_rock, padx=50, pady=20)
rock_button.grid(row=2, column=1)

paper_button = Button(window, text="paper", command=player_choice_paper, padx=50, pady=20)
paper_button.grid(row=2, column=2)

scissors_button = Button(window, text="scissors", command=player_choice_scissors, padx=50, pady=20)
scissors_button.grid(row=2, column=3)

# submit button
submit_button = Button(window, text="submit", command=submit, padx=50, pady=20)
submit_button.grid(row=3, column=2)

# win/lose/tie label
you_won_label = Label(window, text="You Won!")
you_lost_label = Label(window, text="You lost :(")
tie_label = Label(window, text="tie")

#configure grid layout
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.mainloop()
