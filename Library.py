import sys
import simpleaudio
from termcolor import cprint, colored
import time
import random
from Encounters import pathEncounters


class create_new_Player:
    def __init__(self, Name, Health, Mana, Kit, Level):
        self.Name = Name
        self.Health = Health
        self.Mana = Mana
        self.Kit = Kit
        self.Level = Level


def rng(min, max):
    x = random.randint(min, max)
    return x


def new_Player():
    global Health
    global Mana
    global Kit

    Name = input("Please Enter A Name: ")
    Level = 1

    cprint(" --- Choose A Class | Guardian, Archer, Or Mage --- ", "cyan")
    playerClass = input("-> ")

    if playerClass.lower() == "guardian":
        Kit = "Guardian"
        Health = 180
        Mana = 0

    if playerClass.lower() == "archer":
        Kit = "Archer"
        Health = 100
        Mana = 0

    if playerClass.lower() == "mage":
        Kit = "Mage"
        Health = 120
        Mana = 100

    Player = create_new_Player(Name, Health, Mana, Kit, Level)
    return Player


def playMusic(musicfile):
    x = simpleaudio.WaveObject.from_wave_file(musicfile)
    x.play()


def slowType(str):
    x = 0.001
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(x)


def storyType(str):
    x = 0.01
    for letter in str:
        for char in letter:
            sys.stdout.write(char)
            time.sleep(x)


def storyPrint(str):
    colored(storyType(str), "blue")


def randomPath():
    randomnum = rng(1, 3)
    if randomnum == 1:
        pathEncounters.cavern_Path()
    if randomnum == 2:
        pathEncounters.mountain_Path()
    if randomnum == 3:
        pathEncounters.swamp_Path()
