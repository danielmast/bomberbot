import stateprocessor
from agent import Agent
from api import APIThread
from env import Env
from stateprocessor import Stateprocessor

if __name__ == '__main__':
  agent = Agent()
  env = Env()
  stateprocessor.stateprocessor = Stateprocessor(agent, env, is_train=True)

  api_thread = APIThread()
  api_thread.start()