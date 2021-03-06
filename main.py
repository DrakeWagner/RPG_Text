import sys
import time
import random
from random import randint

for i in range(0, 5):
    print(' ')
print('===================================================')
print('=========== Welcome to rpg_1_test =================')
print('===================================================')


def main_menu():
    print('Welcome to rpg_1_test!')
    print('1) Start')
    print('2) About')
    print('3) Exit')
    menu_input = input('>>> ')
    if menu_input == '1':
        start()
    if menu_input == '2':
        pass
    if menu_input == '3':
        sys.exit()
    else:
        main_menu()


class Player_Class:
    def __init__(self, myclass=None, hp=0, maxhp=0, strength=0, agility=0, gold=0, potions=0, sword=False,
                 shield=False):
        self.myclass = myclass
        self.hp = hp
        self.maxhp = maxhp
        self.strength = strength
        self.agility = agility
        self.gold = gold
        self.potions = potions
        self.sword = sword
        self.shield = shield

    def pick_class(self):
        # Chooses the player's main class
        myclassOptions = ['warrior', 'wizard', 'archer']
        print('Create your player')
        print('You may pick from the options "warrior", "wizard", and "archer"')
        while True:
            myclasschoice = input('>>  ')
            if myclasschoice in myclassOptions:
                self.myclass = myclasschoice
                print('You have chosen {}!'.format(myclasschoice))
                break
            else:
                print('Please try again. Enter "warrior", "wizard", or "archer"')
        if self.myclass == 'warrior':
            self.myclass = 'warrior'
            self.maxhp = 25
            self.hp = 25
            self.strength = 3
            self.agility = 1
            self.potions = 0
            self.sword = False
            self.shield = False
        if self.myclass == 'archer':
            self.myclass = 'archer'
            self.maxhp = 15
            self.hp = 15
            self.strength = 5
            self.agility = 8
            self.potions = 0
            self.sword = False
            self.shield = False
        if self.myclass == 'wizard':
            self.myclass = 'wizard'
            self.maxhp = 12
            self.hp = 12
            self.strength = 6
            self.agility = 4
            self.potions = 1
            self.sword = False
            self.shield = False

# Assigns the chosen class to p1
p1 = Player_Class()


# Starts the game loop
def start():
    p1.pick_class()
    menu(p1)


# Main loop of the game
def menu(your_player):
    time.sleep(.5)
    print('================')

    if p1.hp <= 0:
        print('Oh dear, you died.')
        time.sleep(2)
        print(' \n' * 3)
        main_menu()

    if your_player.gold < 0:
        your_player.gold = 0
    print('Gold: %i' % your_player.gold)
    print('HP: %i/%i' % (your_player.hp, your_player.maxhp))
    print('Potions: %i' % your_player.potions)
    print(' ')
    print('1) Fight')
    print('2) Store')
    print('3) Player Info')
    print('4) Use Healing Potion')
    print('5) Explore')
    option = int(input('>> '))
    if option == 1:
        fight()
    elif option == 2:
        store(p1)
    elif option == 3:
        print('[[[Player Stats]]]')
        for key, value in p1.__dict__.items():
            print(key, ': ', value, sep='')
        menu(p1)
    elif option == 4:
        use_potion(p1)
        menu(p1)
    elif option == 5:
        pass
        # explore()

# Healing potion mechanics
def use_potion(your_player):
    if your_player.potions > 0:
        your_player.potions -= 1
        your_player.hp += 10
        print('You gulp down the crimson colored liquid. You feel your hp go up by {}.'.format(10))
        if your_player.hp > your_player.maxhp:
            your_player.hp = your_player.maxhp
    elif your_player.potions == 0:
        print('You have no healing potions!')


# Classes
class Zombie:
    def __init__(self, name='Zombie'):
        self.myclass = name
        self.maxhp = 20
        self.hp = self.maxhp
        self.strength = 5
        self.agility = 1
        self.gold = randint(4, 8)


class Skeleton:
    def __init__(self, name='Skeleton'):
        self.myclass = name
        self.maxhp = 15
        self.hp = self.maxhp
        self.strength = 3
        self.agility = 3
        self.gold = randint(1, 4)


# Decides the enemy
def enemy_decider():
    global enemy
    num = randint(1, 2)
    if num == 1:
        enemy = Skeleton()
    elif num == 2:
        enemy = Zombie()
    print('A {} suddenly appears!'.format(enemy.myclass))


def fight():
    enemy_decider()
    print(enemy.myclass)

    while p1.hp >= 0 or enemy.hp >= 0:
        print('1) Attack')
        print('2) Run')
        print('3) Use Potion')
        option = input('>>> ')
        if option == '1':
            attack(p1, enemy)
            print('')
        elif option == '2':
            run(p1, enemy)
        elif option == '3':
            # Uses potion as your turn in battle, then defend
            if p1.potions > 0:
                use_potion(p1)
                enemy_attack(p1, enemy)
            elif p1.potions <= 0:
                print('You have no healing potions!')



    print('fight() ended')

