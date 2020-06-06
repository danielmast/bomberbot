import stateprocessor
from agent import Agent
from api import APIThread
from constants import action_size
from env import Env
from stateprocessor import Stateprocessor

if __name__ == '__main__':
  state_size = 0 # todo
  agent = Agent(state_size=state_size, action_size=action_size)
  env = Env()
  stateprocessor.stateprocessor = Stateprocessor(agent, env, is_train=True)

  api_thread = APIThread()
  api_thread.start()