import env
import agent
from agent import Agent
from api import APIThread
from env import Env

if __name__ == '__main__':
  env.env = Env()
  agent.agent = Agent()
  api_thread = APIThread()
  api_thread.start()