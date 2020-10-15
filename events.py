from random import randint

# Events defines the random and pseudorandom room encounters in the dungeon.
# Pre-defined events are logged in the list of events and are accessed via indexing.
# Randomly generated events will pull from a list of pre-defined encounter components, such as creatures, puzzles, treasures, etc.
# Randomly generated events created will be added to the list in order to maintain a more unique feeling to each room.
# Afterthought - it might be worthwhile to create themes of sorts (undead, goblins, other mythological creatures) to pull from. This would allow for greater diversity of encounters while not impeding development time (would just need to rename the classes).

class Dungeon_Matrix:
    def __init__(self, room_count=32):
        #could take an input to change dungeon size from rng, also shape for x and y dimensions
        self.room_count = room_count
        self.rooms_remaining = self.room_count
        self.printable = ''
        self.count = 0
        if self.room_count > 256:
            self.room_count = 256
            self.x_array = [[True for y in range(16)] for x in range(16)]
            self.create_paths(self.room_count, self.x_array)
        else:
            self.x_array = [[False for y in range(16)] for x in range(16)]
            self.room_array = [[False for y in range(16)] for x in range(16)]
            self.create_paths(self.room_count, self.x_array)
            
    def create_paths(self, room_count, x_array):
        #initializes start point for dungeon paths
        x_start = randint(0, 15)
        y_start = randint(0, 15)
        self.x_array[x_start][y_start] = True
        self.start = [x_start, y_start]

        while self.rooms_remaining > 0:
            self.next_room(self.start[0], self.start[1])
            
    def next_room(self, x, y):
        directions = [False, False, False, False]
        
        #checks for existing rooms around coordinates, accounts for the possibility of being out of bounds
        # if no existing room adjacent, creates new room
        try:
            if self.x_array[x][y+1]:
                directions[0] = True
            else:
                if self.rooms_remaining > 0:
                    directions[0] = self.rand_exit()
                    if directions[0]:
                        self.x_array[x][y+1] = True
                        self.rooms_remaining -= 1
                        self.next_room(x, y+1)                   
        except IndexError:
            pass
        try:
            if self.x_array[x+1][y]:
                directions[1] = True
            else:
                if self.rooms_remaining > 0:
                    directions[1] = self.rand_exit()
                    if directions[1]:
                        self.x_array[x+1][y] = True
                        self.rooms_remaining -= 1
                        self.next_room(x+1, y)
        except IndexError:
            pass        
        try:
            if y > 0:
                if self.x_array[x][y-1]:
                    directions[2] = True
                else:
                    if self.rooms_remaining > 0:
                        directions[2] = self.rand_exit()
                        if directions[2]:
                            self.x_array[x][y-1] = True
                            self.rooms_remaining -= 1
                            self.next_room(x, y-1)
        except IndexError:
            pass        
        try:
            if x > 0:
                if self.x_array[x-1][y]:
                    directions[3] = True
                else:
                    if self.rooms_remaining > 0:
                        directions[3] = self.rand_exit()
                        if directions[3]:
                            self.x_array[x-1][y] = True
                            self.rooms_remaining -= 1
                            self.next_room(x-1, y)
        except IndexError:
            pass
            
        #Inserts actual room to array
        self.room_array[x][y] = Room(directions)

                    
    def rand_exit(self):
        rexit = randint(0, 1)
        if rexit == 1:
            return True
        else:
            return False
            
    def gen_printable(self):
        lines = []
        self.count = 0
        for y in range(16):
            temp = ''
            for x in range(16):
                if self.x_array[x][y] == False:
                    temp += ' - '
                else:
                    temp += " X "
                    self.count += 1
            lines.append(temp)
        self.printable = '\n'.join(lines)
            
            

class Dungeon:
    def __init__(self):
        
        return
        
    def add_room(self, room):
        return
        
class Room:
    def __init__(self, directions):
        self.directions = directions
        self.is_visited = False
        self.cleared = False
        self.event_selector = randint(0, 100)
        self.event = Event(self.event_selector)
        
        
    def visit(self):
        self.is_visited = True
        
    def complete(self):
        self.cleared = True
        
    def get_interaction:
        return self.event.interaction

class Event:
    def __init__(self, event_selector):
        self.index = index
        self.event_type = None
        contents = None
        self.interaction = None
        
        # Type categories: 0-70: Creature encounters
        # 71-85: Treasure encounters
        # 86-95: Equipment vaults
        # 96-100: Specialty encounters
        
        if type_selector <= 70:
            self.contents = self.get_creature()
            self.description = self.contents.description
            self.actions = self.contents.actions
            self.value = self.contents.value
            self.interaction = Interaction(self.description, self.actions, self.value)
        elif type_selector <= 85:
            self.contents = self.get_treasure
            self.description = self.contents.description
            self.actions = self.contents.actions
            self.value = self.contents.value
            self.interaction = Interaction(self.description, self.actions, self.value)
        elif type_selector <= 95:
            self.contents = self.get_vault
            self.description = self.contents.description
            self.actions = self.contents.actions
            self.value = self.contents.value
            self.interaction = Interaction(self.description, self.actions, self.value)
        else:
            self.contents = self.get_specialty
            self.description = self.contents.description
            self.actions = self.contents.actions
            self.value = self.contents.value
            self.interaction = Interaction(self.description, self.actions, self.value)
            
            
        #print("Type selector = " + str(type_selector))
        #print("Event type is " + self.event_type + "\n")
        
    def get_creature(self):
        creature = creatures[randint(0, len(creatures)-1]
        return creature
        
    def get_treasure(self):
        treasure = treasures[randint(0, len(treasures)-1]
        return treasure
    
    def get_vault(self):
        vault = vaults[randint(0, len(vaults)-1]
        return vault
        
    def get_specialty(self):
        specialty = specialties[randint(0, len(specialties)-1]
        return specialty
    
class Interaction:
    def __init__(self, description, actions, value):
        self.description = description
        self.actions = actions
        self.value = value
        
        

class Chest:
    def __init__(self):
        self.items = []
        self.num_items = randint(2, 5)
        for x in range(self.num_items):
            self.items.append(items[randint(0, 100)])
            
class Vault:
    def __init__(self):
        self.items = []
        self.num_items = randint(3, 8)
        for x in range(self.num_items):
            self.items.append(items[randint(0, 100)]
            
    
    
    #def random_event(self, index):


#event1 = Event(2)
#event2 = Event(1)
#event3 = Event(3)    