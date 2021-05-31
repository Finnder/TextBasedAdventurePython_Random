import sys
import time
import random
from colorama import init
from colorama import Fore, Back, Style
import pyttsx3
import pickle
import os

speechEngine = pyttsx3.init()

# Colorama init
init(autoreset=True)

XpGainPerEnemy = 10

def OnKillEnemyCoinGain(min, max):
    return random.randint(min, max)
    

Damage = 0
XP = 0
MaxXP = 0
Kit = " "
Health = 0
MaxHealth = 0
Level = 0
Name = ""
Coin = 0

speechEngineActive = False

class create_new_Player:
    def __init__(self, Name, Health, MaxHealth, Mana, Kit, Level, XP, MaxXP, Damage, Coin):
        self.Name = Name
        self.Health = Health
        self.MaxHealth = MaxHealth
        self.Mana = Mana
        self.Kit = Kit
        self.Level = Level
        self.XP = XP
        self.MaxXP = MaxXP
        self.Damage = Damage
        self.Coin = Coin

def rng(min, max):
    x = random.randint(min, max)
    return x

def new_Player():
    global Name
    global Level
    global Health
    global MaxHealth
    global Kit
    global Mana
    global XP
    global MaxXP
    global Damage
    global Coin

    try:
        # Initial Values
        Name = input(" Enter Your New Characters Name: ")
        Level = 1
        XP = 0
        MaxXP = 100

        print(Fore.GREEN + "-- Choose A Class | Guardian, Archer, Or Mage --")

        playerClass = input("> ")

        if playerClass.lower() == "guardian":
            Kit = "Guardian"
            MaxHealth = 150
            Health = MaxHealth
            Mana = 0
            Damage = 5
            Coin = 20

        if playerClass.lower() == "archer":
            Kit = "Archer"
            MaxHealth = 110
            Health = MaxHealth
            Mana = 0
            Damage = 8
            Coin = 20

        if playerClass.lower() == "mage":
            Kit = "Mage"
            MaxHealth = 120
            Health = MaxHealth
            Mana = 100
            Damage = 6
            Coin = 20

        Player = create_new_Player(Name, Health, MaxHealth, Mana, Kit, Level, XP, MaxXP, Damage, Coin)
        return Player

    except:
        print(Fore.RED + "[ERROR CREATING CHARACTER]")

def slowType(str):
    x = 0.001
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(x)

def storyType(str):
    x = 0.01
    for letter in str:
        for char in letter:
            sys.stdout.write(char)
            time.sleep(x)

def storyPrint(text):
    storyType(text)
    if speechEngineActive:
        speechEngine.say(text)
        speechEngine.runAndWait()
        speechEngine.stop()

def continueOrShowStats(stats):
    if stats:
        userInput = input("Press Enter To Continue OR Type 1 To Show Your Stats")
        if userInput == "1":
            print(" ")
            print("==================|")
            print(Fore.LIGHTGREEN_EX + f"Current XP: {XP}")
            print(Fore.GREEN + f"Max XP: {MaxXP}")
            print(Fore.CYAN + f"Current Level: {Level}")
            print(Fore.RED + f"Health: {Health}")
            print(Fore.LIGHTRED_EX + f"Damage: {Damage}")
            print(Fore.YELLOW + f"Coin: {Coin}")
            if Kit.lower() == "mage":
                print(Fore.BLUE + f"Mana: {Mana}")
            print("==================|")
            print(" ")
            continueOrShowStats(False)

    if not stats:
        userInput = input("Press Enter To Continue")

def SAVE_GAME():
    DATA_ARRAY = [Name, Level, Health, MaxHealth, Mana, Kit, XP, MaxXP, Damage, Coin]
    pickle.dump(DATA_ARRAY, open(f"Saved_Game_Data/{Name}.dat", "wb"))

