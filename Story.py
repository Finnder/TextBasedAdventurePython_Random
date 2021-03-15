import Music
from termcolor import colored
import simpleaudio as sa
from Library import *

def start_Up_Menu():

    playMusic('Music/menuMusic.wav')

    startText = colored("Start", "green")
    optionsText = colored("Options", "blue")
    exitText = colored("Exit", "red")

    print(slowType(f""" 
    Hello, Welcome To Finn's RPG and Text Base Adventure!!!
    -------------------------------------------------------
    (Type One)
    -> {startText}
    --> {optionsText}
    ---> {exitText}
    """
    ))

def options_Menu():
    pass

def intro():
    storyPrint("""
    You begin in a small village off the coast of a very large ocean. You grew up here and you love it here.
    You feel a desire for adventure to see whats beyond the little village that has held you safe. 
    Your parents say you should stay in the village where its safe, but something is driving you to explore the world.
    """)
