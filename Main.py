import os

import pickle
from colorama import Fore, Back
from colorama import init
import simpleaudio as sa
import Library
import Story
from PIL import Image
import Music
import Paths

# Colorama init
init(autoreset=True)

CurrentVersion = 0.1

# Menu Music
menuMusic = sa.WaveObject.from_wave_file('Music/menuMusic.wav')
isMenuMusicActive = False

def options_Menu():
    global isMenuMusicActive
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + "--- OPTIONS MENU ---")
    print(Fore.LIGHTRED_EX + """
- [Manage Saves]
- [Modifiers]
    """)

    optionsChoice = input(">")

    # Shows Saved Games
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

        if Library.speechEngineActive:
            print("Text To Speech - ON")
        else:
            print("Text To Speech - OFF")

        userInput = input(">")
        if userInput.lower() == "music" or "1":
            if isMenuMusicActive:
                os.system('cls' if os.name == 'nt' else 'clear')
                isMenuMusicActive = False
                startup_Menu(isMenuMusicActive)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                isMenuMusicActive = True
                startup_Menu(isMenuMusicActive)
        if userInput.lower() == "texttospeech" or "2" or "tts":
            if Library.speechEngineActive:
                Library.speechEngineActive = False
            else:
                Library.speechEngineActive = True


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
 -> New Game - 1
 --> Continue - 2
 ---> Options - 3
 ----> Exit - 4
    """
    )

    user_Selection = input("> ")

    if user_Selection.lower() == "new game" or user_Selection == "1":

        # New Player Set-Up
        player = Library.new_Player()
        playerName = player.Name
        playerLevel = player.Level
        playerHealth = player.Health
        playerMaxHealth = player.MaxHealth
        playerMana = player.Mana
        playerClass = player.Kit
        playerCurrentXP = player.XP
        playerMaxXP = player.MaxXP
        playerDamage = player.Damage
        playerCoin = player.Coin

        DATA = [playerName, playerLevel, playerHealth, playerMaxHealth, playerMana, playerClass, playerCurrentXP, playerMaxXP, playerDamage, playerCoin]

        # Writing the save data for new player
        pickle.dump(DATA, open(f"Saved_Game_Data/{playerName}.dat", "wb"))

        Story.intro()

    if user_Selection.lower() == "continue" or user_Selection == "2":
        savedName = input("Enter Saved Game Name: ")

        try:
            # Retrieving data from save file
            SaveLoaded = pickle.load(open(f"Saved_Game_Data/{savedName}.dat", "rb"))
            Library.Name = SaveLoaded[0]
            Library.Level = SaveLoaded[1]
            Library.Health = SaveLoaded[2]
            Library.MaxHealth = SaveLoaded[3]
            Library.Mana = SaveLoaded[4]
            Library.Kit = SaveLoaded[5]
            Library.XP = SaveLoaded[6]
            Library.MaxXP = SaveLoaded[7]
            Library.Damage = SaveLoaded[8]
            Library.Coin = SaveLoaded[9]

        except FileNotFoundError:
            print(Fore.RED + "THE FILE-NAME YOU ENTERED DOES NOT EXIST.")
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
