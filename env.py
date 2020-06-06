import controls
from constants import *

env = None

class Env:
    def __init__(self):
        self.return_value = 0

    def update_return_value(self, state):
        self.return_value = self.return_value + state['reward']
        print('return', self.return_value)

    def step(self, action):
        assert action < action_size

        # perform the action
        controls.do_action(action)
        return None