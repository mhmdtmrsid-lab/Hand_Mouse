import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

screen_w, screen_h = pyautogui.size()

def move_mouse(x, y):
    pyautogui.moveTo(x, y)

def left_click():
    pyautogui.click()

def right_click():
    pyautogui.rightClick()

def mouse_down():
    pyautogui.mouseDown()

def mouse_up():
    pyautogui.mouseUp()

def scroll(amount):
    pyautogui.scroll(amount)
