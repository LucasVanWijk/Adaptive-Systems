from ..Assingment_1.Maze.State import State_Class, State_Deterministic, State_Non_Deterministic
from ..Assingment_1.Maze.Main import create_states, set_neighbors,create_maze
from ..Assingment_1.Maze.World import World_Class
import tqdm
import random


def extract_policy(state_dict):
    new_state_dict = {}
    for key in state_dict.keys():
        x, y = key.split("_")
        
        actions =[("Left", state_dict.get(f"{x-1}_{y}")), ("Right", state_dict.get(f"{x+1}_{y}"))
                  ("Up", state_dict.get(f"{x}_{y+1}")), ("Down", state_dict.get(f"{x}_{y-1}"))]
        action = actions.sort(key=lambda a: a[1])[0]
        new_state_dict = {key: action}
    return new_state_dict


def run_policy(location, policy, world_states, succes_chanse, end_states):
    done = False
    vistited_states = []
    rewards = []
    while done == False:
        vistited_states.append(location)
        rewards.append(world_states[location].reward)
        x, y = location.split("_")
        choice = policy[location]
        if random.randint(succes_chanse, 10):
            choices = ["Left", "Right", "Up", "Down"] - [choice]
            choice = random.choice(choices)
        
        if choice == "Left":
            new_loc = world_states.get{f"{x-1}_{y}"}
        if choice == "Right":
            new_loc = world_states.get{f"{x+1}_{y}"}
        if choice == "Up":
            new_loc = world_states.get{f"{x}_{y+1}"}
        if choice == "Down":
            new_loc = world_states.get{f"{x}_{y-1}"}
        
        if new_loc is not None:
            location = new_loc
            done = if location in end_states



    





class monte_carlo_policy(World_Class):
    def __init__(self, state_dict):
        super().__init__(state_dict)
    
    def monte_carlo(self, policy, n_episodes, discount_factor, print_interval=None):
        """ Evaluate a policy by using the `run_episode` method.
        :param policy: A policy to be evaluated.
        :param n_episodes: Number of episodes to be used for evaluation.
        :param discount_factor: Gamma discount factor.
        :return: A list containing the cumulative rewards of each episode.
        """
        returns_sum = []
        returns_count = []

        V = []

        for _ in tqdm(range(1, n_episodes + 1)):
            # Generate an episode by running the run method this returns states, actions and rewards.
            states, rewards = run_policy()
            G = 0
            states = episode[0]
            rewards = episode[2]
            for idx in range(len(states) - 2, 0, -1):
                curr_state = states[idx]
                G = discount_factor * G + rewards[idx + 1]
                if curr_state not in states[:idx - 1]:
                    returns_sum[curr_state] += G
                    returns_count[curr_state] += 1.0
                    V[curr_state] = returns_sum[curr_state] / returns_count[curr_state]
            self.reset()
        return V

