# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:11:16 2022

@author: alipage-ouarti
"""

class Potion():
    def __init__(self, name, heal, defence):
        self.name = name
        self.heal = heal
        self.defence = defence  
    def boire(self):
        heal=self.heal
        self.heal=0
        return heal
    


class Weapon():
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
class Holy_sword(Weapon):
    def holy_curse(self, curse):
        self.curse = curse
class Corupted_sword(Weapon):
    def demon_curse(self, curse):
        self.curse = curse



class Armor():
    def __init__(self, name, defence):
        self.name = name
        self.defence = defence
"""
class Item():
    def __init__(self):
        #weapons
        self.basic_sword = 0
        self.long_sword = 0
        self.holy_sword = 0
        self.Dagger = 0
        self.mass = 0
        #potions
        self.heal_low_potion = 0
        self.heal_mid_potion = 0
        self.heal_hight_potion = 0
        self.defence_low_potion = 0
        self.defence_mid_potion = 0
        self.defence_hight_potion = 0
        #armors
        self.null_armor = 0
        self.basic_amor = 0
    def ChangeItem(number, name):
        #weapon
        if (name == "épee basique"):
            self.basic_sword += number
        elif (name == "grande épee"):
            self.long_sword += number
        elif (name == "épee sacré"):
            self.long_sword += number
        elif (name == "dague"):
            self.long_sword += number
        elif (name == "massue"):
            self.long_sword += number
        #potions
        if (name == "faible potion de soin"):
            self.heal_low_potion += number
        elif (name == "moyenne potion de soin"):
            self.heal_mid_potion += number
        elif (name == "haute potion de soin"):
            self.heal_higth_potion += number
        elif (name == "faible potion de défence"):
            self.defence_low_potion += number
        elif (name == "moyenne potion de défence"):
            self.defence_mid_potion += number
        elif (name == "haute potion de défence"):
            self.defence_hight_potion += number
        #armors
        if (name == "null armure):
            self.null_armor += number
        elif (name == "armure basique"):
            self.basic_amor += number
"""