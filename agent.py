import numpy as np

from constants import action_size


class Agent(object):
  def __init__(self):
    pass

  def act(self, state):
    return np.random.choice(action_size)
