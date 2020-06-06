
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
        action = self.agent.act(state)
        self.env.step(action)

        if self.is_train:
            self.agent.update_replay_memory(self.prev_state, self.prev_action, reward, state)
