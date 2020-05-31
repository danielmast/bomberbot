import env
from agent import Agent
from api import APIThread
from env import Env


def play_one_episode(agent, env):
  state = None
  done = False

  while not done:
    action = agent.act(state)
    res = env.step(action)

if __name__ == '__main__':
  env.env = Env()
  agent = Agent()
  api_thread = APIThread()
  api_thread.start()
  play_one_episode(agent, env.env)