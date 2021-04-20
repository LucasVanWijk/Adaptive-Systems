import State
from World import World_Class

def create_states(determenistic=True):
    trans_values = [-1,-1,-1,40, -1,-1,-10,-10, -1,-1,-1,-1, 10,-2,-1,-1]
    val_iter = 0
    states = {}
    if determenistic:
        class_type = State.State_Determenistic
    else:
        class_type = State.State_Non_Determenistic
    
    for i in range(4):
        for ii in range(4):
            pos = f"{i}_{ii}"
            states[pos] = class_type(pos, trans_values[val_iter])
            val_iter += 1
            
    return states

def set_neigbors(pos, all_agents):
    neigbors = [all_agents.get("{}_{}".format(int(pos[0]) -1, pos[2])),  #Left 
                all_agents.get("{}_{}".format(pos[0], int(pos[2]) +1)),  #Up
                all_agents.get("{}_{}".format(int(pos[0]) +1, pos[2])),  #Right
                all_agents.get("{}_{}".format(pos[0], int(pos[2]) -1)),] #Down
    
    return neigbors

#states = create_states()
states = create_states(determenistic=False)
for state in states.values():
    if state.pos not in ["0_3", "3_0"]:
        state.neigbors = set_neigbors(state.pos, states)

world_instance = World_Class(states)
world_instance.iter(1000, [1,2,5,10,25,50, 75, 100] + list(range(100, 1000, 200)))