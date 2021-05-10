class Agent():
    def __init__(self, current_state, policy, deterministic=False):
        self.current_state = current_state
        self.policy = policy
        self.visits = [current_state]
        self.deterministic = deterministic
    
    def next_state(self):
        if self.current_state.neighbors != None:
            preferred_next_state = random.choice(self.policy[self.current_state.pos])
            if not self.deterministic:
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
