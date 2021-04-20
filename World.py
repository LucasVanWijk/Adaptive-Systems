class World_Class():
    def __init__(self, agent_dict):
        self.agent_dict = agent_dict
    
    def iter(self, nmb_iterations=25, print_interval=None):
        if print_interval == None:
            print_interval = [nmb_iterations-1]
        
        for i in range(nmb_iterations):
            
            for agent in self.agent_dict.values():
                # Note agent is a pointer to a instance. 
                # If you modify agent you also modify the corresponding value in the agent_dict 
                agent.value = agent.get_new_val()
            if i in print_interval:
                print(i)
                self.print_world()
    
    def print_world(self):
        base = ""
        for i in range(4):
            for ii in range(4):
                base += "   " + self.agent_dict[f"{i}_{ii}"].__repr__() + "    "
            print(base)
            base = ""
