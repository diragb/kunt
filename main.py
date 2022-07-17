# Packages:
import random
from time import sleep
import win32gui, win32con
import json
from typing import List
from playsound import playsound
import sys

# Constants:
class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'
targets = json.load(open('targets.json'))
prelaunch = json.load(open('prelaunch.json'))


# Variables:
current_windows = []
available_targets = []


# Functions:
def tstring2sec(tstring: str):
  return sum(x * int(t) for x, t in zip([ 3600, 60, 1 ], tstring.split(':'))) 

def winEnumHandler(hwnd, ctx):
  if win32gui.IsWindowVisible(hwnd):
    current_windows.append({ 'hex': hex(hwnd), 'name': win32gui.GetWindowText(hwnd) })

def goToRandomWindow(names: List):
  try:
    target = random.choice(names)
    target_window = win32gui.FindWindowEx(None, None, None, target['window_name'])
    win32gui.SetForegroundWindow(target_window)
    win32gui.ShowWindow(target_window, win32con.SW_MAXIMIZE)
    exec('\n'.join(target['target']['exec']))
  except:
    target = random.choice(names)
    target_window = win32gui.FindWindowEx(None, None, None, target['window_name'])
    win32gui.SetForegroundWindow(target_window)
    win32gui.ShowWindow(target_window, win32con.SW_MAXIMIZE)
    exec('\n'.join(target['target']['exec']))

def kunt():
  win32gui.EnumWindows(winEnumHandler, None)
  for window in current_windows:
    for target in targets:
      if target['name'] in window['name']: available_targets.append({ 'window_name': window['name'], 'target': target })
  goToRandomWindow(available_targets)


# Execution:
if __name__ == '__main__':
  arguments = sys.argv[1:]
  no_notification = True if '--no-notification' in arguments else False
  no_print = True if '--no-print' in arguments else False
  already_slept = False
  start, run, repeat = map(lambda tstring: tstring2sec(tstring), prelaunch.values())

  if not no_print: print(f'🤖  { color.BOLD }{ color.BLUE }KUNT{ color.END } is running..')
  if not no_print: print(f'\
    🤖  { color.BOLD }{ color.BLUE }KUNT{ color.END } is running..\
    \n\n🤔  { color.BOLD }{ color.BLUE }KUNT{ color.END } stands for:\
      \n\t🏃  { color.BOLD }{ color.RED }Kinetic{ color.END }\
      \n\t👤  { color.BOLD }{ color.CYAN }User{ color.END }\
      \n\t🧮  { color.BOLD }{ color.GREEN }NP-Complete{ color.END }\
      \n\t🔨  { color.BOLD }{ color.YELLOW }Toolkit{ color.END }\
    \n\n📜  { color.BOLD }{ color.BLUE }KUNT{ color.END } was made to help workers being forced under constant surveillance by their workplaces to automate their work-habits and show that { color.UNDERLINE }progress is being made{ color.END }.\
    \n\n🤷  Until workplaces understand that their workers don\'t really like being under constant f*cking surveillance like a 1984 movie, people will keep making and using tools like { color.BOLD }{ color.BLUE }KUNT{ color.END }.\
  ')

  while True:
    if start != 0 and not already_slept:
      sleep(start - run / 2)
      already_slept = True
    else:
      sleep(repeat - run / 2)
    if not no_notification: playsound('assets/start.mp3')
    kunt()
    sleep(run)
    if not no_notification: playsound('assets/stop.mp3')
    sleep(repeat - run / 2)
