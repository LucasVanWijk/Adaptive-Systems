import State
import Policy
from World import World_Class

def create_states(class_type,
                  trans_values=[-1,-1,-1,40, -1,-1,-10,-10, -1,-1,-1,-1, 10,-2,-1,-1]):
    """Creates a dict of states

    Args:
        class_type (Class (State)): The class of states that need to be created
        trans_values (list): The value a agent would get if it entered this state. 
                             Ordered on occurrence

    Returns:
        [dict]: a dict where the position is the key.
                and it's value the agent at that state.
    """

    # The reward a agent would get for moving to this state
    
    val_iter = 0
    states = {}

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

def create_maze_states(state_type):
    states = create_states(state_type)
    for state in states.values():
        # 0_3", "3_0 are final states and should have no neighbors
        if state.pos not in ["0_3", "3_0"]:
            state.neighbors = set_neighbors(state.pos, states)
    
    return states

states = create_maze_states(State.State_Non_Deterministic)
world_value_iterations = World_Class(states)
world_value_iterations.value_iterations(100, [100])

states = create_maze_states(Policy.Monte_State)
world_monte_carlo = World_Class(states)

random_policy = {}
for state in states.values():
    random_policy[state.pos] = state.neighbors

world_monte_carlo.monte_carlo(random_policy, nmb_iterations=50000, print_interval=[0,1,50000])
