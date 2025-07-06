import random

options = ["rock","paper","scissors"]



def get_choices():
    player_choice = input("select R P S : ")
    com_choice = random.choice(options)

    choices = {"c_player":player_choice,"c_com":com_choice}


    return choices

inputs = get_choices()

player = inputs["c_player"]
com = inputs["c_com"]

def check_winner(player,com):
    print (f"you chose {player} and computer chose {com}")

    if player == com :
        return "tie"
    
    elif player =="rock" :
        if com == "paper":
            return "you loose"
        else :
            return "you won"
    
    elif player =="paper" :
        if com == "rock":
            return "you won"
        else :
            return "you loose"
    
    elif player =="scissors" :
        if com == "paper":
            return "you won"
        else :
            return "you loose"
    


print (check_winner(player,com))
