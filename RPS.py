import random
import sys
def start():
    ai_=("rock","paper","scissors")
    comp = random.choice(ai_)
    Pscore = 0
    Cscore = 0
    print("you know the rules. \n")
    for k in range(0, 3):
        comp = random.choice(ai_)
        player = input("enter either |ROCK|PAPER|SCISSORS|:")
        if player == comp:
            print("you chose "+player+" and the comp chose "+comp)
            print("its a tie \n")
    #loss
        if comp == "rock" and player == "scissors":

            print("you chose "+player+" and the comp chose "+comp)
            print("And you lost that one \n")
            Cscore +=1

        if comp == "scissors" and player == "paper":

            print("you chose "+player+" and the comp chose "+comp)
            print("And you lost that one \n")
            Cscore +=1

        if comp == "paper" and player == "rock":

            print("you chose "+player+" and the comp chose "+comp)
            print("And you lost that one \n")
            Cscore +=1
    #win
        if comp == "paper" and player == "scissors":

            print("you chose "+player+" and the comp chose "+comp)
            print("and thats one for you \n")
            Pscore -= 1
            
        if comp == "scissors" and player == "rock":

            print("you chose "+player+" and the comp chose "+comp)
            print("and thats one for you \n")
            Pscore -= 1
        
            
        if comp == "rock" and player == "paper":
    
            print("you chose "+player+" and the comp chose "+comp)
            print("and thats one for you \n")
            Pscore -= 1
    #if Csore and Pscore == the same then tis a tie and not a loss
    # fix the numbering system | shouldnt go below 0
            
    print("the comp got "+str(Cscore)+" and you got "+str(Pscore))
    if Cscore < Pscore:
        print("You won the game")
    else:
        print("unlucky, you lost the game")

    reStart = input("Would you like to play again? \n")
    if reStart == "yes" or "y":
        cout = 3
        while cout < 1:
            cout -=1
            print(cout)
        if cout == 0:
            start()
    elif reStart == "no" or "n":
        print("oh ok...well...goodbye I guess")
        sys.exit()
        
start()
    
        

