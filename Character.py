# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:22:39 2022

@author: alipage-ouarti
"""

class Person():
    def __init__(self, character, health, attack, defence, money, lvl, villager_trust, weapon, armor):
        self.character = character
        self.health = health
        self.attack = attack
        self.defence = defence
        self.money = money
        self.lvl = lvl
        self.villager_trust = villager_trust


class Knight(Person):
    def weapon_aura(self, aura):
        self.aura = aura
        
        
class Holy_knight(Person):
    def god_protection(self, protection):
        self.protection = protection
        
        
class Assassin(Person):
    def hide(self, hiding):
        self.hiding = hiding


class Orc(Person):
    def back_stab(self, stab):
        self.stab = stab
