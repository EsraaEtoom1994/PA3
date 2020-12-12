from game_character import GameCharacter
import random

class Warrior(GameCharacter):                         # Warrior class is a sub class from super class GameCharacter.

    def __init__(self, name, health, attack_max, magic):    # Call __init__() method for the Warrior object.

        super().__init__(name, health, attack_max, magic)   # Call super().__init__() function
        self.popularity =0

        print(f"{self.name} is ready to fight!")

    def buy_armor(self,gold, member,explorer):
        """This method receives gold and a member as input. The warrior then issues a command to buy armor for that
        team member. A random shield value between 0% - 20% is returned.This random shield value is added 
        to the health value for that team member.This also increases the warriors popularity level by the same amount."""
        
        if explorer.get_gold() < gold:
            print("you dont have enough gold")
            return

        shield_value = random.randrange(0,20)   #shield value is a random between 0% - 20%.
        
        if member.get_health() + shield_value > member.max_health:
            member.set_health(100)
        else:
            member.set_health(member.get_health() + shield_value)

        explorer.set_gold(explorer.get_gold()-gold)   #decreases gold value of explorer
        self.popularity +=shield_value

    def share_intelligence(self,explorer):
        """This method increases the explorer's foresight level by 1/10th of the warrior's popularity level."""
        shared_val=self.popularity/10
        explorer.set_foresight(shared_val)
        print(f"increases the {explorer.name} foresight level")

    def improve_strength(self,explorer):
        """ this is function improve strength value of warrior by 5 opposite 1 of gold """
        spend_gold=int(input(print("How much of gold do you want to spend to improve strength???")))

        if spend_gold > explorer.get_gold():
            spend_gold=explorer.get_gold()
        if spend_gold * 5 +self.get_strength()>100:
            spend_gold=(self.strength-spend_gold*5)/5 

        self.set_strength(spend_gold*5 + self.get_strength())
        explorer.set_gold(explorer.get_gold()-spend_gold)      
        print(f"improve strength of {self.name} ")
            