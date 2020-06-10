import numpy as np
from matplotlib.colors import rgb2hex

def current_screen(img):
    if np.array_equal(img[300, 460], [130, 180, 55]):
        print(rgb2hex(img[300, 460]/255.0))
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