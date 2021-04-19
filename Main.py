import Library, Game_Mechanics, Story, Encounters.pathEncounters
import random
from colorama import init
from colorama import Fore, Back, Style

# Colorama init
init(autoreset=True)

user_Selection = input("-> ")

def start_Up_Menu():

    print(
    """ 
    Hello, Welcome To Finn's RPG and Text Base Adventure!!!
    -------------------------------------------------------
    -> New Game
    --> Continue
    ---> Options
    ----> Exit
    """
    )

    if user_Selection.lower() == "new game" or user_Selection == "1":
        # New Player Set-Up
        player = Library.new_Player()
        playerName = player.Name
        playerLevel = player.Level
        playerHealth = player.Health
        playerMana = player.Mana
        playerClass = Library.Kit

        # Writing the save data for new player
        data = open(f"./Saved_Game_Data/{playerName}.txt", "w")
        data.write(f"{playerName} \n")
        data.write(f"{playerLevel} \n")
        data.write(f"{playerHealth} \n")
        data.write(f"{playerMana} \n")
        data.write(f"{playerClass} \n")
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
        data.close()

    if user_Selection.lower() == "options" or user_Selection == "3":
        Story.options_Menu()

    if user_Selection.lower() == "exit" or user_Selection == "4":
        quit()