def player_attack(p1, enemy):
    # Player's turn
    damage = p1.strength + randint(-2, 2)
    if p1.hp > 0:
        enemy.hp -= damage
        print('You attack the {} for {} damage.'.format(enemy.myclass, damage))

# Enemy's turn
def enemy_attack(p1, enemy):
    damage = enemy.strength + randint(-2, 2)
    if enemy.hp > 0:
        # Player's dodge chance (bypass enemy attack)
        hitmiss = 20 - int(p1.agility)
        DodgeDie = randint(1, hitmiss)
        if 4 > DodgeDie:
            print('You dodged the attack!')
        elif 4 <= DodgeDie:
            # Enemy attack
            p1.hp -= damage
            print('The {} hit you for {} damage!'.format(enemy.myclass, damage))




def attack(p1, enemy):
    # Attack mechanics
    player_attack(p1, enemy)

    # Enemy's turn
    enemy_attack(p1, enemy)

    # Prints status of player and enemy
    if p1.hp > 0:
        print('Your hp: {}/{}'.format(p1.hp, p1.maxhp))
    elif p1.hp <= 0:
        print('Oh dear, you died.')
        # print('Score: {}'.format(score)
        time.sleep(2)
        print(' \n' * 3)
        main_menu()
    if enemy.hp > 0:
        print('{} hp: {}/{}'.format(enemy.myclass, enemy.hp, enemy.maxhp))
    elif enemy.hp <= 0:
        print('You killed the {}!'.format(enemy.myclass))
        time.sleep(1)
        print('You found {} gold.'.format(enemy.gold))
        p1.gold += enemy.gold
        time.sleep(1)
        menu(p1)


def run(x, y):
    success = randint(1, 2)
    print("You attempt to flee...")
    time.sleep(1)
    if success == 1:
        print('You successfully fled the battle!')
        print('In your hurry to get away, you dropped some gold!')
        x.gold -= 2
        menu(p1)
    if success == 2:
        print('You failed to flee...')
        time.sleep(1)
        enemy_attack(x, y)


def shop_intro_line():
    line1 = 'A shopkeeper is standing at the counter, eating some mashed potatoes.'
    line2 = 'An odd looking man welcomes you into his shop'
    line3 = 'You startle the shopkeeper as you enter, causing him scream.'
    line4 = 'A talking cat sits on the counter, flicking its tail.'
    line5 = 'A shopkeeper is standing at the counter, eating some mashed potatoes.'
    lines = [line1, line2, line3, line4, line5]
    random_shop_intro_line = random.choice(lines)
    print(random_shop_intro_line)

def store(player):
    print('/////////////////||                      \n',
          '||Ye Olde Shoppe||                          \n',
          '|||||||[]|||||||||')
    shop_intro_line()
    time.sleep(1)
    print("You're a %s! I have just the goods you need." % player.myclass)
    time.sleep(1)

    # Want to add staff/bow for other classes eventually
    while player.myclass == 'warrior' or 'archer' or 'wizard':
        warrior_items = ['exit', 'sword', 'Sword', 'shield', 'Shield', 'healing potion', 'potion']
        print('[ Sword: 15 gold ]\n'
              '[ Shield: 15 gold ]\n'
              '[ Healing Potion: 5 gold ]')
        print(' ')
        print("Enter an item name, or type 'exit' to return to the menu")
        storeinput = input('>>> ')
        storeinput = storeinput.lower()
        if storeinput in warrior_items:
            if storeinput == 'exit':
                menu(p1)
            elif storeinput == 'sword':
                if player.gold >= 15 and player.shield == False:
                    print('You purchase the sword. You feel your strength go up by 3')
                    player.gold -= 15
                    player.strength += 3
                    player.shield = True
                elif player.gold < 15:
                    print("You can't afford this!")
            elif storeinput == 'shield':
                if player.gold >= 15 and player.shield == False:
                    print('You purchase the shield. You feel your agility go up by 3')
                    player.gold -= 15
                    player.agility += 3
                    player.shield = True
                elif player.gold < 15:
                    print("You can't afford this!")
            elif storeinput == 'healing potion' or 'potion':
                if player.gold >= 5:
                    print('You purchase the potion! It looks like it can restore 10 hitpoints.')
                    player.potions += 1
                    player.gold -= 5
                elif player.gold < 5:
                    print("You can't afford this, idiot!")
        elif storeinput not in warrior_items:
            print("Did you mean something else?")
    menu(p1)


def explore(p1):
    pass


main_menu()
