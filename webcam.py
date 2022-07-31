# Packages:
import json
import random
import os
from PIL import Image, ImageEnhance
from datetime import datetime
import cv2


# Constants:
prelaunchArguments = json.load(open('prelaunch.json'))
cwd = os.getcwd()


# Functions:
def saveRandomVideoScreenshot():
  weekday = datetime.today().strftime('%A').lower()
  weekdayVideos = os.listdir(cwd + '\\' + f'/assets/videos/{weekday}/')
  weekdayVideo = random.choice(weekdayVideos)
  video = cv2.VideoCapture(f'./assets/videos/{weekday}/{weekdayVideo}')
  frameCount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  randomFrame = random.randrange(0, frameCount)
  video.set(cv2.CAP_PROP_POS_FRAMES, randomFrame - 1)
  success, frame = video.read()
  screenshotName = f'{randomFrame}.png'
  if success:
    cv2.imwrite(screenshotName, frame)
  video.release()
  cv2.destroyAllWindows()
  return screenshotName

def modifyAndGetScreenshot(name):
  darkFactor = random.uniform(0.75, 1)
  contrastFactor = random.uniform(1, 1.25)
  target = Image.open(name)
  darkenedTarget = target.point(lambda point: point * darkFactor)
  target.close()
  os.remove(name)
  contrastedDarkenedTarget = ImageEnhance.Contrast(darkenedTarget).enhance(contrastFactor)
  darkenedTarget.close()
  if prelaunchArguments['images']['rtl']: contrastedDarkenedTarget = contrastedDarkenedTarget.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
  contrastedDarkenedTarget.save(name)
  contrastedDarkenedTarget.close()
  return name

def imagesToReplace():
  targetImages = []
  targetDirectory = prelaunchArguments['images']['targetDirectory']
  imagesPresent = os.listdir(targetDirectory)
  for imageName in imagesPresent:
    if (prelaunchArguments['images']['targetNameMustMatch'] in imageName):
      targetImages.append(targetDirectory + '\\' + imageName)
  return targetImages

def getRandomAFKImage():
  afkDirectory = cwd + '\\' + prelaunchArguments['images']['afk']
  afkImages = os.listdir(afkDirectory)
  afkImage = random.choice(afkImages)
  return afkDirectory + '\\' + afkImage

def replaceThumbnail(targetPath, source: Image.Image):
  thumbnailPath = targetPath.replace(prelaunchArguments['images']['targetNameMustMatch'], prelaunchArguments['images']['targetThumbnailNameMustMatch'])
  thumbnail = Image.open(thumbnailPath)
  newThumbnail = source.resize((thumbnail.width, thumbnail.height))
  thumbnail.close()
  newThumbnail.save(thumbnailPath)
  newThumbnail.close()

def replace(**kwargs):
  for targetPath in kwargs['these']:
    target = Image.open(targetPath)
    source = Image.open(kwargs['withThis']).resize((target.width, target.height))
    source.save(targetPath)
    replaceThumbnail(targetPath, source)
    source.close()
    target.close()
  os.remove(kwargs['withThis'])

def handleActivityImage():
  replace(
    these=imagesToReplace(),
    withThis=modifyAndGetScreenshot(saveRandomVideoScreenshot())
  )

def handleAFKImage():
  replace(
    these=imagesToReplace(),
    withThis=getRandomAFKImage()
  )

def handleWebcam(isAFK: bool):
  try:
    if not isAFK:
      try:
        handleActivityImage()
      except:
        try:
          print('Failed to get screenshot, using fallback images.')
        except:
          print('Failed to get screenshot, using AFK images.')
          handleAFKImage()
    else:
      handleAFKImage()
  except:
      print('🔴 Could not replace image.')
