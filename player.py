from random import randint
#from resources import *

# Defines the player class, which dictates room generation, boss creation, inventory management, so on.

class Player:
    def __init__(self, name):
        self.name = str(name)
        self.inventory = Inventory()
        self.max_health = 20
        self.health = 20
        self.damage = 1
        self.defense = 0
        self.power_rating = 0
        self.rooms_completed = 0
        self.is_alive = True
        
    def room_finish(self):
        self.rooms_completed += 1
        
    def equip(self, item):
        if item.equippable:
            self.max_health += item.health
            self.damage += item.damage
            self.defense += item.defense
            self.power_rating += item.power_rating
            print(item.name + " was equipped.\n")
            return
        else:
            print("""
{IT_NAME} cannot be used this way.
            """.format(IT_NAME=item.name))
            return
        
    def unequip(self, item):
        self.max_health -= item.max_health
        self.damage -= item.damage
        self.defense -= item.defense
        self.power_rating -= item.power_rating
        if self.max_health < 0:
            self.max_health = 0
        if self.damage < 1:
            self.damage = 1
        if self.defense < 0:
            self.defense = 0
        if self.power_rating < 0:
            self.power_rating = 0
        
    def use_item(self, item):
        if not item.equippable:
            if self.health + item.health <= self.max_health:
                self.health += item.health
                print("""
{NAME} used {ITEM} to restore {HEALS} health.
{NAME} has {HEALTH} health.
                """.format(NAME = self.name, ITEM = item.name, HEALS = item.health, HEALTH = self.health))
                self.inventory.remove(item)
                return
            elif self.health == self.max_health:
                print('Already at full health!')
            else:
                self.health = self.max_health
                self.inventory.remove(item)
                print( """
{NAME} used {ITEM} to restore {HEALS} health.
{NAME} has {HEALTH} health.
                """.format(NAME = self.name, ITEM = item.name, HEALS = item.health, HEALTH = self.health))
                return
        else:
            print("""
{IT_NAME} cannot be used this way.
            """.format(IT_NAME=item.name))
            return
        
    def attack(self):
        return self.damage
        
    def defend(self, damage):
        received = damage - self.defense
        if received < 0:
            received = 0
        self.health -= received
        if self.health <= 0:
            self.is_alive = False
            print("""
{NAME} received a fatal blow of {DAMAGE} damage, ending their journey.
            """.format(NAME = self.name, DAMAGE = received))
            return
        else:
            print("""
{NAME} received {DAMAGE}. {NAME} has {HEALTH} health points remaining.
            """.format(NAME = self.name, DAMAGE = received, HEALTH = self.health))
            return
            
    def __repr__(self):
        printable = self.name + ' ' + str(self.damage) + " " + str(self.is_alive)
        return printable
        
        

class Enemy:
    def __init__(self, name, health, damage, defense, power_rating):
        self.name = str(name)
        self.health = health
        self.damage = damage
        self.defense = defense
        self.power_rating = power_rating
        self.is_alive = True
        
    def enemy_attack(self):
        return self.damage
        
    def enemy_defend(self, damage):
        if not self.is_alive:
            print(self.name + ' is already dead.\n')
            return
        received = damage - self.defense
        if received < 0:
            received = 0
        self.health -= received
        if self.health <= 0:
            loot = self.die()
            print(self.name + ' dropped ' + loot.name + '!')
            return loot
        else:
            print("""
{ENEMY} received {DAM} damage. {ENEMY} has {HEALTH} health points remaining.
            """.format(ENEMY=self.name, DAM=received, HEALTH=self.health))
            
    
    def die(self):
        self.is_alive = False
        #loot = randint(0, 100)
        #return items_list[loot]
        print(self.name + " has died.")
        return Item('Testy boi', 1000, 'Just for testing')
        
        
        
class Item:
    def __init__(self, name, health, description, equippable=False, damage=0, defense=0, max_health=0, power_rating=0):
        self.name = name
        self.health = health
        self.description = description
        self.equippable = equippable 
        self.damage = damage
        self.defense = defense
        self.max_health = max_health
        self.power_rating = power_rating
        
    def __str__(self):
        return """
{NAME}
{DESC}
        """.format(NAME=self.name, DESC = self.description)
    
    def __repr__(self):
        return [self.name, self.health, self.description, self.equippable, self.damage, self.defense, self.power_rating]

class Inventory:
    def __init__(self):
        self.bag = []
        
    def add(self, item):
        temp = False
        for thing in self.bag:
            if thing[1] == item.name:
                thing[0] += 1
                temp = True
                print("""
{IT_NAME} was added to the inventory.
                """.format(IT_NAME=item.name))
                return
        if not temp:
            self.bag.append([1, item.name, item])
            print("""
{IT_NAME} was added to the inventory.
            """.format(IT_NAME = item.name))
            return
        
    def remove(self, item):
        for thing in self.bag:
            if item in thing:
                self.bag.remove(thing)
        
    def __repr__(self):
        printable = "Current Inventory: \n"
        for item in self.bag:
            printable = printable + str(item[0]) + "     " + str(item[1]) + '\n'
        return str(printable)    
        
                
        
        
        