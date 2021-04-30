def val_iter(state_dict):
    for state in state_dict.values():
        if deterministic:
            V = max()
            state.value = V
        else:
            all_actions = [(state.value + state.tran_val) for state in self.neighbors if state != None]
            most_rewarding = max(all_actions)
            other = all_actions.copy()
            other.remove(most_rewarding)
            weighted_actions = (most_rewarding *  0.7) + statistics.mean(other) * 0.3
            state.value = weighted_actions
