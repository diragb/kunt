# Packages:
import random
from time import sleep
import win32gui, win32con
import json
from typing import List
from playsound import playsound
playsound('./assets/start.mp3')
import sys
import os
from PIL import Image
import actions


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
last_state = {
  'target': {}
}


# Functions:
def tstring2sec(tstring: str):
  return sum(x * int(t) for x, t in zip([ 3600, 60, 1 ], tstring.split(':'))) 

def winEnumHandler(hwnd, ctx):
  if win32gui.IsWindowVisible(hwnd):
    current_windows.append({ 'hex': hex(hwnd), 'name': win32gui.GetWindowText(hwnd) })

def goToRandomWindow(names: List, is_afk: bool):
  try:
    target = random.choice(names)
    target_window = win32gui.FindWindowEx(None, None, None, target['window_name'])
    win32gui.SetForegroundWindow(target_window)
    win32gui.ShowWindow(target_window, win32con.SW_MAXIMIZE)
    if not is_afk: exec('\n'.join(target['target']['exec']))
    last_state['target'] = target
  except:
    print('⚠️  Failed to bring windows to the foreground as they are minimized or have lost state.')
    print('🔃  Shuffling 5 windows...')
    actions.shuffleWindows(5)
    target = random.choice(names)
    target_window = win32gui.FindWindowEx(None, None, None, target['window_name'])
    win32gui.SetForegroundWindow(target_window)
    win32gui.ShowWindow(target_window, win32con.SW_MAXIMIZE)
    if not is_afk: exec('\n'.join(target['target']['exec']))
    last_state['target'] = target
    print('✅  Handled window error.') 

def do_random_shit(is_afk: bool):
  try:
    if not is_afk or len(last_state['target']) == 0:
      win32gui.EnumWindows(winEnumHandler, None)
      for window in current_windows:
        for target in targets:
          if target['name'] in window['name']: available_targets.append({ 'window_name': window['name'], 'target': target })
      goToRandomWindow(available_targets, is_afk)
    else:
      lt = last_state['target']
      goToRandomWindow([ last_state['target'] ], is_afk)
  except:
    if not is_afk:
      actions.switchWindows(random.randrange(3) + 1)
      actions.switchTab(random.randrange(6) + 1)
      actions.moveMouse()
      actions.scroll()
      actions.spamCtrlLeftKey(random.randrange(100) + 100)

def get_random_source_image():
  images = os.listdir(os.getcwd() + '\\' + prelaunch['images']['source_directory'])
  image = random.choice(images)
  return os.getcwd() + '\\' + prelaunch['images']['source_directory'] + '\\' + image

def replace_one_image(image_path: str):
  target = Image.open(image_path)
  source = Image.open(get_random_source_image())
  if prelaunch['images']['rtl']: source = source.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
  new_target = source.resize((target.width, target.height))
  target.close()
  new_target.save(image_path)
  new_target.close()
  if prelaunch['images']['replace_thumbails']:
    thumbnail_path = image_path.replace(prelaunch['images']['match'], prelaunch['images']['thumbnail_match'])
    thumbnail = Image.open(thumbnail_path)
    new_thumbnail = source.resize((thumbnail.width, thumbnail.height))
    thumbnail.close()
    new_thumbnail.save(thumbnail_path)
    new_thumbnail.close()
  source.close()

def replace_images():
  images = os.listdir(prelaunch['images']['target_directory'])
  for image in images:
    if (prelaunch['images']['match'] in image):
      replace_one_image(prelaunch['images']['target_directory'] + '\\' + image)

def get_random_afk_image():
  images = os.listdir(os.getcwd() + '\\' + prelaunch['images']['afk'])
  image = random.choice(images)
  return os.getcwd() + '\\' + prelaunch['images']['afk'] + '\\' + image

def replace_one_image_with_afk(image_path: str):
  target = Image.open(image_path)
  source = Image.open(get_random_afk_image())
  if prelaunch['images']['rtl']: source = source.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
  new_target = source.resize((target.width, target.height))
  target.close()
  new_target.save(image_path)
  new_target.close()
  if prelaunch['images']['replace_thumbails']:
    thumbnail_path = image_path.replace(prelaunch['images']['match'], prelaunch['images']['thumbnail_match'])
    thumbnail = Image.open(thumbnail_path)
    new_thumbnail = source.resize((thumbnail.width, thumbnail.height))
    thumbnail.close()
    new_thumbnail.save(thumbnail_path)
    new_thumbnail.close()
  source.close()

def replace_images_with_afk():
  images = os.listdir(prelaunch['images']['target_directory'])
  for image in images:
    if (prelaunch['images']['match'] in image):
      replace_one_image_with_afk(prelaunch['images']['target_directory'] + '\\' + image)

# Execution:
if __name__ == '__main__':
  arguments = sys.argv[1:]
  no_notification = True if '--no-notification' in arguments else False
  no_print = True if '--no-print' in arguments else False
  already_slept = False
  start, run, repeat = map(lambda tstring: tstring2sec(tstring), prelaunch['time'].values())

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
    current_windows = []
    available_targets = []
    is_afk = prelaunch['afk'] >= random.uniform(0, 1)
    if start != 0 and not already_slept:
      sleep(start - run / 2)
      already_slept = True
    if not no_notification:
      try:
        playsound('./assets/start.mp3')
        if not no_print: print('🔴 Stop')
      except:
        print('🔴 Stop')
    do_random_shit(is_afk)
    sleep(run)
    if not no_notification:
      try:
        playsound('./assets/stop.mp3')
        if not no_print: print('🟢 Resume')
      except:
        print('🟢 Resume')
    if prelaunch['images']['replace']:
      try:
        if not is_afk:
          replace_images()
        else:
          replace_images_with_afk()
      except:
        print('🔴 Could not replace image.')
    sleep(repeat - run / 2)
