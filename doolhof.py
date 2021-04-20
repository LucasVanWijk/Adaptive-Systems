from mesa import Agent, Model
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.space import MultiGrid
from mesa.time import RandomActivation

doolhof = [[-1,-1,-1,40], [-1,-1,-10,-10], [-1,-1,-1,-1], [10,-2,-1,-1]]
grid = CanvasGrid(portrayal, 4, 4, 500, 500)

class MoveAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

class StateAgent():
    """The agent of a state"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model, value)
        self.value = value

    def move(self):
        possible_steps = self.model.grid.get_neighbors(
            self.pos,
            moore=False,
            include_center=False)
        neighbor_values = [state.value]
        

class Model(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(4, 4, True)
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()


server = ModularServer(MoneyModel,
                       [grid],
                       "Money Model",
                       {"N":100, "width":10, "height":10})
server.port = 8521 # The default
server.launch()