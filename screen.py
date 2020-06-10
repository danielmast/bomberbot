import re
from subprocess import Popen, PIPE
from time import sleep

import cv2
import mss
import numpy as np

from constants import tab_name


def get_geo_string(window_id):
    out, err = Popen(["xdotool", "getwindowgeometry", window_id], stdout=PIPE).communicate()
    return out.decode('utf-8')


def get_window_id():
    proc = Popen(["xdotool", "search", tab_name], stdout=PIPE)
    out, err = proc.communicate()
    return out.decode('utf-8')[:-1]


def parse_geometry_string(geo_string):
    geo_string = geo_string.replace("\n", "")
    regex = r'^Window \d{1,10}  Position: (\d{1,4}),(\d{1,4}) \(screen: \d{1,4}\)  Geometry: (\d{1,4})x(\d{1,4})'
    # Example: 'Window 48234499  Position: 1024,567 (screen: 0)  Geometry: 512x448'
    groups = re.match(regex, geo_string).groups()
    return tuple(int(el) for el in groups)


def get_game_geometry():
    geo_string = get_geo_string(get_window_id())
    left, top, width, height = parse_geometry_string(geo_string)
    return left, top, width, height


def window_to_foreground(window_id):
    Popen(["xdotool", "windowactivate", window_id], stdout=PIPE).communicate()
    sleep(0.05)


def capture_gamewindow():
    left, top, width, height = get_game_geometry()
    monitor = {"top": top, "left": left, "width": width, "height": height}
    # window_to_foreground(get_window_id())
    img = mss.mss().grab(monitor)
    rgba = np.array(img)
    rgb = cv2.cvtColor(rgba, cv2.COLOR_BGRA2RGB)
    return rgb


def current_screen(img):
    if np.array_equal(img[300, 460], [130, 180, 55]):
        return 0
    elif np.array_equal(img[430, 400], [113, 113, 113]):
        return 1
    elif np.array_equal(img[460, 500], [127, 127, 127]):
        return 2
    elif np.array_equal(img[485, 500], [127, 127, 127]):
        return 3
    elif np.array_equal(img[90, 240], [122, 122, 122]):
        if np.array_equal(img[110, 530], [75, 99, 22]):
            return 5
        else:
            return 4
    elif np.array_equal(img[470, 710], [127, 127, 127]):
        return 6

    return None