from game_character import GameCharacter
import datetime 
import random

class Medic(GameCharacter):                            #Medic class is a sub class from super class GameCharacter.

    def __init__(self, name, health, heal, magic):     #Call __init__() method for the Medic object.

        super().__init__(name, health, heal, magic)    # Call super().__init__() function.
        
        self.nanobots=10                #represents the number of nanobots available for the medic to use,defaults is 10.
        self.nanobots_accuracy_level=0  #represents the level of accuracy for the nanobots,defaults is 0.

        print(f"Your medic {self.name}, to the rescue!")

    def heal(self, character):
        #heal value eqale random number between 10%-90% of nanobots
        heal_value = (random.randrange(int(self.nanobots * 0.1) , int(self.nanobots + 0.9))) 
       
        if character.get_health() + heal_value > character.max_health:
            heal_value=character.max_health - character.get_health()   #Actual value added for the character
            character.set_health(100)
        else:
            character.set_health(character.get_health() + heal_value)
         
        print(f"> {self.name} is healing {character.name}. {(heal_value)}")
        self.nanobots-=heal_value   #nanobots value decreases by heal_value 
        return heal_value
    
    def attack(self, character):
        self.heal(character)
    
    def back_to_the_future(self,ftime):
        """This method receives a date and a time in the future. The medic travels in time to retrieve advanced nanobots
        that help the medic heal other characters more efficiently. The number of nanobots returned with our medic after
        every trip to the future is equal to the microseconds difference between our time in the future and now.
        Every time the medic takes a trip back in time, the nanobots_accuracy_level increases by 1."""
        
        current_time = datetime.datetime.now()  #get current time.
        diff=ftime- current_time                #difference between current time and future time.
        self.nanobots_accuracy_level+=1         #the nanobots_accuracy_level increases by 1.

        # """ convert difference between current time and future time to second and then convert it to microsecond
        # and add the value nanobots of medic. """
        self.nanobots += diff.total_seconds()*1000000  
        print (f'{self.name} get{diff.total_seconds()*1000000} from the future ')  

    def improve_magic(self, character):
        """ this is function improve magic value of character by random number between 10%-50% of nanobots """
        #heal value eqale random number between 10%-50% of nanobots
        magic_value = (random.randrange(int(self.nanobots * 0.1) , int(self.nanobots + 0.5))) 
       
        if character.magic + magic_value > 100:
            magic_value=100-character.magic    #Actual value added to the character magic.
            character.magic=100                #set character magic value to maximum value(100).
        else:
            character.magic+=magic_value
         
        print(f"> {self.name} is improve magic of {character.name}. {(magic_value)}")
        self.nanobots-=magic_value   #nanobots value decreases by magic_value 
        return magic_value

