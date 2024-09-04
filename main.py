import random

def RPC():
    user = input("'r' for rock, 'p' for paper, 's' for scissor ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        print("It's a tie!")
    elif is_win(user, computer):
        print('he hey, not bad!')
    else:
        print('Cupu Man!')
    
def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    
RPC()