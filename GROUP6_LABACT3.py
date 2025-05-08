from abc import ABC, abstractmethod 

class GameCharacter(ABC):
    def __init__(self, name, level, health, mana, defense,damage_type, attack_power):
        self.name = name
        self.level = level
        self.health = health
        self.mana = mana
        self.defense = defense
        self.damage_type = damage_type
        self.attack_power = attack_power

    def show_stats(self):
        print(f"{self.name} is level {self.level}. ")
        print(f"{self.name} has {self.health} hp.")
        print(f"{self.name} has {self.mana} mana.")
        print(f"{self.name} has {self.defense} armor.")
        print(f"{self.name} has {self.attack_power} {self.damage_type} attack.")

    def move(self):
        print(f"{self.name} moves.")


    def attack(self):
        print(f"{self.name} attacks.")


    def defend(self):
        print(f"{self.name} defends.")


    @abstractmethod
    def perform_special(self):
        pass


    @abstractmethod
    def character_type(self):
        pass

class Tank(GameCharacter):
     def __init__(self, name, level, health, mana, defense,damage_type, attack_power, shield, cc_reduction):
        super().__init__(name, level, health, mana, defense,damage_type, attack_power)
        self.shield = shield
        self.cc_reduction = cc_reduction
    
     def show_stats(self):
        print(f"{self.name} is level {self.level}. ")
        print(f"{self.name} has {self.health} hp.")
        print(f"{self.name} has {self.mana} mana.")
        print(f"{self.name} has {self.defense} armor.")
        print(f"{self.name} has {self.attack_power} {self.damage_type} attack.")
        print(f"{self.name} has {self.shield} shield.")
        print(f"{self.name} has {self.cc_reduction} CC reduction.")
        
        
     def perform_special(self):
         print(f"{self.name} performs a Taunt to draw enemy attention!")
    
     def gain_shield(self):
         print(f"{self.name} gains a shield.")

     def block(self):
         print(f"{self.name} blocks an attack")

     def character_type(self):
         print(f"{self.name} is a Tank.")



#Assassin
class Assassin(GameCharacter):
     def __init__(self, name, level, health, mana, defense,damage_type, attack_power, crit_rate, crit_damage):
        super().__init__(name, level, health, mana, defense,damage_type, attack_power)
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
    
     def show_stats(self):
        print(f"{self.name} is level {self.level}. ")
        print(f"{self.name} has {self.health} hp.")
        print(f"{self.name} has {self.mana} mana.")
        print(f"{self.name} has {self.defense} armor.")
        print(f"{self.name} has {self.attack_power} {self.damage_type} attack.")
        print(f"{self.name} has {self.crit_rate} Crit Rate.")
        print(f"{self.name} has {self.crit_damage} Crit Damage.")

     def perform_special(self):
        print(f"{self.name} performs a deadly sneak attack!")


     def sneak(self):
        print(f"{self.name} sneaks behind enemies for a surprise strike.")


     def vanish(self):
        print(f"{self.name} vanishes to escape or reposition.")


     def character_type(self):
        print(f"{self.name} is an Assassin.")

#Fighter
class Fighter(GameCharacter):
    def __init__(self, name, level, health, mana, defense,damage_type, attack_power, rage,life_steal):
        super().__init__(name, level, health, mana, defense,damage_type, attack_power)
        self.rage = rage
        self.life_steal = life_steal
    
    def show_stats(self):
        print(f"{self.name} is level {self.level}. ")
        print(f"{self.name} has {self.health} hp.")
        print(f"{self.name} has {self.mana} mana.")
        print(f"{self.name} has {self.defense} armor.")
        print(f"{self.name} has {self.attack_power} {self.damage_type} attack.")
        print(f"{self.name} has {self.rage} rage.")
        print(f"{self.name} has {self.life_steal} Lifesteal.")

    def perform_special(self):
        print(f"{self.name} enters rage mode and increases attack!")


    def combo(self):
        print(f"{self.name} executes a devastating combo.")


    def throw(self):
        print(f"{self.name} throws the enemy!")


    def character_type(self):
        print(f"{self.name} is a Fighter.")


#Mage
class Mage(GameCharacter):
    def __init__(self, name, level, health, mana, defense,damage_type, attack_power, mana_regen, magic_crit):
        super().__init__(name, level, health, mana, defense,damage_type, attack_power)
        self.magic_crit = magic_crit
        self.mana_regen = mana_regen

    def show_stats(self):
        print(f"{self.name} is level {self.level}. ")
        print(f"{self.name} has {self.health} hp.")
        print(f"{self.name} has {self.mana} mana.")
        print(f"{self.name} has {self.defense} armor.")
        print(f"{self.name} has {self.attack_power} {self.damage_type} attack.")
        print(f"{self.name} has {self.magic_crit} magic crit.")
        print(f"{self.name} has {self.mana_regen} mana regen.")

    def perform_special(self):
        print(f"{self.name} casts a powerful AoE (Area of Effect) spell!")


    def cast(self):
        print(f"{self.name} casts a damaging spell.")


    def burst(self):
        print(f"{self.name} releases a burst of magical energy.")


    def character_type(self):
        print(f"{self.name} is a Mage.")

