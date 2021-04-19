import Music
from Library import *
from colorama import init
from colorama import Fore, Back, Style


# Colorama init
init(autoreset=True)

def start_Up_Menu():

    print(slowType(
    """ 
    Hello, Welcome To Finn's RPG and Text Base Adventure!!!
    -------------------------------------------------------
    -> New Game
    --> Continue
    ---> Options
    ----> Exit
    """
    ))

def options_Menu():
    print(slowType( """
    - [Manage Saves]
    - [Modifiers]
    """
    ))

    optionsChoice = input(">")
    
    if optionsChoice.lower() == "manage saves":
        print("--- SAVED GAMES ---")

    if(optionsChoice.lower() == "modifiers"):
        pass


def intro():
    storyPrint(
    """
    You begin in a small village off the coast of a very large ocean. You grew up here and you love it here.
    You feel a desire for adventure to see whats beyond the little village that has held you safe. 
    Your parents say you should stay in the village where its safe, but something is driving you to explore the world.
    """)
