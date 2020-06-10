import pyautogui

def click(screen):
    if screen == 0:
        pyautogui.click(530, 480)
    elif screen == 1:
        pyautogui.click(530, 400)
    elif screen == 2:
        pyautogui.click(530, 400)
    elif screen == 3:
        pyautogui.click(530, 400)
    elif screen == 4:
        pass
    elif screen == 5:
        pyautogui.click(550, 410)
    elif screen == 6:
        pyautogui.click(530, 420)
    else:
        pass