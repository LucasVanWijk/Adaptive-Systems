import State
from World import World_Class

def create_states(deterministic=True):
    """[summary]

    Args:
        deterministic (bool, optional): Specifies if the behavior of the agent
                                        in this state should be deterministic or not. 
                                        Defaults to True.

    Returns:
        List: A list of all the states a agent can be in
    """

    # The reward a agent would get for moving to this state
    trans_values = [-1,-1,-1,40, -1,-1,-10,-10, -1,-1,-1,-1, 10,-2,-1,-1]
    val_iter = 0
    states = {}
    if deterministic:
        class_type = State.State_Deterministic
    else:
        class_type = State.State_Non_Deterministic
    
    for i in range(4):
        for ii in range(4):
            pos = f"{i}_{ii}"
            states[pos] = class_type(pos, trans_values[val_iter])
            val_iter += 1
            
    return states

def set_neighbors(pos, all_agents):
    """For a state at a given position returns a list of it's neighbors

    It is implemented in main and not in the state class because to logic to assigning neighbors is problem specific.
    The code below works for a grid but not for a network. 
    Keeping this logic out of the state class ensures the state class can also be applied to network other problems.
    As long as a set_neighbors function for that probelm is worked out.

    Args:
        pos (string): the coordinate position of a state
        all_agents (dict): a dict where the key is the coordinate position and it's value is the state occupying that position

    Returns:
        [list]: A list of the neighbors of the state
    """
    neighbors = [all_agents.get("{}_{}".format(int(pos[0]) -1, pos[2])),  #Left 
                all_agents.get("{}_{}".format(pos[0], int(pos[2]) +1)),  #Up
                all_agents.get("{}_{}".format(int(pos[0]) +1, pos[2])),  #Right
                all_agents.get("{}_{}".format(pos[0], int(pos[2]) -1)),] #Down
    
    return neighbors


states = create_states(deterministic=False)
for state in states.values():
    # 0_3", "3_0 are final states and should have no neighbors
    if state.pos not in ["0_3", "3_0"]:
        state.neighbors = set_neighbors(state.pos, states)

world_instance = World_Class(states)
world_instance.value_iterations(1000, [1,2,5,10,25,50, 75, 100] + list(range(100, 1000, 200)))