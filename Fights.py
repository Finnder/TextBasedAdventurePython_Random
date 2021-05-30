import random
import time
import os
import Library
import Story
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

battleIsON = True

resistnextattack = False

# Called When Combat Sequence Starts
def RandomBasicEnemy():
    os.system('cls' if os.name == 'nt' else 'clear')
    global random_enemy
    rng = random.randint(1, 3)
    random_enemy = Random_Enemy()
    print(" ")
    print(Library.storyPrint("An Enemy Appeared Out Of No where!"))
    time.sleep(1)

    # Loop For Battle Sequence
    while battleIsON:
        Random_Move()
        Player_Move()

        # When Enemy Dies
        if random_enemy.enemyHP <= 0:
            print(" ")
            print(Fore.YELLOW + "The Enemy Was Slain!!")
            print(Fore.LIGHTYELLOW_EX + f"You Gained {Library.XpGainPerEnemy} XP!")
            playerXP = int(Library.XP)
            playerXP += Library.XpGainPerEnemy
            Library.XP = str(playerXP)

            # When Enemy Levels Up
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

# Enemy Random Move Event
def Random_Move():
    move = random.randint(1, 2)
    if move == 1:
        EnemyAttacks()
    if move == 2:
        EnemyDefends()

# Create A Random Enemy
def Random_Enemy():
    randomHP = random.randint(5, 20)
    random_damageMax = random.randint(4, 8)

    Current_Enemy = Enemy(randomHP, 0, 2, random_damageMax)
    return Current_Enemy

# When The Enemy Attacks
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

# When The Enemy Defends Itself
def EnemyDefends():
    global resistnextattack
    print(Fore.BLUE + "Enemy Defends! (Next outgoing attack will deal 50% less damage for player)")
    print(" ")
    resistnextattack = True
    time.sleep(1)

# When It's The Players Turn
def Player_Move():
    print(Fore.MAGENTA + "Available Moves: Attack(1), Defend(2), Pass(3)")
    print(" ")
    player_move = input("Your Move: ")
   
    if player_move == "1":
        PlayerAttacks()

    elif player_move == "2":
        pass

    else:
        PlayerPass()
        

# When Player Attacks 
def PlayerAttacks():
    global resistnextattack

    # When Enemy Goes Into Defence Mode - Reduce Player Damage
    if resistnextattack == True:
        random_enemy.enemyHP = random_enemy.enemyHP - (int(Library.Damage) / 2)
        print(f"You dealt {(Library.Damage / 2)} To The Enemy!")
        resistnextattack = False
    
    else:
        random_enemy.enemyHP = random_enemy.enemyHP - int(Library.Damage)
        print(f"You dealt {Library.Damage} To The Enemy!")

# When Player Passes 
def PlayerPass():
    print("You Passed Your Turn...")


# Enemy Constructor
class Enemy:
    def __init__(self, enemyHP, enemyResistance, enemyDamagePerHitMin, enemyDamagePerHitMax):
        self.enemyHP = enemyHP
        self.enemyDamagePerHitMin = enemyDamagePerHitMin
        self.enemyDamagePerHitMax = enemyDamagePerHitMax
        self.enemyResistance = enemyResistance