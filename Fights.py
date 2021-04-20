import random
import time

import Library
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)
# ALL FIGHT ENCOUNTERS IN THE WORLD

battleIsON = True


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
            break


def Random_Move():
    move = random.randint(1, 3)
    if move == 1:
        EnemyAttacks()
    if move == 2:
        EnemyDefends()
    if move == 3:
        print(Back.WHITE + Fore.BLACK + "Enemy Passed His Turn")


def Random_Enemy():
    randomHP = random.randint(5, 20)
    random_damageMax = random.randint(4, 8)

    Current_Enemy = Enemy(randomHP, 2, random_damageMax)
    return Current_Enemy


def EnemyAttacks():
    enemyDamageToDeal = random.randint(random_enemy.enemyDamagePerHitMin, random_enemy.enemyDamagePerHitMax)
    print(Fore.RED + f"Enemy Attacks! Dealing {Fore.LIGHTRED_EX + str(enemyDamageToDeal)} Total Damage!")
    print(" ")
    time.sleep(2)


def EnemyDefends():
    print(Fore.BLUE + "Enemy Defends! (Next outgoing attack will deal 50% less damage for player)")
    print(" ")
    time.sleep(2)


def Player_Move():
    print(Fore.MAGENTA + "Available Moves: Attack(1), Defend(2), Pass(3)")
    print(" ")
    player_move = input("Your Move: ")
    if player_move == "1":
        PlayerAttacks()


def PlayerAttacks():
    print(f"You dealt {Library.Damage} To The Enemy!")
    random_enemy.enemyHP = random_enemy.enemyHP - Library.Damage


class Enemy:
    def __init__(self, enemyHP, enemyDamagePerHitMin, enemyDamagePerHitMax):
        self.enemyHP = enemyHP
        self.enemyDamagePerHitMin = enemyDamagePerHitMin
        self.enemyDamagePerHitMax = enemyDamagePerHitMax
