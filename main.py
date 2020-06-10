import time

import clicker
import screen
import stateprocessor
from agent import Agent
from api import APIThread
from constants import state_dim, action_size
from env import Env
from stateprocessor import Stateprocessor

if __name__ == '__main__':
  agent = Agent(state_dim=state_dim, action_size=action_size)
  env = Env()
  stateprocessor.stateprocessor = Stateprocessor(agent, env, is_train=True)

  api_thread = APIThread()
  api_thread.start()

  while True:
    gamewindow = screen.capture_gamewindow()
    current_screen = screen.current_screen(gamewindow)
    clicker.click(current_screen)
    time.sleep(0.5)
