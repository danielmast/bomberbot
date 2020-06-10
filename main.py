import screencapturer
import stateprocessor
from agent import Agent
from api import APIThread
from constants import state_dim, action_size
from env import Env
from stateprocessor import Stateprocessor
import imageprocessor
import time

if __name__ == '__main__':
  agent = Agent(state_dim=state_dim, action_size=action_size)
  env = Env()
  stateprocessor.stateprocessor = Stateprocessor(agent, env, is_train=True)

  # while True:
  #   gamewindow = screencapturer.capture_gamewindow()
  #   screen = imageprocessor.current_screen(gamewindow)
  #   print(screen)
  #   time.sleep(0.5)

  api_thread = APIThread()
  api_thread.start()