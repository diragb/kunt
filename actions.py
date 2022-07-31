# Packages:
import pyautogui
import random
from time import sleep


# Functions:
def switchWindows(tabCount = 1):
  pyautogui.keyDown('alt')
  for _ in range(tabCount):
    pyautogui.keyDown('tab')
  pyautogui.keyUp('alt')

def shuffleWindows(windowCount = 1):
  print(windowCount)
  for i, _ in enumerate(range(windowCount)):
    pyautogui.keyDown('alt')
    for __ in range(i):
      pyautogui.keyDown('tab')
      sleep(0.01)
    pyautogui.keyUp('alt')
    sleep(0.01)

def switchTab(tabCount = 1):
  pyautogui.keyDown('ctrlleft')
  for _ in range(tabCount):
    pyautogui.keyDown('tab')
    sleep(0.01)
  pyautogui.keyUp('ctrlleft')

def moveMouse(x = None, y = None):
  width, height = pyautogui.size()
  pyautogui.moveTo(x or random.randrange(width), y or random.randrange(height))

def scroll():
  scrollBy = random.choice([-1, 1]) * random.randrange(500, 1000)
  pyautogui.scroll(scrollBy)
  return scrollBy

def spamCtrlLeftKey(count = 100):
  pyautogui.PAUSE = 0
  for _ in range(count):
    pyautogui.keyDown('ctrlleft', None, False)
    pyautogui.keyUp('ctrlleft', None, False)
  pyautogui.PAUSE = 0.01

def moveMouseToSafeSpace():
  pyautogui.moveTo(340, 1060)

def spamMouseClick(count = 100):
  moveMouseToSafeSpace()
  pyautogui.PAUSE = 0
  for _ in range(count):
    pyautogui.click()
  pyautogui.PAUSE = 0.01
