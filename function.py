def won(user_choice, computer_choice):
    if (user_choice == 'p' and computer_choice == 'r') or (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p'):
        return True