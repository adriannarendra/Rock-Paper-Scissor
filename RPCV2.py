import random
import time

def RockPaperScissor():
    while True:
        computer = random.choice(["r", "p", "s"])
        
        def response(computer):
            if computer == "r":
                return "ROCK!"
            elif computer == "p":
                return "PAPER!"
            else:
                return "SCISSOR!"
            
        player = input("(R) rock  (P) paper  (S) scissor: ").lower()
        print()
        
        print("Computer: I choose...", end="", flush=True)
        time.sleep(2)
        print(f" {response(computer)}")
        print()  
        
        if computer == player:
            print("It's a Tie!")
        elif is_win(player, computer):
            print("You Won!")
        else:
            print("Computer Won!")
            
        print()
        
        play_again = input("Play again? (Y) Yes  (N) NO: ").lower()
        if play_again == 'y':
            continue
        else:
            break
        
def is_win(p1, p2):
    if p1 == 'r' and p2 == 's' or p1 == 'p' and p2 == 'r' or p1 == 's' and p2 == 'p':
        return True
    
RockPaperScissor()