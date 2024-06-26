# import
from tkinter import *
import random
import math

# create variables
player_choice = ""
computer_choice = ""
output = ""
player_and_computer_chose = ""
score = 0
number_of_games = 0
win_percentage = 0.0


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
    global win_percentage_label
    global score_label
    global you_won_label
    global you_lost_label
    global tie_label
    global score
    score += 1
    win_percentage = math.floor(score / number_of_games * 100)
    score_label = Label(window, text=f"score is {score}")
    win_percentage_label = Label(window, text=f"win percentage is {win_percentage}%")
    you_won_label.grid_forget()
    you_lost_label.grid_forget()
    tie_label.grid_forget()
    score_label.grid_forget()
    win_percentage_label.grid_forget()
    you_won_label.grid(row=4, column=2)
    score_label.grid(row=5, column=2)
    win_percentage_label.grid(row=6, column=2)


#set label to You lose
def lose():
    global win_percentage_label
    global you_won_label
    global you_lost_label
    global tie_label
    global score_label
    win_percentage = math.floor(score / number_of_games * 100)
    score_label = Label(window, text=f"score is {score}")
    win_percentage_label = Label(window, text=f"win percentage is {win_percentage}%")
    you_won_label.grid_forget()
    you_lost_label.grid_forget()
    tie_label.grid_forget()
    score_label.grid_forget()
    win_percentage_label.grid_forget()
    you_lost_label.grid(row=4, column=2)
    score_label.grid(row=5, column=2)
    win_percentage_label.grid(row=6, column=2)


#set label to tie
def tie():
    global win_percentage_label
    global score_label
    global you_won_label
    global you_lost_label
    global tie_label
    win_percentage = math.floor(score / number_of_games * 100)
    score_label = Label(window, text=f"score is {score}")
    win_percentage_label = Label(window, text=f"win percentage is {win_percentage}%")
    you_won_label.grid_forget()
    you_lost_label.grid_forget()
    tie_label.grid_forget()
    score_label.grid_forget()
    win_percentage_label.grid_forget()
    tie_label.grid(row=4, column=2)
    score_label.grid(row=5, column=2)
    win_percentage_label.grid(row=6, column=2)


#win detection
def submit():
    global player_choice,computer_choice,score, number_of_games, win_percentage, win_percentage_label, score_label
    if player_choice in possible_choices:
        number_of_games += 1
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
        
        #who chose what
        player_choice_label = Label(window, text="Player chose: " + player_choice)
        computer_choice_label = Label(window, text="Computer chose: " + computer_choice)
        player_choice_label.grid(row=3, column=1)
        computer_choice_label.grid(row=3, column=3)

        #reset choices
        player_choice = ""
        computer_choice = ""


# create window
window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("900x600")

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
score_label = Label(window, text=f"score is {score}")
win_percentage_label = Label(window, text=f"win percentage is {win_percentage}")



#configure grid layout
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
# window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.mainloop()
