def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "pls,check the word "

def number_to_name(number):
    """
    Take a number as input(0-1-2-3-4) and return string
    (rock-Spock-paper-lizard-scissor)
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "pls,chek ur number"
    
    
def rpsls(player_choice):
    print ('\n')
    print("player choose ",player_choice)
    player_number = name_to_number(player_choice)
    import random
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("computer choose ",comp_choice)
    diff = (comp_number - player_number) %5
    
    if diff ==3 or diff==4:
        print("Player wins!")
        
    elif diff ==1 or diff ==2:
        print("Computer wins!")
        
    else:
        print("Player and Computer tie!")
    
    
    
print("enter ur choice (rock/Spock/paper/lizard/scissors): ")
choice=input()
rpsls(choice)
