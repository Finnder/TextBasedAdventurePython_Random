import os

from colorama import Fore, Back
from colorama import init
import simpleaudio as sa
import Library
import Story
import Music
import Paths

# Colorama init
init(autoreset=True)

# Menu Music
menuMusic = sa.WaveObject.from_wave_file('Music/menuMusic.wav')
isMenuMusicActive = False

def options_Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + "--- OPTIONS MENU ---")
    print(Fore.LIGHTRED_EX + """
- [Manage Saves]
- [Modifiers]
    """)

    optionsChoice = input(">")

    if optionsChoice.lower() == "manage saves" or optionsChoice == "1":
        print(Fore.GREEN + Back.BLACK + "--- SAVED GAMES ---")
        for file in os.listdir('Saved_Game_Data'):
            if os.path.isfile(os.path.join('Saved_Game_Data', file)):
                print(Back.BLACK + Fore.RED + file)

        print(" ")
        input("Press Any Button To Continue")

        # Clear Terminal and Show Menu
        os.system('cls' if os.name == 'nt' else 'clear')

        startup_Menu(False)

    # If you want to add modifications to the game
    elif optionsChoice.lower() == "modifiers" or optionsChoice == "2":
        if isMenuMusicActive:
            print("Music - ON")
        else:
            print("Music - OFF")

        userInput = input(">")
        if userInput.lower() == "music" or "1":
            global isMenuMusicActive
            if isMenuMusicActive:
                os.system('cls' if os.name == 'nt' else 'clear')
                isMenuMusicActive = False
                startup_Menu(isMenuMusicActive)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                isMenuMusicActive = True
                startup_Menu(isMenuMusicActive)

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        startup_Menu(isMenuMusicActive)


def startup_Menu(music):

    if music:
        menuMusic.play()
    if not music:
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
        playerDamage = player.Damage

        # Writing the save data for new player
        data = open(f"./Saved_Game_Data/{playerName}.txt", "w")
        data.write(f"{playerName}\n")
        data.write(f"{playerLevel}\n")
        data.write(f"{playerHealth}\n")
        data.write(f"{playerMana}\n")
        data.write(f"{playerClass}\n")
        data.write(f"{playerCurrentXP}\n")
        data.write(f"{playerMaxXP}\n")
        data.write(f"{playerDamage}")
        data.close()

        Story.intro()

    if user_Selection.lower() == "continue" or user_Selection == "2":
        savedName = input("Enter Saved Game Name: ")

        try:
            data = open(f"./Saved_Game_Data/{savedName}.txt", "r")
            Library.Name = data.readline()
            Library.Level = data.readline()
            Library.Health = data.readline()
            Library.Mana = data.readline()
            Library.Kit = data.readline()
            Library.XP = data.readline()
            Library.MaxXP = data.readline()
            Library.Damage = data.readline()
            data.close()
        except FileNotFoundError:
            print(Fore.RED + "THE NAME YOU ENTERED DOES NOT EXIST.")
            input(" ")
            os.system('cls' if os.name == 'nt' else 'clear')

            startup_Menu(isMenuMusicActive)

        Library.continueOrShowStats(True)
        Story.intro()

    if user_Selection.lower() == "options" or user_Selection == "3":
        options_Menu()

    if user_Selection.lower() == "exit" or user_Selection == "4":
        quit()

# Initial Start Up
startup_Menu(isMenuMusicActive)
