#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.decreaseHealth(self.power)

    def decreaseHealth(self, hitDamage):
        self.health = self.health - hitDamage

    def alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self):
        super().__init__(10, 5)

    def printStatus(self, enemy):
        print("You have {} health and {} power.".format(self.health, self.power))
        print("The goblin has {} health and {} power.".format(enemy.health, enemy.power))

class Goblin(Character):
    def __init__(self):
        super().__init__(6, 4)

def main(hero, goblin):
    while goblin.alive() and hero.alive():
        hero.printStatus(goblin)
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
            print("You do {} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")

hero = Hero()
goblin = Goblin()
main(hero, goblin)