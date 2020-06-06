import numpy as np

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
        state_array = np.zeros((12, 14, 7))
        return state_array
