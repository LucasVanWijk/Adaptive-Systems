# AS

##Structure
In opdracht 1 theorie is the theory part of this assignment (in dutch). 
In 1_4.py is the code I used to do the value iteration of 1.4 by hand.
The rest is the code for 3.0 and onwards.

##The code
The code works as follows

Create a dictionary of all possible states.
  (Where the key is the position of the state and it’s value a instance of the state class).
Assign every state a list of neighboring states a agent can transition to.
Create a instance of the world class.
Pass it the dictionary of all the states.
Call the value_iteration function of the world class.
 
##Notes
All functions and classes have docstrings explaining how they work.
Problem specific logic is disconnect as much as possible form the world and state classes to ensure reusability.
Only State_Non_Determenistic contains problem specific logic in the way it calculates the value of all possible actions. 
For any new deterministic problem no new state logic needs to be written. 
For a new non deterministic problem one only needs to create a new child class of the state class that implements det_value_for_all_actions for this specific problem.
In both cases a new function to assing neigbors to states needs to be written

