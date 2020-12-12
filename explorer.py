from game_character import GameCharacter

#Explorer class is a sub class from super class GameCharacter
class Explorer(GameCharacter):          
     # Call __init__() method for the Explorer object
    def __init__(self, name, health, attack_max, magic):  
        super().__init__(name, health, attack_max, magic)  # Call super().__init__() function

        self.gold=0      #Represents the amount of gold the explorer successfully managed to find,Default value is 0.
        self.foresight =1 #value between 1-3 representing the foresight level for the explorer, Default value is 1. 

        print(f"Commander '{self.name}' at your service.")
    
    def set_gold(self, gold): 
        """ this function assign value for gold variable when the gold value is less than zero the gold value=0
        and otherwise the gold value equal gold"""      
        if gold<0:
            self.gold=0
        else:
            self.gold = gold

    def get_gold(self):
        """ this function return gold value """
        return self.gold
    
    def set_foresight(self, foresight):
        """ this function assign value for foresight variable when the foresight value is greater than 3 the foresight
        value=3 ,when the foresight value less than 1 the foresight vaule=1, and otherwise the foresight value
        equal new foresight""" 

        new_foresight=self.foresight +int(foresight)
        
        if new_foresight >3:
            self.foresight=3
        elif new_foresight <1:
            self.foresight=1
        else:
            self.foresight = new_foresight

    def get_foresight(self):
        """ this function return foresight value """
        return self.foresight

    def go_on_quest(self,map, position):
        """This method receives a random map on which the explorer is placed on a position, randomly.
        The explorer can move to explore other locations on the map,given that the number of steps an explorer
        can move in any direction is equal or less than their foresight level. After returning from a quest,
        the explorer loses one foresight level."""

        gold_count=0  # this variable count the gold in the map.

        for x in range(position[0]-self.foresight ,position[0]+self.foresight+1):     # to move in column of map. 
            for y in range(position[1]-self.foresight,position[1]+self.foresight+1): # to move in row of map.
                if x in range(0,4) and y in range(0,4):   # to ignore incorrect position.
                    if map[y][x]=='$':                    #if the position in map =$ the gold_count increase by one.
                        gold_count+=1       
        
        self.set_foresight(-1)                   #After returning from a quest, the explorer loses one foresight level.
        self.set_gold(gold_count+self.get_gold())                        #add gold_count value.
        print (f'{self.name} get {gold_count} golds')

    def improve_foresight(self):
        """ this is function improve foresight level of explorer by 1 opposite 5 gold """
        if self.gold >= 5:
            self.set_foresight(1)
            self.gold-=5
            print("awesome, you are improve your foresight")
        else:
            print("you does not having enough gold to improve your foresight")    
        




