from dataclasses import dataclass
import random
import statistics


@dataclass
class State():
    """A representation of the state a agent can be in

    Args:
        pos (str): The coordinate position of the state in the maze. 
                   Also functions as the id of the string.
        value (float): The value or utility of the state.
        trans_value (int): The reward a agent recieves for moving into this state.
        is_end_state (bool): Boolean representing if the state is a final state.
        neighbors (list): A list of all posible states accesible from this state.
    """

    pos: str
    value: float
    trans_value: int
    is_end_state = False
    neighbors = []

    def __repr__(self):
        return str(round(self.value, 2))


class Agent():
    """A agent who tries to find the optimal way trough a maze.
    
    Args:
        current_state (State): the current state the agent is in.
        policy (dict): A dict where the key is the coordinate position of the state (aka id), 
                       and and the value is a list containing the states it is suppoded to move to.
                       If there is only one optimal action (according to this policy) the list will have one element.
                       If there are multiple actions who are equally optimal the list will have more elements.
        visits (list): A list of all the states this agents has visited this episode
        deterministic (bool): A boolean representing if the agents acts determenistic. 
                             (if it always preforms the actions it wants to).
        gamma (float): The chanse (as a factor) that a agent preforms a actions that it determins not optmial.
    """
    def __init__(self, current_state, policy,
                 deterministic=False, gamma=0.3):
        self.current_state = current_state
        self.policy = policy
        self.visits = [current_state]
        self.deterministic = deterministic
        self.gamma = gamma

    def next_state(self):
        preferred_next_state_loc = random.choice(self.policy[self.current_state.pos]).pos
        for state in self.current_state.neighbors:
            if state.pos == preferred_next_state_loc:
                preferred_next_state = state
        
        if not self.deterministic and (random.randint(0, 100) < self.gamma*100):
            other = self.current_state.neighbors.copy()
            other.remove(preferred_next_state)
            preferred_next_state = random.choice(other)

        self.current_state = preferred_next_state
        self.visits += [self.current_state]

    def run_sim(self):
        is_final = self.current_state.is_end_state
        while not is_final:
            self.next_state()
            is_final = self.current_state.is_end_state

        return self.visits


def get_neighbors(world, state_id):
    """For a state at a given position returns a list of it's neighbors

    Args:
        world (dict): a dict where the key is the coordinate position and it's value is the state occupying that position
        state_id (string): the id (coordinate location) of the state

    Returns:
        [list]: A list of the neighbors which are accessible
    """
    list_of_neighbors_ids = [f"{int(state_id[0]) -1}_{state_id[2]}",   # Left
                             f"{state_id[0]}_{int(state_id[2]) + 1}",  # Up
                             f"{int(state_id[0]) +1}_{state_id[2]}",   # Right
                             f"{state_id[0]}_{int(state_id[2]) -1}"]  # Down

    # Filters out all the non existing neighbors
    return [world.get(id) for id in list_of_neighbors_ids if world.get(id) is not None]


def create_maze(maze_dimmensions=[4, 4],
                trans_val_list=[-1, -1, -1, 40,
                                -1, -1, -10, -10,
                                -1, -1, -1, -1,
                                10, -2, -1, -1],

                end_states=["0_3", "3_0"]):

    
    maze = {}
    i = 0
    for length in range(maze_dimmensions[0]):
        for width in range(maze_dimmensions[1]):
            loc = f"{length}_{width}"
            cell_state = State(loc, 0, trans_val_list[i])
            if loc in end_states:
                cell_state.is_end_state = True

            maze[loc] = cell_state
            i += 1

    for value in maze.values():
        value.neighbors = get_neighbors(maze, value.pos)

    return maze


def value_iterations(state_dict, nmb_iterations, print_interval=[],
                     deterministic=False, gamma=0.3):
    for i in range(nmb_iterations):
        for state in state_dict.values():
            if not state.is_end_state:
                neighbors = state.neighbors
                reward = lambda state: state.value + state.trans_value
                all_actions = [reward(state) for state in neighbors if state != None]
                if deterministic:
                    state.value = max(all_actions)
                else:
                    weighted_actions = []
                    for action in all_actions:
                        other = all_actions.copy()
                        other.remove(action)
                        weighted_action = action*(1-gamma) + statistics.mean(all_actions)*gamma
                        weighted_actions.append(weighted_action)
                    state.value = max(weighted_actions)

        if i in print_interval:
            print("\n\n")
            print(f"{state_dict['0_0']}     {state_dict['0_1']}             {state_dict['0_2']}             {state_dict['0_3']}")
            print(f"{state_dict['1_0']}     {state_dict['1_1']}             {state_dict['1_2']}             {state_dict['1_3']}")
            print(f"{state_dict['2_0']}     {state_dict['2_1']}             {state_dict['2_2']}             {state_dict['2_3']}")
            print(f"{state_dict['3_0']}     {state_dict['3_1']}             {state_dict['3_2']}             {state_dict['3_3']}")

    return state_dict


def extract_policy(state_dict):
    policy = {}
    reward = lambda state: state.value + state.trans_value
    for key in state_dict:
        neighbors = state_dict[key].neighbors
        reward_optimal_action = 0
        for neighbor in neighbors:
            reward_neighbor = reward(neighbor)
            if reward_optimal_action < reward_neighbor:
                policy[key] = [neighbor]
            elif reward_optimal_action == reward_neighbor:
                policy[key] += [neighbor]
            reward_optimal_action = reward(policy[key][0])

    return policy


def mcpe(state_dict, policy, deterministic=False,
         nmb_iterations=25, print_interval=None, gamma=1):

    if print_interval is None:
        print_interval = [nmb_iterations-1]

    returns = {key: [0] for key in state_dict.keys()}
    for i in range(nmb_iterations+1):
        random_pos = random.choice(list(state_dict.keys()))
        start_state = state_dict[random_pos]        
        episode = Agent(start_state, policy, deterministic).run_sim()
        episode.reverse()
        T = episode

        # Because for the first iteration would result in 0*gamma + reward,
        # and the final state can not be visited more than once.
        # The first iteration can be simplefied to a one liner.
        # This wil also prevent the function form trying to assing a value to a final state
        G = T.pop(0).trans_value
        while len(T):
            St = T.pop(0)
            # If the same state is not in T afther removing it.
            # It is the first visit
            if St not in T:
                G = G*gamma + St.trans_value
                returns[St.pos] += [G]

        for key in returns.keys():
            # In the pseuodo code state_dict is noted as V
            state_dict[key].value = statistics.mean(returns[key])

    print("\n\n")
    print(f"{state_dict['0_0']}     {state_dict['0_1']}             {state_dict['0_2']}             {state_dict['0_3']}")
    print(f"{state_dict['1_0']}     {state_dict['1_1']}             {state_dict['1_2']}             {state_dict['1_3']}")
    print(f"{state_dict['2_0']}     {state_dict['2_1']}             {state_dict['2_2']}             {state_dict['2_3']}")
    print(f"{state_dict['3_0']}     {state_dict['3_1']}             {state_dict['3_2']}             {state_dict['3_3']}")


maze = create_maze()
itert = value_iterations(maze, 50, print_interval=[], deterministic=True)
policy = extract_policy(itert)
mcpe(create_maze(), policy, nmb_iterations = 1000, deterministic=True)
