import numpy as np
from tensorflow.keras.layers import Dense, Input, Flatten
from tensorflow.keras.models import Model


class Agent():
  def __init__(self, state_dim, action_size):
    self.action_size = action_size
    self.epsilon = 0.1
    self.model = mlp(state_dim, action_size)

  def act(self, state):
    if np.random.rand() <= self.epsilon:
      return np.random.choice(self.action_size)
    act_values = self.model.predict(np.expand_dims(state, axis=0))
    return np.argmax(act_values[0]) # returns action

  def update_replay_memory(self, state, action, reward, next_state):
    pass


def mlp(input_dim, n_action, n_hidden_layers=1, hidden_dim=32):
  """ A multi-layer perceptron """

  # input layer
  i = Input(shape=input_dim)
  x = i

  x = Flatten()(x)

  # hidden layers
  for _ in range(n_hidden_layers):
    x = Dense(hidden_dim, activation='relu')(x)

  # final layer
  x = Dense(n_action)(x)

  # make the model
  model = Model(i, x)

  model.compile(loss='mse', optimizer='adam')
  print((model.summary()))
  return model
