import random
from function import won

def play():
    user_choice = input("Choose 'r' for rock 'p' for paper or 's' for scissor: ")
    computer_choice = random.choice(['r', 'p', 's'])
    #Game.won(user_choice, computer_choice)

    if user_choice == computer_choice:
        print("tie")
    elif won(user_choice, computer_choice):
        print("You won")
        
    elif not won(user_choice, computer_choice):
        print("You Lost")

while True:
    play()