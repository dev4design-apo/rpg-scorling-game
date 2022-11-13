"""
Created on Wed Oct 19 11:40:49 2022

@author: alipage-ouarti
"""
#####items---
from Inventory import Potion
####potions--
###healing potion-
##potion heal +
heal_low_potion = Potion("faible potion de soin", 10, 0)
#
##potion heal ++
heal_mid_potion = Potion("moyenne potion de soin", 20, 0)
#
##potion heal +++
heal_hight_potion = Potion("haute potion de soin", 50, 0)
###-
###defence potion-
##potion defence +
heal_low_potion = Potion("faible potion de défence", 0, 10)
#
##potion defence ++
heal_mid_potion = Potion("moyenne potion de défence", 0, 20)
#
##potion defence +++
heal_hight_potion = Potion("haute potion de défence", 0, 50)
###-
####weapons--
from Inventory import Weapon, Holy_sword, Corupted_sword
###basic sword
basic_sword = Weapon(name = "épee basique", attack=5)
###great sword
great_sword = Weapon(name = "grande épee", attack=10)
###holy sword
holy_sword = Holy_sword(name="épee sacré", attack=50)
holy_sword.holy_curse(False)
###dager
dagger = Weapon(name = "dague", attack=2)
###mass
mass = Weapon(name = "massue", attack=15)
####corupted sword
corupted_sword = Corupted_sword(name = "épe corompue", attack=25)
corupted_sword.demon_curse(False)
####staff
staff = Weapon(name = "staff", attack=20)
####--
####--
####armors--
from Inventory import Armor
###null armor
null_armor = Armor(name = "null armure", defence=0)
####--
###basic armor
basic_sword = Armor(name = "armure basique", defence=10)
####--
#####---

#####char---
from Character import Person, Knight, Holy_knight, Assassin, Orc
####kight--
knight = Knight(character="chevalier", health=100, attack=10, defence=10, money=30, lvl=1, villager_trust=1, weapon=basic_sword, armor=null_armor)
knight.weapon_aura(False)
####--
####holy kight--
holy_knight = Holy_knight(character="paladin", health=100, attack=25, defence=5, money=0, lvl=1, villager_trust=1, weapon=holy_sword, armor=null_armor)
holy_knight.god_protection
####--
####assasin--
assassin = Assassin(character="assasin", health=100, attack=30, defence=2, money=10, lvl=1, villager_trust=1, weapon=dagger, armor=null_armor)
assassin.hide(4)
####--
####npc orc--
npc_orc = Orc(character="orc", health=50, attack=15, defence=2, money=3, lvl=2, villager_trust=0, weapon=mass, armor=null_armor)
npc_orc.back_stab(5)
####--
####npc orc barbu--
npc_orc_barbu = Orc(character="orc barbu", health=75, attack=18, defence=1, money=5, lvl=3, villager_trust=0, weapon=mass, armor=null_armor)
npc_orc_barbu.back_stab(7)
####--
####npc corupted guardian--
npc_corupted_guardian = Person(character="gardien corompu", health=150, attack=22, defence=10, money=10, lvl=4, villager_trust=0, weapon=corupted_sword, armor=null_armor)
####--
####alchimiste--
alchimist = Person(character="alchimiste", health=75, attack=22, defence=10, money=10, lvl=4, villager_trust=0, weapon=staff, armor=null_armor)
####--
#####---


valid_class = "non"
while valid_class.lower() != "oui":
    char_select = int(input("\ntaper 1 pour s electionner la class chevalier, 2 pour l'alchimiste et 3 pour assasin : "))
    
    if (char_select == 1 ):
        print("\nce personnage peut utiliser une attaque special qui tue l'ennemie instantanement")
        valid_class = input("valider votre choix, entrer oui ou non : ")
        if valid_class.lower() == "oui":
            main_character = knight
            main_character.weapon = basic_sword
    """        
    if (char_select == 2 ):
        print("\nce personnage peut utiliser une protection divinne qui le rend invulnerable pendent 15s")
        valid_class = input("valider votre choix, entrer oui ou non : ")
        if valid_class.lower() == "oui":
            main_character = holy_knight
            main_character.weapon = holy_sword
    """
    if (char_select == 2 ):
        print("\nce personnage utilise la magie")
        valid_class = input("valider votre choix, entrer oui ou non : ")
        if valid_class.lower() == "oui":
            main_character = alchimist
            main_character.weapon = staff
            
    if (char_select == 3 ):
        print("\nce personnage peut cacher sa pressence et echapper a un enemie si le niveau de l enemie et egale ou inferieur a selui du joueur")
        valid_class = input("valider votre choix, entrer oui ou non : ")
        if valid_class.lower() == "oui":
            main_character = assassin
            main_character.weapon = dagger


