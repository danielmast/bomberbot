import time

import controls
from constants import *

env = None

class Env:
    def __init__(self):
        self.started = False
        self.state = None
        self.return_value = 0

    def update(self, state):
        self.started = True
        self.state = state
        self.return_value = self.return_value + self.state['reward']
        print('return', self.return_value)

    def step(self, action):
        assert action < action_size

        if not self.started:
            time.sleep(0.2)
            return

        # perform the action
        controls.do_action(action)
        return None