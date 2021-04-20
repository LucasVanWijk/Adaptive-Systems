from statistics import mean
class State_Class():
    def __init__(self, pos, tran_val,value=0, agent_in_cell=False, is_final=False):
        self.pos = pos
        self.tran_val = tran_val
        self.value = value
        self.agent_in_cell = agent_in_cell
        self.neigbors = None

    def get_new_val(self):
        if self.neigbors is not None:
            return max(self.det_values_for_all_actions())
        else:
            return 0
    
    def det_values_for_all_actions(self):
        pass

    def __repr__(self):
        if self.agent_in_cell:
            return "[{}]".format(self.value)
        else:
            return "{}".format(self.value)
    



class State_Determenistic(State_Class):
    def __init__(self, pos, tran_val,value=0, agent_in_cell=False, is_final=False):
        super().__init__(pos, tran_val,value, agent_in_cell, is_final)
    
    def det_values_for_all_actions(self):
        return [(agent.value + agent.tran_val) for agent in self.neigbors if agent != None]


class State_Non_Determenistic(State_Class):
    def __init__(self, pos, tran_val,value=0, agent_in_cell=False, is_final=False):
        super().__init__(pos, tran_val,value, agent_in_cell, is_final)
    
    def det_values_for_all_actions(self):
        all_actions = [(agent.value + agent.tran_val) for agent in self.neigbors if agent != None]
        weighted_actions = []
        for action in all_actions:
            other = all_actions.copy()
            other.remove(action)
            weighted_actions.append(action*0.7 + mean(other)*0.3)
        
        return weighted_actions