def Random_Shop_Keeper_Items():
    global MaxHealth
    global Damage
    global DamageBoostActive
    global Health
    global PotionOfHealActive
    global PotionOfIncreaseHealthActive
    global XPBoost
    global XPGain
    global XP
    global XpGainPerEnemy
    global Coin

    i = 0
    RNG_ARRAY = []

    # Active Items In Shop
    PotionOfIncreaseHealthActive = False
    PotionOfHealActive = False
    DamageBoostActive = False
    XPBoost = False
    XPGain = False

    commonItemsMinCost = 10
    commonItemsMaxCost = 30
    rareItemsMinCost = 40
    rareItemsMaxCost = 60
    specialItemsMinCost = 100
    specialItemsMaxCost = 200

    # COST OF ITEMS
    potionOfHealthCost = rng(commonItemsMinCost, commonItemsMaxCost)
    potionOfXpGainCost = rng(commonItemsMinCost, commonItemsMaxCost)
    
    potionOfMaxHealthBoostCost = rng(rareItemsMinCost, rareItemsMaxCost)
    potionOfDamageBoostCost = rng(rareItemsMinCost, rareItemsMaxCost)
    potionOfXpBoostCost = rng(rareItemsMinCost, rareItemsMaxCost)


    # Number of Sections On The Market (Add If You Make A New One) Ex. XP Items
    marketSections = 3

    # Display Player Money
    print(Fore.YELLOW + f"Your Coins: {Coin}")
    print("----------------------------------------------------------------------------")

    while i <= marketSections:
        i += 1
        RNG_ARRAY.append(rng(1, 2))

    # HEALING ITEM
    if RNG_ARRAY[0] == 1:
        print(Fore.LIGHTRED_EX + "Item (1): Potion Of Health [Restore Health To Max Health]" + Fore.LIGHTYELLOW_EX + f"[Cost: {potionOfHealthCost}]")
        PotionOfHealActive = True
    elif RNG_ARRAY[0] == 2:
        print(Fore.LIGHTRED_EX + "Item (1): Potion Of Max Health Boost [+10 Max Health]"  + Fore.LIGHTYELLOW_EX + f"[Cost: {potionOfMaxHealthBoostCost}]")
        PotionOfIncreaseHealthActive = True

    # DAMAGE ITEM
    if RNG_ARRAY[1] == 1:
        print(Fore.BLUE + "Item (2): Damage Boosting Potion [+1 Strength]" + Fore.LIGHTYELLOW_EX + f"[Cost: {potionOfDamageBoostCost}]")
        DamageBoostActive = True
    elif RNG_ARRAY[1] == 2:
        print(Fore.LIGHTBLUE_EX + "Item (2): Damage Boosting Potion (+1 Strength)" + Fore.LIGHTYELLOW_EX + f"[Cost: {potionOfDamageBoostCost}]")
        DamageBoostActive = True

    # XP ITEM
    if RNG_ARRAY[2] == 1:
        print(Fore.LIGHTGREEN_EX + "Item (3): XP Boost Potion [+1 XP Per Battle]" + Fore.LIGHTYELLOW_EX + f"[Cost: {potionOfXpBoostCost}]")
        XPBoost = True

    elif RNG_ARRAY[2] == 2:
        print(Fore.LIGHTGREEN_EX + "Item (3): XP Gain Potion [+8 XP]" + Fore.LIGHTYELLOW_EX + f"[Cost: {potionOfXpGainCost}]")
        XPGain = True

    # CLASS SPECIFIC ITEMS

    #TODO: - create items that cater to specific kits, warrior-new move or something like that


    print("----------------------------------------------------------------------------")
    
    # PLAYER CHOICE FOR ITEM
    userInput = input(">")

    if userInput == "1" and PotionOfHealActive:
        
        if(Coin >= potionOfHealthCost):
            Health = MaxHealth
            PotionOfHealActive = False
            Coin -= potionOfHealthCost
            print(Fore.LIGHTGREEN_EX + f"Health Is Now -> {Health}")
            print(Fore.YELLOW + f"Coins Now At -> {Coin}")
            print(" ")
            input("Press Enter To Continue")
        else:
            print(Fore.LIGHTRED_EX + "Sorry You Don't Have Enough Coin For This Item")
            input("Press Enter To Continue")
        
        

    elif userInput == "1" and PotionOfIncreaseHealthActive:
        
        if(Coin >= potionOfMaxHealthBoostCost):
            MaxHealth += 10
            PotionOfIncreaseHealthActive = False
            Coin -= potionOfMaxHealthBoostCost
            print(f"Max Health Is Now -> {MaxHealth}")
            print(Fore.YELLOW + f"Coins Now At -> {Coin}")
            print(" ")
            input("Press Enter To Continue")
        else:
            print(Fore.LIGHTRED_EX + "Sorry You Don't Have Enough Coin For This Item")
            input("Press Enter To Continue")
        

    elif userInput == "2" and DamageBoostActive:
        if(Coin >= potionOfDamageBoostCost):
            Damage += 1
            DamageBoostActive = False
            Coin -= potionOfDamageBoostCost
            print(Fore.LIGHTRED_EX + f"Current Damage Is Now -> {Damage}")
            print(Fore.YELLOW + f"Coins Now At -> {Coin}")
            print(" ")
            input("Press Enter To Continue")
        else:
            print(Fore.LIGHTRED_EX + "Sorry You Don't Have Enough Coin For This Item")
            input("Press Enter To Continue")

       
    elif userInput == "2" and DamageBoostActive:
        if(Coin >= potionOfDamageBoostCost):
            Damage += 1
            DamageBoostActive = False
            Coin -= potionOfDamageBoostCost
            print(Fore.LIGHTRED_EX + f"Current Damage Is Now -> {Damage}")
            print(Fore.YELLOW + f"Coins Now At -> {Coin}")
            print(" ")
            input("Press Enter To Continue")
        else:
            print(Fore.LIGHTRED_EX + "Sorry You Don't Have Enough Coin For This Item")
            input("Press Enter To Continue")

    elif userInput == "3" and XPBoost:
        if(Coin >= potionOfXpBoostCost):
            XpGainPerEnemy += 1
            XPBoost = False
            Coin -= potionOfXpBoostCost
            print(f"XP Per Battle Is Now -> {XpGainPerEnemy}")
            print(Fore.YELLOW + f"Coins Now At -> {Coin}")
            print(" ")
            input("Press Enter To Continue")
        else:
            print(Fore.LIGHTRED_EX + "Sorry You Don't Have Enough Coin For This Item")
            input("Press Enter To Continue")

    elif userInput == "3" and XPGain:
        if(Coin >= potionOfXpGainCost):
            XP += 8
            XPGain = False
            Coin -= potionOfXpGainCost
            print(f"Current XP Is Now -> {XP} / {MaxXP}")
            print(Fore.YELLOW + f"Coins Now At -> {Coin}")
            print(" ")
            input("Press Enter To Continue")
        else:
            print(Fore.LIGHTRED_EX + "Sorry You Don't Have Enough Coin For This Item")
            input("Press Enter To Continue")


    # Save Game After Shop Keeper
    SAVE_GAME()

