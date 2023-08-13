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
        
        for i in range(nmb_iterations):
            for state in self.state_dict.values():
                state.value = state.get_new_val()
            if i in print_interval:
                print(i)
                self.print_world()
        return self.state_dict
    
    def print_world(self):
        """Prints a representation of the world
        """
        base = ""
        for i in range(4):
            for ii in range(4):
                base += "   " + self.state_dict[f"{i}_{ii}"].__repr__() + "    "
            print(base)
            base = ""
