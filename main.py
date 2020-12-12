from explorer import Explorer
from medic import Medic
from warrior import Warrior
import datetime 
import random

def creat_team(tnum):
    """ this function create team of three character Warrior,Medic and Explorer"""

    w=Warrior(f"w{tnum}",100,100,100) # create Warrior character.
    m=Medic(f"m{tnum}",100,100,100)   # create Medic character.
    e=Explorer(f"e{tnum}",100,100,100) # create Explorer character.

    return w,m,e   

def choose_opponent(teams,team_round,playr):
    """this function allow player to choose one player from the opponent team"""

    print("which opponent you want to cast spell on it?")
    if team_round==0:      #determine opponent team
        opp=1
    else:
        opp=0
    for i in range(0,3):
        print(f"{i}:{teams[opp][i].name}") #print opponent team
    att=int(input("Choose opponent:"))
    return teams[opp][att]

def choose_member(teams,team_round,playr):
    """this function allow player to choose  player from his team"""

    print("which member you want to cast spell on it?")
    for i in range(0,3):
        print(f"{i}:{teams[team_round][i].name}") #print member team
    mem=int(input("Choose member:"))
    return teams[team_round][mem]

def attack_action(teams,team_round,playr):
    """ this function perform attack to opponent team"""
    opp=choose_opponent(teams,team_round,playr)
    teams[team_round][playr].attack(opp) #use cureent character to attack choosen opponent 

def cast_spell_action(teams,team_round,playr):
    """ this is function cast spell on opponent team"""
    opp=choose_opponent(teams,team_round,playr)
    teams[team_round][playr].cast_spell_on(opp) #use cureent character to cast spell on choosen opponent 

def w_action(teams,team_round,playr):
    """This function allow worrior to choose one of his actions """

    print("3:buy armor - buy armorfor a member of the team")
    print("4:share intelligence- share intelligence with the Explorer")
    print("5:improve strength- improve strength of warrior")

    chosen_action=int(input("Choos action:"))

    if chosen_action==1:
        attack_action(teams,team_round,playr)
    elif chosen_action==2:
        cast_spell_action(teams,team_round,playr)
    elif chosen_action==3:
        buy_armer_action(teams,team_round,playr)
    elif chosen_action==4:
        share_intelligence_action(teams,team_round,playr)
    elif chosen_action==5:
        improve_strength(teams,team_round,playr)

def buy_armer_action(teams,team_round,playr):
    """ this function allow warrior to choose one of his team to buy armer for it """
    mem=choose_member(teams,team_round,playr)
    teams[team_round][playr].buy_armor(5,mem,teams[team_round][2])

def share_intelligence_action(teams,team_round,playr):
    """ this function execute share intelligence function"""
    teams[team_round][playr].share_intelligence(teams[team_round][2])

def improve_strength(teams,team_round,playr):
    """ this function execute improve strength function """
    teams[team_round][playr].improve_strength(teams[team_round][2])

def m_action(teams,team_round,playr):
    """This function allow medic to choose one of his actions"""

    print("3:heal")
    print("4:back_to_the_future")
    print("5:improve_magic")
    chosen_action=int(input("Choos action:"))

    if chosen_action==1:
        attack_action(teams,team_round,playr)
    elif chosen_action==2:
        cast_spell_action(teams,team_round,playr)
    elif chosen_action==3:
        heal_action(teams,team_round,playr)
    elif chosen_action==4:
        back_to_the_future_action(teams,team_round,playr)
    elif chosen_action==5:
        improve_magic_action(teams,team_round,playr) 

def heal_action(teams,team_round,playr):
    """this function allow medic to choose one member of his team to execute heal function on it"""
    mem=choose_member(teams,team_round,playr)
    teams[team_round][playr].heal(mem)

def back_to_the_future_action(teams,team_round,playr):
    """this function get current time and add  second to current time and then call back to the future function"""
    cur_time = datetime.datetime.now()                          # get current time
    fut_time = cur_time + datetime.timedelta(seconds=1) #add 1 second to current time 
    teams[team_round][playr].back_to_the_future(fut_time)       #call back to futuer function

def improve_magic_action(teams,team_round,playr):
    """this function allow medic to choose one member of his team to improve magic of it """
    mem=choose_member(teams,team_round,playr)
    teams[team_round][playr].improve_magic(mem)

def e_action(teams,team_round,playr):
    """This function allow explorer to choose one of his actions"""
    
    print("3:go_on_quest")
    print("4:improve_foresight")
    chosen_action=int(input("Choos action:"))

    if chosen_action==1:
        attack_action(teams,team_round,playr)
    elif chosen_action==2:
        cast_spell_action(teams,team_round,playr)
    elif chosen_action==3:
        go_on_quest_action(teams,team_round,playr)
    elif chosen_action==4:
        improve_foresight_action(teams,team_round,playr)

def go_on_quest_action(teams,team_round,playr):
    map=get_map()
    x=random.randrange(0,4)
    y=random.randrange(0,4)
    teams[team_round][playr].go_on_quest(map,(x,y))
    
def get_map():
    path='C:/Users/user/Desktop/python/PA3/treasure_maps_new.txt' #set file path
    
    maps=[]
    my_file = open(path, "r")

    content = my_file.read()
    all_maps=content.split("\n,")
    for map in all_maps:
        x=[]
        amap=map[2:-3].replace(" ","").split(',\n')
        for row in amap:
            y=[]
            arow=row[1:-1].split(',')
            for poss in arow:
                y.append(poss[1])
            x.append(y)
        maps.append((x))
    rand_map=random.randrange(0,len(maps)+1)  
    return maps[rand_map]



def improve_foresight_action(teams,team_round,playr):
    """this function execute improve foresight function """
    teams[team_round][playr].improve_foresight()


def run_game(teams):
    team_round=0   #first round start with team1.
    chosen_char=1  

    while(chosen_char !=-1):  
        print(f"Team {team_round+1} Wich character do you wish to choose for this round?")
        for i in range(0,3):   
            print(f"{i}:{teams[team_round][i].name}")   #display characters of team who has the round
        
        chosen_char=int(input("Choose character:"))
        print(f"you have choosen {teams[team_round][chosen_char].name} to play this round.")
        print(f"{teams[team_round][chosen_char].name} Can do the following:")

        print("1:attack - attacks an enemy character")
        print("2:cast spell - casts a spell on an enemy character")

        if chosen_char==0:
            w_action(teams,team_round,chosen_char)
        elif chosen_char==1:
            m_action(teams,team_round,chosen_char)
        elif chosen_char==2:
            e_action(teams,team_round,chosen_char)
        
        if team_round==0:
            team_round=1
        else:
            team_round=0
        print("************")

            
        
if __name__ == "__main__":
    
    print("A new BOT game has been started.")

    teams=(creat_team(1),creat_team(2))   #create tuple of tow tuples each one contain team characters.
    run_game(teams)
    print(teams[0][0].name)