# Marksman
class Marksman(GameCharacter):
    def __init__(self, name, level, health, mana, defense,damage_type, attack_power, range, penetration):
        super().__init__(name, level, health, mana, defense,damage_type, attack_power)
        self.range = range
        self.penetration = penetration

    def show_stats(self):
        print(f"{self.name} is level {self.level}. ")
        print(f"{self.name} has {self.health} hp.")
        print(f"{self.name} has {self.mana} mana.")
        print(f"{self.name} has {self.defense} armor.")
        print(f"{self.name} has {self.attack_power} {self.damage_type} attack.")
        print(f"{self.name} has {self.range} range.")
        print(f"{self.name} has {self.penetration} penetration.")

    def perform_special(self):
        print(f"{self.name} performs a long-range precision shot!")


    def shoot(self):
        print(f"{self.name} shoots a powerful arrow.")


    def snipe(self):
        print(f"{self.name} snipes enemies from a great distance.")


    def character_type(self):
        print(f"{self.name} is a Marksman.")

# Support
class Support(GameCharacter):
    def __init__(self, name, level, health, mana, defense,damage_type, attack_power, healing, buff_rate):
        super().__init__(name, level, health, mana, defense,damage_type, attack_power)
        self.healing = healing
        self.buff_rate = buff_rate

    def show_stats(self):
        print(f"{self.name} is level {self.level}. ")
        print(f"{self.name} has {self.health} hp.")
        print(f"{self.name} has {self.mana} mana.")
        print(f"{self.name} has {self.defense} armor.")
        print(f"{self.name} has {self.attack_power} {self.damage_type} attack.")
        print(f"{self.name} has {self.healing} healing.")
        print(f"{self.name} has {self.buff_rate} buff rate.")

    def perform_special(self):
        print(f"{self.name} performs a healing boost to the team!")


    def heal(self):
        print(f"{self.name} heals an ally.")


    def boost(self):
        print(f"{self.name} boosts allies' stats for a short duration.")


    def character_type(self):
        print(f"{self.name} is a Support.")        




# Header eme
print("These game characters are based in Mobile Legends Bang Bang.\n")


# Example, not sure sa mga other infos na ilagay like mana etc HAHHAHA
tank = Tank(name="Tigreal", level=10, health=3000, mana=200, defense = 300, damage_type="Physical", attack_power=100, shield=150, cc_reduction="50%")
fighter = Fighter(name="Leomord", level=8, health=2500, mana=150, defense=150, damage_type="Physical", attack_power=250, rage="0", life_steal="25%")
assassin = Assassin(name="Ling", level=9, health=1900, mana=180, defense= 100, damage_type="Physical", attack_power=500, crit_rate="35%", crit_damage="200%")
mage = Mage(name="Lylia", level=7, health=2100, mana=250, defense=130, damage_type= "Magic", attack_power= 350, mana_regen="120%", magic_crit="40%")
marksman = Marksman(name="Miya", level=6, health=1800, mana=100, defense=100, damage_type="Physical", attack_power= 300, range="120%", penetration="150%")
support = Support(name="Rafaela", level=5, health=1800, mana=150, defense=130, damage_type="Magic", attack_power=100, healing="120%", buff_rate="70%")

print("\n\n\n1.Showcase Characters \n2.Simulate battle\n3.Exit")
while True:
    choice = input("Choose(1/2/3):")
    if choice == "1":
        print("Tank:")
        tank.character_type()
        tank.show_stats()
        print("\n\n")
        print("Fighter: ")
        fighter.character_type()
        fighter.show_stats()
        print("\n\n")
        print("Assassin: ")
        assassin.character_type()
        assassin.show_stats()
        print("\n\n")
        print("Mage: ")
        mage.character_type()
        mage.show_stats()
        print("\n\n")
        print("Marksman: ")
        marksman.character_type()
        marksman.show_stats()
        print("\n\n")
        print("Support: ")
        support.character_type()
        support.show_stats()
        print("\n\n")
    elif choice == '2':
        tank.move()
        tank.gain_shield()
        support.boost()
        tank.perform_special()
        fighter.attack()
        fighter.throw()
        assassin.sneak()
        mage.cast()
        marksman.shoot()
        tank.block()
        fighter.combo()
        marksman.perform_special()
        assassin.perform_special()
        assassin.vanish()
        support.heal()
        support.perform_special()
        mage.burst()
        fighter.perform_special()
        fighter.attack()
    elif choice == '3':
        print("VICTORY! See you next time!")
        break
    else:
        print("Please choose only within the options.")
