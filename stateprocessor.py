import numpy as np

from constants import state_dim

stateprocessor = None

class Stateprocessor():
    def __init__(self, agent, env, is_train):
        self.agent = agent
        self.env = env
        self.is_train = is_train
        self.prev_state = None
        self.prev_action = None
        self.prev_reward = None


    def process_state(self, state):
        reward = state['reward']
        self.env.update_return_value(reward)
        state_array = self.state_array(state)
        action = self.agent.act(state_array)
        self.env.step(action)

        if self.is_train:
            self.agent.update_replay_memory(self.prev_state, self.prev_action, reward, state)

    def state_array(self, state):
        """ Converts JSON state to numpy array """
        state_array = np.zeros(state_dim)

        p0 = state['players'][0]
        state_array[0, p0['y'], p0['x']] = 1

        p1 = state['players'][1]
        state_array[1, p1['y'], p1['x']] = 1

        for pu in state['powerups']:
            state_array[2, pu['y'], pu['x']] = 1

        for b in state['bombs']:
            state_array[3, b['y'], b['x']] = 1

        for e in state['explosions']:
            state_array[4, e['y'], e['x']] = 1

        for b in state['barrels']:
            state_array[5, b['y'], b['x']] = 1

        for w in state['walls']:
            state_array[6, w['y'], w['x']] = 1

        return state_array
