#Ben Shade
#this is ment to play a game of rock paper sisscors

import random

hand = random.randrange(3)

enemy = input("Which do you play, rock ? paper ? or scissors ? please lower case ")
#rock is 0 paper is 1 scissors is 2
if enemy == "paper" and hand == 1 or enemy == "rock" and hand == 0 or enemy == "scissors" and hand == 2 :
    print("ITS A TIE!!!!!!!!!!!!!!!!!!!!!!!!")
    elif enemy == "paper" and hand == 1:
        print("the computer played paper")
    elif enemy == "rock" and hand == 0 :
        print("the computer played rock")
    elif enemy == "scissors" and hand == 2 :
        print("teh computer played scissors")


elif enemy == "paper" and hand == 2 or enemy == "rock" and hand == 1 or enemy == "scissors" and hand == 0 :
    print("the computer beats you this round...")
    elif enemy == "paper" and hand == 2 :
        print("the computer played scissors")
    elif enemy == "rock" and hand == 1 :
        print("the computer played paper")
    elif enemy == "scissors" and hand == 0 :
        print("the computer played rock")


elif enemy == "paper" and hand == 0 or enemy == "rock" and hand == 2 or enemy == "scissors" and hand == 1 :
    print("The computer staggers away in defeat")
    elif enemy == "paper" and hand == 0 :
        print("the computer played rock")
    elif enemy == "rock" and hand == 2 :
        print("The computer played scissors")
    elif enemy == "scissors" and hand == 1 :
        print("the computer played paper")


else:
    print("what caused you to put THAT you gremlin")

input("\n\nPress enter to exit")
    

