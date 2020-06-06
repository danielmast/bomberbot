import numpy as np



class Agent():
  def __init__(self, state_size, action_size):
    self.action_size = action_size
    self.epsilon = 1.0
    self.model = mlp(state_size, action_size)

  def act(self, state):
    if np.random.rand() <= self.epsilon:
      return np.random.choice(self.action_size)
    act_values = self.model.predict(state)
    return np.argmax(act_values[0]) # returns action

  def update_replay_memory(self, state, action, reward, next_state):
    pass


def mlp(input_dim, n_action, n_hidden_layers=1, hidden_dim=32):
  return None # todo