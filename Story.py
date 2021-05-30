from Library import *
from colorama import init
import pyttsx3
import Paths
import Fights
import Library
from PIL import Image

# Colorama init
init(autoreset=True)

numOfFights = 0

def intro():
    global numOfFights
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
    
    if numOfFights >= 2:
        NewShopkeeper()

    numOfFights += 1
    NewFight()

# Generates random path for player
def NewPath():
    Paths.RandomPath()

# Create A New Battle Sequence For Player
def NewFight():
    Fights.RandomBasicEnemy()

# Create A Shopkeeper
def NewShopkeeper():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = "You are walking down a path and see a small road side shop."
    storyPrint(text)

    print("\n See whats in the shop?(1) OR Continue(2)")
    userInput = input(">")
    if userInput == "shop" or "1":
        Library.Random_Shop_Keeper_Items()

    elif userInput == "continue" or "2":
        pass


