from copy import deepcopy

class state():
    def __init__(self, pos, tran_val,value=0, agent_in_cell=False):
        self.pos = pos
        self.tran_val = tran_val
        self.value = value
        self.agent_in_cell = agent_in_cell
    
    def set_neigbors(self, all_agents):
        self.neigbors = [all_agents.get("{}_{}".format(int(self.pos[0]) -1, self.pos[2])), #Left 
                        all_agents.get("{}_{}".format(self.pos[0], int(self.pos[2]) +1)),  #Up
                        all_agents.get("{}_{}".format(int(self.pos[0]) +1, self.pos[2])),  #Right
                        all_agents.get("{}_{}".format(self.pos[0], int(self.pos[2]) -1)),] #Down

    def get_new_val(self):
        vals = []
        for agent in self.neigbors:
            if agent != None:
                vals.append(agent.value + agent.tran_val)
            else:
                pass

        return max(vals)
    
    def __repr__(self):
        if self.agent_in_cell:
            return "[{}]".format(self.value)
        else:
            return "{}".format(self.value)

def print_world(all_agents):
    base = ""
    for i in range(4):
        for ii in range(4):
            base += "   " + all_agents[f"{i}_{ii}"].__repr__() + "    "
        print(base)
        base = ""

doolhof = [-1,-1,-1,40, -1,-1,-10,-10, -1,-1,-1,-1, 10,-2,-1,-1]
val_iter = 0
agent_dict = {}
for i in range(4):
    for ii in range(4):
        pos = f"{i}_{ii}"
        agent_dict[pos] = state(pos, doolhof[val_iter])
        val_iter += 1



for i in range(10):
    print(i)
    new_agent_dict = {}
    for agent in agent_dict.values():
        agent.set_neigbors(agent_dict)
    
    for agent in agent_dict.values():
        update_agent = deepcopy(agent)
        update_agent.value = agent.get_new_val()
        new_agent_dict[agent.pos] = update_agent

    
    print_world(new_agent_dict)
    agent_dict = new_agent_dict.copy()