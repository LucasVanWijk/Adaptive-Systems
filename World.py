import random
import statistics


class Agent():
    def __init__(self, current_state, policy, deterministic=False):
        self.current_state = current_state
        self.policy = policy
        self.visits = [current_state]
    
    def next_state(self):
        if self.current_state.neighbors != None:
            preferred_next_state = random.choice(self.policy[self.current_state.pos])
            if not deterministic:
                if random.randint(0,100) < 30:
                    other = self.current_state.neighbors.copy()
                    other.remove(preferred_next_state)
                    preferred_next_state = random.choice(other)
            
            if preferred_next_state != None:
                self.current_state = preferred_next_state

            self.current_state.visited += 1
            self.visits = self.visits + [self.current_state]
    
    def run_sim(self):
            is_final = False
            while not is_final:
                self.next_state()
                if self.current_state.neighbors == None:
                    is_final = True
            
            return self.visits


class World_Class():
    def __init__(self, state_dict):
        self.state_dict = state_dict # A dict of all states in this world
    
    def value_iterations(self, nmb_iterations=25, print_interval=None):
        """Iterates over all the states and assigns it a new value according to the theory of value iteration.

        Args:
            nmb_iterations (int, optional): The number of iterations. Defaults to 25.
            print_interval ([type], optional): A list with all the iteration numbers
                                               at which the world needs to be printed. 
                                               Defaults to None.
        """
        if print_interval == None:
            print_interval = [nmb_iterations-1]
        
        for i in range(nmb_iterations+1):
            for state in self.state_dict.values():
                state.value = state.get_new_val()
            if i in print_interval:
                print(i)
                self.print_world()
        
        return self.state_dict
    
    def monte_carlo(self, policy, nmb_iterations=25, print_interval=None, discount=1):
        """Iterates over all the states and assigns it a new value according to the theory of value iteration.

        Args:
            nmb_iterations (int, optional): The number of iterations. Defaults to 25.
            print_interval ([type], optional): A list with all the iteration numbers
                                               at which the world needs to be printed. 
                                               Defaults to None.
        """
        if print_interval == None:
            print_interval = [nmb_iterations-1]
        
        for i in range(nmb_iterations+1):
            random_pos = random.choice(list(self.state_dict.keys()))
            start_state = self.state_dict[random_pos]            
            visits = Agent(start_state, policy).run_sim()
            visits.reverse()
            G = 0
            new_reward_dict = {key: [] for key in self.state_dict.keys()}
            for visit in visits:
                new_reward_dict[visit.pos] += [G]
                G += visit.tran_val
            
            for key in new_reward_dict.keys():
                state_visits = new_reward_dict[key]
                if len(state_visits) > 0:
                    self.state_dict[key].value = statistics.mean(state_visits)

            if i in print_interval:
                print(i)
                # for v in visits:
                #     print(v.pos)
                self.print_world()
    
    def print_world(self):
        """Prints a representation of the world """
        base = ""
        for i in range(4):
            for ii in range(4):
                base += "   " + self.state_dict[f"{i}_{ii}"].__repr__() + "    "
            print(base)
            base = ""
