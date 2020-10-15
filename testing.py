from player import *

def item_test():
    item1 = Item('douche', 0, 'canoe')
    item2 = item1
    item3 = Item('sword', 0, "It's a sword", True, 2, 0, 0, 2)

    inv = Inventory()

    inv.add(item1)
    inv.add(item2)
    inv.add(item3)
    
    print(inv)
    return

def enem_test():
    enemy = Enemy('Derp', 15, 0, 0, 0)
    while enemy.health > 0:
        enemy.enemy_defend(1)
        enemy.enemy_defend(2)
        enemy.enemy_defend(3)
        enemy.enemy_defend(4)
        
def player_test1():
    player = Player('Frodo')
    use_test = Item('potion', 2, 'Healing potion that restores 2 health.')
    equip_test = Item('Sword', 0, 'A basic iron sword', True, 5, 0, 0, 5)
    enemy = Enemy('Derp', 15, 1, 0, 0)
    
    player.inventory.add(use_test)
    player.inventory.add(use_test)
    player.inventory.add(equip_test)
    player.max_health += 10
    print(player.inventory)
    
    player.use_item(use_test)
    enemy.enemy_defend(player.attack())
    
    player.equip(equip_test)
    
    enemy.enemy_defend(player.attack())
    
    while player.is_alive and enemy.is_alive:
        loot = enemy.enemy_defend(player.attack())
        if not enemy.is_alive:
            player.inventory.add(loot)
    
    print(player.inventory)
    
def player_test2():    
    player = Player('Frodo')
    use_test = Item('potion', 2, 'Healing potion that restores 2 health.')
    equip_test = Item('Sword', 0, 'A basic iron sword', True, 5, 0, 0, 5)
    enemy = Enemy('Derp', 15, 10, 2, 0)
    
    player.max_health += 10
    
    player.inventory.add(use_test)
    player.inventory.add(use_test)
    player.inventory.add(equip_test)
    player.use_item(use_test)
    player.use_item(equip_test)
    player.max_health += 10
    player.equip(equip_test)
    print(player.inventory)
    
    print(player)
    player.unequip(equip_test)
    print(player)
    
    while player.is_alive:
        player.defend(enemy.enemy_attack())
    
    
#item_test()
#enem_test()
#player_test1()
player_test2()
