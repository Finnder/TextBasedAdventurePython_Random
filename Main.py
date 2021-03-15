import Library, Game_Mechanics, Story, Encounters.pathEncounters
import random



Story.start_Up_Menu()

user_Selection = input("|> ")

if user_Selection.lower() == "new game":

    # New Player Set-Up
    player = Library.new_Player()
    playerName = player.Name
    playerLevel = player.Level
    playerHealth = player.Health
    playerMana = player.Mana

    Story.intro()
    Library.randomPath()
if user_Selection.lower() == "continue":

if user_Selection.lower() == "options":
    pass

if user_Selection.lower() == "exit":
    quit()

