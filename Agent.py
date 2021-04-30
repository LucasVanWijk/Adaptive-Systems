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

def create_policy(policy_type, deterministic, state_dict):
    if policy_type == "random":
        policy = {}
        for key in state_dict:
            policy[key] = state_dict[key].neighbors
        return policy
    
    if policy_type == "greedy":
        if deterministic:
            all_possible_actions = state_dict[key].neighbors
            most_rewarding = max(all_possible_actions)
            policy[key] = most_rewarding
        
        # else:
        #     for key in state_dict:
        #         all_possible_actions = state_dict[key].neighbors
        #         most_rewarding = max(all_possible_actions)
        #         other = all_actions.copy()
        #         other.remove(most_rewarding)
        #         weighted_actions = ([most_rewarding] *  7) + other
        #         policy[key] = weighted_actions
        #     return policy

    
