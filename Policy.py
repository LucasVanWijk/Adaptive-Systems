from State import State_Class

class Monte_State(State_Class):
    def __init__(self, pos, tran_val,value=0, state_in_cell=False, is_final=False):
        super().__init__(pos, tran_val,value, state_in_cell, is_final)
        self.visited = 0
    
    def get_new_val(self, value):
        return (self.value * self.visited + value) / (self.visited+1)
