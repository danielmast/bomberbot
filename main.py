import os
import time

import numpy as np

import screen
import stateprocessor
from agent import Agent
from api import APIThread
from constants import state_dim, action_size, models_folder, returns_folder
from env import Env
from stateprocessor import Stateprocessor


def maybe_make_dir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)


if __name__ == '__main__':
  t = np.load(f'{returns_folder}/train.npy')
  maybe_make_dir(models_folder)
  maybe_make_dir(returns_folder)
  num_episodes = 3

  agent = Agent(state_dim=state_dim, action_size=action_size)
  env = Env()
  stateprocessor.stateprocessor = Stateprocessor(agent, env, is_train=True)
  sp = stateprocessor.stateprocessor

  api_thread = APIThread()
  api_thread.start()

  while sp.episode < num_episodes:
    gamewindow = screen.capture_gamewindow()
    current_screen = screen.current_screen(gamewindow)
    sp.process_screen(current_screen)
    time.sleep(0.5)

  agent.save(f'{models_folder}/dqn.h5')
  np.save(f'{returns_folder}/train.npy', sp.returns)