if char_select==1:
    atq1= "brise côtes"
elif char_select==2:
    atq1= "lame divine"
elif char_select==3:
    atq1= "taillade furtive"

#from Inventory import Item
   
###############################################################################
###############################################################################
###############################################################################
#combats
def npc_orc_combat():
    print ("\nchoisissez votre attaque, tapper 1 pour l'ataquer avec", atq1, "et 2 un coup de poing")
    choix2 = int(input("votre choix:"))
    if choix2 == 1:
        opponent.health-= main_character.attack + main_character.weapon.attack
        print("\nvous donnez un coup de", main_character.weapon.name, "à l'orc")
    if choix2 == 2:
        opponent.health-= main_character.attack
        print("\nvous donnez un coup de poign à l'orc")
    if opponent.health > 0:
        main_character.health-= opponent.attack
        print("\nl'orc vous donne ensuite un violent coup de massue. vous perdez 15 points de vie")
    if opponent.health <= 0:
        print("\nbravo!+ 3 pieces!")
        main_character.money+= opponent.money
        main_character.villager_trust+= 6
###############################################################################
###############################################################################
#villes
def premiere_ville():
    print("\naprès quelques heures de marche, vous arrivez dans une ville au frontieres du dommaine du sorcier démoniaque")
    print("\nen tant que zone tampon avec le pays de l'ennemi, des patrouilles de soldats armés jusqu'au dents font des rondes frequemment")
    print("\nil ne vaudrait mieux ne pas déclencher de conflit")
    print("\nvoulez vous retrer dans le village?")
    choix4 = int(input("\nretrer oui pour retrer dans le village et non pour continuer vottre route"))
    if choix4 == "oui":
        print("\nvous arrivez sur la place du marché. Un marchand d'arme se tient sur la place.Il vous interpelle:'Hé Noble chevalier!voulez-vous acheter quelque chose'")
        print("\n1 pour voir sa marchandise et 2 pour le frapper et voler la caisse")
        choix5 = int(input("que faites vous?:"))
        if choix5 == 1 :
            print("\nle marchand vous montre ses articles:")
        if choix5 == 2:
            print("\nvous commencez à menacer le marchand avec votre épée mais soudain, une patrouille débarque.")
"""
            choix6 = int(input("tapper 1 pour les attaquer, et tapper 2 pour s'enfuire que faites vous?:"))
                if choix6 == 1 :
                    #combat contre les soldata
                    #victoire
                    #Vous mourrez dans la mélée
                if choix6 == 2:
                        #fuite du joueur
            
    if choix4 == "non":
        #vous continuer votre route jusque au terrain de chasse
"""
###############################################################################
###############################################################################

print("\nvous êtes un",main_character.character, "du royaume de machintrucland, allez sauver la princesse du royaume des griffes du sorcier démoniaque")
print("\nmettez 1 pour une belle armure, 2 pour une bourse remplie de pieces")
a = int(input("choisissez:"))
if a == 1:
    main_character.health += 10
    print("vous avez ressu une armure basic") 
elif a == 2:
    main_character.money += 5
    print("+ 5 pieces d'or!")
    
    
print("\nvous vous mettez en marche vers le royaume du perfide sorcier. Mais un orc vous barre la route")
opponent = npc_orc
print("\n1 pour l'attaquer, ou 2 pour tenter une fuite")
choix1 = int(input("\nquel est votre choix?"))
if choix1 == 1:       
    print("\nl'orc vous apperçoit au loin et commence à courrir vers vous. Le combat commence.")
    while opponent.health > 0:
        npc_orc_combat()
    if choix1 == 2:
        if (main_character.hide >= opponent.lvl):
            print("\nvous vous faufillez discrétement derreire l'orc et réussissez à fuire")
        else:
            if opponent.health > 0:
                main_character.health-= opponent.attack + opponent.back_stab
                print("\nl'orc vous donne un violent coup de massue. vous perdez 20 points de vie")
                npc_orc_combat()


print("vous continuez votre route et appersever un paysan courent dans votre direction.")
choix3 = int(input("\nvoulez vous approchez de lui, oui ou non"))
if choix3 == "oui":
    if (main_character.villager_trust >= 5):
        print("vous avez tué l'orc! vous avez sauvé le village! Prenez ces pieces en guise de remerciement")
        main_character.money+=10
        print("argent+ 10")
        premiere_ville()
    else:
        print("hé espece de chomeur! je t'ai vu esquivé l'orc! Tu n'est qu'un poltron! Casse toi!")
        print("vous continuez votre route chassé à coup de bâtons les villageois attirées par les clameur du paysant")
        main_character.health-=20
        print("vous perdez 20 points de vie")
        premiere_ville()
if choix3 == "non":
    premiere_ville()

  ## boire = heal_low_potion.boire()