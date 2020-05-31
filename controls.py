from subprocess import Popen, PIPE
from constants import *
import time

def key_press(key, delay):
    Popen(["xdotool", "search", "--name", tab_name, "windowfocus", "keydown", "--delay", str(delay), key, "keyup", key], stdout=PIPE).communicate()


def do_action(action):
    key = keys[action]
    if action == BOMB:
        delay = 10
    else:
        delay = 250
    key_press(key, delay)
    time.sleep(0.2)