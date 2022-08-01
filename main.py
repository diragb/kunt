# Packages:
import random
import time
import json
from playsound import playsound
playsound('./assets/start.mp3')
import sys
import pyautogui
from webcam import handleWebcam
from screen import simulateWork, restore

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
prelaunchArguments = json.load(open('prelaunch.json'))


# Functions:
def tstring2sec(tstring: str):
  return sum(x * int(t) for x, t in zip([ 3600, 60, 1 ], tstring.split(':'))) 

def alertStop(noNotification, noPrint):
  if not noNotification:
    try:
      playsound('./assets/start.mp3')
      if not noPrint: print('🔴 Stop')
    except:
      print('🔴 Stop')

def alertResume(noNotification, noPrint):
  if not noNotification:
    try:
      playsound('./assets/stop.mp3')
      if not noPrint: print('🟢 Resume')
    except:
      print('🟢 Resume')

# Execution:
if __name__ == '__main__':
  arguments = sys.argv[1:]
  noNotification = True if '--no-notification' in arguments else False
  noPrint = True if '--no-print' in arguments else False
  alreadySlept = False
  start, run, repeat = map(lambda tstring: tstring2sec(tstring), prelaunchArguments['time'].values())
  mousePosition: pyautogui.Point
  scrollBy: int
  activeWindow: pyautogui.Window

  if not noPrint: print(f'🤖  { color.BOLD }{ color.BLUE }KUNT{ color.END } is running..')
  if not noPrint: print(f'\
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
    isAFK = prelaunchArguments['afk'] >= random.uniform(0, 1)
    isAFK = False
    if start != 0 and not alreadySlept:
      time.sleep(start - (run / 2))
      alreadySlept = True
    alertStop(noNotification, noPrint)
    simulationStartTime = time.time()
    if not isAFK: [ mousePosition, scrollBy, activeWindow ] = simulateWork()
    simulationDuration = time.time() - simulationStartTime
    time.sleep(run - simulationDuration)
    alertResume(noNotification, noPrint)
    handleWebcam(isAFK)
    if not isAFK: restore(mousePosition, scrollBy, activeWindow)
    time.sleep(repeat - run - 3.5)
