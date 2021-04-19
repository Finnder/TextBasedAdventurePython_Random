import os

import Library, Game_Mechanics, Story, Encounters.pathEncounters
import random
from colorama import init
from colorama import Fore, Back, Style

# Colorama init
init(autoreset=True)


def options_Menu():
    print("""
    - [Manage Saves]
    - [Modifiers]
    """
          )

    optionsChoice = input(">")

    if optionsChoice.lower() == "manage saves" or optionsChoice == "1":
        print(Fore.GREEN + Back.BLACK + "--- SAVED GAMES ---")
        for file in os.listdir('Saved_Game_Data'):
            if os.path.isfile(os.path.join('Saved_Game_Data', file)):
                print(Back.BLACK + Fore.RED + file)

        print(" ")
        input("Press Any Button To Continue")

    if (optionsChoice.lower() == "modifiers" or optionsChoice == "2"):
        pass

print(
    f""" 
Hello, Welcome To Finn's RPG and Text Base Adventure!!!
-------------------------------------------------------
-> New Game
--> Continue
---> Options
----> Exit
"""
)

user_Selection = input("> ")

if user_Selection.lower() == "new game" or user_Selection == "1":
    # New Player Set-Up
    player = Library.new_Player()
    playerName = player.Name
    playerLevel = player.Level
    playerHealth = player.Health
    playerMana = player.Mana
    playerClass = player.Kit
    playerCurrentXP = player.XP
    playerMaxXP = player.MaxXP


    # Writing the save data for new player
    data = open(f"./Saved_Game_Data/{playerName}.txt", "w")
    data.write(f"{playerName}\n")
    data.write(f"{playerLevel}\n")
    data.write(f"{playerHealth}\n")
    data.write(f"{playerMana}\n")
    data.write(f"{playerClass}\n")
    data.write(f"{playerCurrentXP}")
    data.close()

    Story.intro()

if user_Selection.lower() == "continue" or user_Selection == "2":
    savedName = input("Enter Saved Game Name: ")

    data = open(f"./Saved_Game_Data/{savedName}.txt", "r")
    playerName = data.readline()
    playerLevel = data.readline()
    playerHealth = data.readline()
    playerMana = data.readline()
    playerClass = data.readline()
    playerCurrentXP = data.readline()
    data.close()

if user_Selection.lower() == "options" or user_Selection == "3":
        options_Menu()

if user_Selection.lower() == "exit" or user_Selection == "4":
        quit()



