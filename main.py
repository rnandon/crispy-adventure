from random import randint
from events import *
from player import *
from resources import *



# This will pull in the mechanics, dialogue, events, and items from other assets and handle the "engine" aspect of the game.
# Features in this portion will be the UI and options selections. I might try to implement Pygame or TKinter later, but for now I'm rolling with just console based.
# Features to look into: saving/loading the game state, logging experience, generally more advanced RPG features than enter a room and interact and repeat.

class Interface:
    def __init__(self):
        self.options = []
        game = Game()
        current_options = game.get_options()
        

class Game:
    def __init__(self):
        print('Setting up the game for you. \n')
        dungeon = Dungeon_Matrix()
        player_name = input('Enter your name, hero: \n')
        player = Player(player_name)
        
