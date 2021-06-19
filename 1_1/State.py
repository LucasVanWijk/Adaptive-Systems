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
        self.num_first_visit = 0

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
    
    def __gt__(self, other):
        if other is None:
            return self.value
        else:
            return self.value > other.value
