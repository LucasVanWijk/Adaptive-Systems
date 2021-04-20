import random
doolhof = [[-1,-1,-1,40], [-1,-1,-10,-10], [-1,-1,-1,-1], [10,-2,-1,-1]]

def agent():
    def __init__(self, pos, world, value):
        self.pos = pos
        self.world = world
        self.value = value
    
    def determin_action(self):
        actions = {"right": 0, "left": 0, "up": 0, : "down": 0}
        if pos[0] == 4 or pos[0] == 0:
            if pos[0] == 4:
                actions["right"] = value
                actions["left"] = world[self.pos[1]]self.pos[0]-1
            else:
                actions["right"] = world[self.pos[1]]self.pos[0]+1
                actions["left"] = value
        else:
            actions["right"] = world[self.pos[1]]self.pos[0]+1
            actions["left"] = world[self.pos[1]]self.pos[0]-1
        
        if pos[1] == 4 or pos[1] == 0:
            if pos[0] == 4:
                actions["down"] = value
                actions["up"] = world[self.pos[1] +1]self.pos[0]
            else:
                actions["down"] = world[self.pos[1]-1]self.pos[0]
                actions["up"] = value
        else:
            actions["down"] = world[self.pos[1] -1]self.pos[0]
            actions["up"] = world[self.pos[1] +1]self.pos[0]

        chosen_action =  max(actions, key=actions.get)
        other = list(set(["right, left, up , down")] - set([chosen_action]))
        if random.randint(0,100) > 30:
            return chosen_action
        else:
            random.random_choice(other)
    
    def move(self):
        