import random
import time

import Library
import Story
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)
# ALL FIGHT ENCOUNTERS IN THE WORLD

battleIsON = True
xpGainPerEnemy = 10

def RandomBasicEnemy():
    global random_enemy
    rng = random.randint(1, 3)
    random_enemy = Random_Enemy()
    print(" ")
    print(Library.storyPrint("An Enemy Appeared Out Of No where!"))
    time.sleep(1)
    while battleIsON:
        Random_Move()
        Player_Move()
        if random_enemy.enemyHP <= 0:
            print(" ")
            print(Fore.YELLOW + "The Enemy Was Slain!!")
            print(Fore.LIGHTYELLOW_EX + f"You Gained {xpGainPerEnemy} XP!")
            playerXP = int(Library.XP)
            playerXP += xpGainPerEnemy
            Library.XP = str(playerXP)
            if playerXP >= 100:
                print(Fore.LIGHTBLUE_EX + "LEVEL UP!")
                playerXP = int(Library.XP)
                playerXP = 0
                Library.XP = str(playerXP)
                playerLevel = int(Library.Level)
                playerLevel += 1
                Library.Level = str(playerLevel)
            break

    Story.intro()

def Random_Move():
    move = random.randint(1, 2)
    if move == 1:
        EnemyAttacks()
    if move == 2:
        EnemyDefends()


def Random_Enemy():
    randomHP = random.randint(5, 20)
    random_damageMax = random.randint(4, 8)

    Current_Enemy = Enemy(randomHP, 2, random_damageMax)
    return Current_Enemy


def EnemyAttacks():
    enemyDamageToDeal = random.randint(random_enemy.enemyDamagePerHitMin, random_enemy.enemyDamagePerHitMax)
    playerHealth = int(Library.Health)
    playerHealth -= enemyDamageToDeal
    Library.Health = str(playerHealth)
    Library.SAVE_GAME()

    print(Fore.RED + f"Enemy Attacks! Dealing {Fore.LIGHTRED_EX + str(enemyDamageToDeal)} Total Damage!")
    print(f"Player Now Has {Fore.LIGHTRED_EX + Library.Health} Health")
    print(" ")
    time.sleep(1)

def EnemyDefends():
    print(Fore.BLUE + "Enemy Defends! (Next outgoing attack will deal 50% less damage for player)")
    print(" ")
    time.sleep(1)


def Player_Move():
    print(Fore.MAGENTA + "Available Moves: Attack(1), Defend(2), Pass(3)")
    print(" ")
    player_move = input("Your Move: ")
    if player_move == "1":
        PlayerAttacks()


def PlayerAttacks():
    print(f"You dealt {Library.Damage} To The Enemy!")
    random_enemy.enemyHP = random_enemy.enemyHP - int(Library.Damage)


class Enemy:
    def __init__(self, enemyHP, enemyDamagePerHitMin, enemyDamagePerHitMax):
        self.enemyHP = enemyHP
        self.enemyDamagePerHitMin = enemyDamagePerHitMin
        self.enemyDamagePerHitMax = enemyDamagePerHitMax
