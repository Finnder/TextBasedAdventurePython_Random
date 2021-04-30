import sys
import time
import random
from colorama import init
from colorama import Fore, Back, Style
import pyttsx3
import pickle

speechEngine = pyttsx3.init()

# Colorama init
init(autoreset=True)

Damage = None
XP = None
MaxXP = None
Kit = " "
Health = None
MaxHealth = None
Level = None
Name = ""
Coin = None

speechEngineActive = False

class create_new_Player:
    def __init__(self, Name, Health, Mana, Kit, Level, XP, MaxXP, Damage):
        self.Name = Name
        self.Health = Health
        self.Mana = Mana
        self.Kit = Kit
        self.Level = Level
        self.XP = XP
        self.MaxXP = MaxXP
        self.Damage = Damage

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
        Coin = 0
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

        if playerClass.lower() == "archer":
            Kit = "Archer"
            MaxHealth = 110
            Health = MaxHealth
            Mana = 0
            Damage = 8

        if playerClass.lower() == "mage":
            Kit = "Mage"
            MaxHealth = 120
            Health = MaxHealth
            Mana = 100
            Damage = 6

        Player = create_new_Player(Name, Health, Mana, Kit, Level, XP, MaxXP, Damage)
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
            print(Fore.LIGHTGREEN_EX + f"Current XP: {XP}")
            print(Fore.GREEN + f"Max XP: {MaxXP}")
            print(Fore.CYAN + f"Current Level: {Level}")
            print(Fore.RED + f"Health: {Health}")
            print(Fore.LIGHTRED_EX + f"Damage: {Damage}")
            if Kit.lower() == "mage":
                print(Fore.BLUE + f"Mana: {Mana}")
            continueOrShowStats(False)

    if not stats:
        userInput = input("Press Enter To Continue")

def SAVE_GAME():
    DATA_ARRAY = [Name, Level, Health, Mana, Kit, XP, MaxXP, Damage]
    pickle.dump(DATA_ARRAY, open(f"Saved_Game_Data/{Name}.dat", "wb"))

def Random_Shop_Keeper_Items():
    global MaxHealth
    global Damage
    global DamageBoostActive
    global Health

    i = 0
    RNG_ARRAY = []

    # Active Items In Shop
    PotionOfIncreaseHealthActive = False
    PotionOfHealActive = False

    DamageBoostActive = False

    while i <= 3:
        i += 1
        RNG_ARRAY.append(rng(1, 2))

    # HEALING ITEM
    if RNG_ARRAY[0] == 1:
        print(Fore.LIGHTRED_EX + "Item (1): Potion Of Health (Restore Health To Max Health)")
        PotionOfHealActive = True
    elif RNG_ARRAY[0] == 2:
        print("Item (1): Potion Of Max Health Boost (+10 Max Health)")
        PotionOfIncreaseHealthActive = True

    # DAMAGE ITEM
    if RNG_ARRAY[1] == 1:
        print(Fore.BLUE + "Item (2): Damage Boosting Potion (+1 Strength)")
        DamageBoost = True
    elif RNG_ARRAY[1] == 2:
        print(Fore.BLUE + "Item (2): Damage Boosting Potion (+1 Strength)")

    # OTHER ITEM
    if RNG_ARRAY[2] == 1:
        print(Fore.GREEN + "Item (3): XP Boost Potion (+5 XP Per Battle)")
    elif RNG_ARRAY[2] == 2:
        print(Fore.GREEN + "Item (3): WIP")

    userInput = input(">")
    if userInput == "1" and PotionOfHealActive:
        Health = MaxHealth

    elif userInput == "1" and PotionOfIncreaseHealthActive:
        MaxHealth += 10
        Health += 10

    elif userInput == "2" and DamageBoostActive:
        Damage += 1

