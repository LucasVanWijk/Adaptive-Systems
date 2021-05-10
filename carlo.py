def monte_carlo(self, policy, nmb_iterations=25, print_interval=None, discount=1):
    """Iterates over all the states and assigns it a new value according to the theory of value iteration.

    Args:
        nmb_iterations (int, optional): The number of iterations. Defaults to 25.
        print_interval ([type], optional): A list with all the iteration numbers
                                            at which the world needs to be printed. 
                                            Defaults to None.
    """
    if print_interval == None:
        print_interval = [nmb_iterations-1]
    
    for i in range(nmb_iterations+1):
        random_pos = random.choice(list(self.state_dict.keys()))
        start_state = self.state_dict[random_pos]            
        visits = Agent(start_state, policy).run_sim()
        visits.reverse()
        G = 0
        counter = 1
        new_reward_dict = {key: 0 for key in self.state_dict.keys()}
        for visit in visits:
            new_reward_dict[visit.pos] = G * (discount**counter)
            G += visit.tran_val
            
        
        for visit in visits:
            if visit.value != 0:
                old_weighted_value = visit.value * visit.num_first_visit
                visit.value = (old_weighted_value + new_reward_dict[visit.pos]) / (visit.num_first_visit +1) 
            else:
                visit.value = new_reward_dict[visit.pos]
            
            visit.num_first_visit += 1
        # for key in new_reward_dict.keys():
        #     state_visits = new_reward_dict[key]

        if i in print_interval:
            print(i)
            # for v in visits:
            #     print(v.pos)
            print([visit.pos for visit in visits])
            self.print_world()