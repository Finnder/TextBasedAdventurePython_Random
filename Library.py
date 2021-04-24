import sys
import time
import random
from colorama import init
from colorama import Fore, Back, Style

# Colorama init
init(autoreset=True)

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
    global Health
    global Mana
    global Kit
    global XP
    global MaxXP
    global Level
    global Damage

    try:
        Name = input("  Enter Your New Characters Name: ")
        Level = 1

        print(Fore.GREEN + "-- Choose A Class | Guardian, Archer, Or Mage --")

        playerClass = input("-> ")

        if playerClass.lower() == "guardian":
            Kit = "Guardian"
            Health = 150
            Mana = 0
            XP = 0
            MaxXP = 100
            Damage = 5

        if playerClass.lower() == "archer":
            Kit = "Archer"
            Health = 110
            Mana = 0
            XP = 0
            MaxXP = 100
            Damage = 8

        if playerClass.lower() == "mage":
            Kit = "Mage"
            Health = 120
            Mana = 100
            XP = 0
            MaxXP = 100
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

def storyPrint(str):
    storyType(str)

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

