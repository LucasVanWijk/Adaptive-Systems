from statistics import mean
class State_Class():
    """A universal state class usable in all MRP problems
    """
    def __init__(self, pos, tran_val,value=0, state_in_cell=False, is_final=False):
        self.pos = pos
        self.tran_val = tran_val
        self.value = value
        self.state_in_cell = state_in_cell
        self.neighbors = None

    def get_new_val(self):
        """Returns the maximum value (reward + value of next state * discount value)
        of all actions

        Returns:
            [int]: Returns the highest value out of all possible actions
        """
        if self.neighbors is not None:
            return max(self.det_values_for_all_actions())
        else:
            return 0
    
    def det_values_for_all_actions(self):
        """Calculate the reward of all possible actions. 
        Because this is problem specific this function is empty in state_class
        and needs to be implemented in a child class
        """
        pass

    def __repr__(self):
        """Returns the representation of the class. (This will be shown in print)

        Returns:
            [string]: The string representation of the class
        """
        if self.state_in_cell:
            return "[{}]".format(self.value)
        else:
            return "{}".format(self.value)
    



class State_Deterministic(State_Class):
    """Implemantation of the state the agent would act deterministically. Universal for all deterministic problems 

    Args:
        State_Class (Parent Class): The parent class this state should inherit logic form
    """
    def __init__(self, pos, tran_val,value=0, state_in_cell=False, is_final=False):
        super().__init__(pos, tran_val,value, state_in_cell, is_final)
    
    def det_values_for_all_actions(self):
        """Calculate the reward of all possible actions. 

        Returns:
            [List]: A list of the rewards for all possible actions
        """
        return [(state.value + state.tran_val) for state in self.neighbors if state != None]


class State_Non_Deterministic(State_Class):
    def __init__(self, pos, tran_val,value=0, state_in_cell=False, is_final=False):
        super().__init__(pos, tran_val,value, state_in_cell, is_final)
    
    def det_values_for_all_actions(self):
        """Calculate the reward of all possible actions. 

        Returns:
            [List]: A list of the rewards for all possible actions
        """

        all_actions = [(state.value + state.tran_val) for state in self.neighbors if state != None]
        weighted_actions = []
        for action in all_actions:
            other = all_actions.copy()
            other.remove(action)
            weighted_actions.append(action*0.7 + mean(other)*0.3)
        
        return weighted_actions
