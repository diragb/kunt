# Packages:
import pyautogui
import random


# Functions:
def switchTab(tab_count = 1):
  pyautogui.keyDown('ctrlleft')
  for _ in range(tab_count):
    pyautogui.keyDown('tab')
  pyautogui.keyUp('ctrlleft')

def moveMouse(x = None, y = None):
  width, height = pyautogui.size()
  pyautogui.moveTo(x or random.randrange(width), y or random.randrange(height))

def scroll():
  pyautogui.scroll(random.choice([-1, 1]) * random.randrange(500, 1000))
