# Imports:
import random
import actions
import pyautogui


# Functions:
def remember():
  return [
    pyautogui.position(),
    pyautogui.getActiveWindow()
  ]

def restore(mousePosition: pyautogui.Point, scrollBy: int, activeWindow: pyautogui.Window):
  pyautogui.moveTo(mousePosition.x, mousePosition.y)
  activeWindow.maximize()
  activeWindow.activate()
  pyautogui.scroll(-scrollBy)

def loadWindows():
  windows = [
    *pyautogui.getWindowsWithTitle('Chrom'),
    *pyautogui.getWindowsWithTitle('Visual Studio Code'),
    *pyautogui.getWindowsWithTitle('Slack')
  ]
  random.shuffle(windows)
  for window in windows:
    try:
      window.maximize()
      window.activate()
      actions.switchWindows(1)
    except:
      print('⚠️  Failed to load windows.')

def simulateWork():
  [ mousePosition, activeWindow ] = remember()
  actions.spamMouseClick(random.randrange(50, 150))
  loadWindows()
  actions.switchTab(random.randrange(2, 6) + 1)
  actions.moveMouse()
  scrollBy = actions.scroll()
  actions.spamCtrlLeftKey(random.randrange(50, 150))
  return [ mousePosition, scrollBy, activeWindow ]
