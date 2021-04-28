from Library import *
from colorama import init
import pyttsx3
import Paths
import Fights
import Library

# Colorama init
init(autoreset=True)

def intro():
    numOfFights = 0
    text = """
    You begin in a small village off the coast of a very large ocean. You grew up here and you love it here.
    You feel a desire for adventure to see whats beyond the little village that has held you safe. 
    Your parents say you should stay in the village where its safe, but something is driving you to explore the world.
    """
    storyPrint(text)

    print(" ")
    continueOrShowStats(True)
    NewPath()
    continueOrShowStats(False)
    numOfFights += 1
    NewFight()
    if numOfFights >= 5:
        NewShopkeeper()

# Generates random path for player
def NewPath():
    Paths.RandomPath()

def NewFight():
    Fights.RandomBasicEnemy()

def NewShopkeeper():
    text = "You are walking down a path and see a small road side shop."
    storyPrint(text)

    print("See whats in the shop?(1) OR Continue(2)")
    userInput = input(">")
    if userInput == "shop" or "1":
        Library.Random_Shop_Keeper_Items()

    elif userInput == "continue" or "2":
        pass


