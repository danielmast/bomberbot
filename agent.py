import numpy as np

from constants import action_size

class Agent():
  def __init__(self):
    pass

  def act(self, state):
    return np.random.choice(action_size)

  def update_replay_memory(self, state, action, reward, next_state):
    pass