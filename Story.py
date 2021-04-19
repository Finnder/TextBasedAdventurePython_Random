import os

import Music
from Library import *
from colorama import init
from colorama import Fore, Back, Style
import pyttsx3

speechEngine = pyttsx3.init()

# Colorama init
init(autoreset=True)

def intro():
    text = """
    You begin in a small village off the coast of a very large ocean. You grew up here and you love it here.
    You feel a desire for adventure to see whats beyond the little village that has held you safe. 
    Your parents say you should stay in the village where its safe, but something is driving you to explore the world.
    """
    storyPrint(text)
    speechEngine.say(text)
    speechEngine.runAndWait()
    speechEngine.stop()

    print(" ")
    input("Press Enter To Continue")

    NewPath()

# Generates random path for player
def NewPath():
    pass



