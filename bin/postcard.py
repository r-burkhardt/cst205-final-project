'''

  Program:  Beat Los Angeles
  File name:  postcard.py
  Files imported:  None
  Author/s:  Roderick Burkhardt, Agustin Preciado, Mina Mansour
  Team:  MB Overloaders
  Team members:  Roderick Burkhardt, Faiga Revah, Mina Mansour, Agustin Preciado
  Date created:  2016/04/19
  Date last modified:  2016/04/19
  Version:  0.0.1

'''

import sys
from string import *
from inspect import getsourcefile
from string import *
from media import *

global PATH
global IMGDIR
global CITYIMAGES
global PICPLACEMENT

thisFile = "bin/postcard.py"
thisFilePath = getsourcefile(lambda:0)
PATH = thisFilePath[:(len(thisFilePath)-len(thisFile))]

if PATH[0] == "/":
  IMGDIR = "sources/"
else:
  IMGDIR = "sources\\"
CITYIMAGES = {}
CITYIMAGES['Beverly Hills'] = 'beverly-hills.jpg'
CITYIMAGES['Grauman\'s Chinese Theatre'] = 'chinese-theatre.jpg'
CITYIMAGES['Getty Center'] = 'getty-museum.jpg'
CITYIMAGES['Griffith Observatory'] = 'griffith-observatory.jpg'
CITYIMAGES['LaBrea Tar Pits'] = 'la-brea-tar-pits.jpg'
CITYIMAGES['LACMA'] = 'lacma.jpg'
CITYIMAGES['Los Angeles City Hall'] = 'los-angeles-city-hall.jpg'
CITYIMAGES['Los Angeles Zoo'] = 'los-angeles-zoo.jpg'
CITYIMAGES['MONA'] = 'mona.jpg'
CITYIMAGES['Norton Simon Museum'] = 'norton-simon-museum.jpg'
CITYIMAGES['Olvera Street'] = 'olvera-street.jpg'
CITYIMAGES['Santa Monica Pier'] = 'santa-monica-pier.jpg'
CITYIMAGES['UCLA'] = 'ucla.jpg'
CITYIMAGES['Union Station'] = 'union-station.jpg'
CITYIMAGES['Universal Studios'] = 'universal-studios-hollywood.jpg'
CITYIMAGES['West Hollywood'] = 'west-hollywood.jpg'

overlay = makePicture(PATH + IMGDIR + 'los-angeles.jpg')

PICPLACEMENT = [[0,0],[0,299],[449,0],[0,599],[449,299],[899,0],[0,899],[449,599],[899,299],[1349,0],[449,899],[899,599],[1349,299],[899,899],[1349,599],[1349,899]]


def makePostcard(picList):
  pictures = []
  postcard = makeEmptyPicture(1800,1200, makeColor(230,179,31))
  for place in picList:
    pictures.append(makePicture(PATH + IMGDIR + CITYIMAGES[place]))
  sizedPictures = []
  for pic in pictures:
    sizedPictures.append(resizePicture(pic, 450, 300))
  for p in range(len(sizedPictures)):
    image = sizedPictures[p]
    position = PICPLACEMENT[p]
    for x in range(0, getWidth(image)):
      for y in range(0, getHeight(image)):
        px1 = getPixel(image, x, y)
        px2 = getPixel(postcard, x+position[0], y+position[1])
        setColor(px2, getColor(px1))
  for x in range(0, getWidth(postcard)):
    for y in range(0, getHeight(postcard)):
      px1 = getPixel(overlay, x, y)
      px2 = getPixel(postcard, x, y)
      color = getColor(px1)
      if distance(color, green) >50:
        setColor(px2, color)
  
  informString = "Your postcard is complete, please use the next\n window to select where you want the postcard saved."
  showInformation(informString)
  
  savePath = pickAFolder()
  postcardSaveIn = savePath + 'los-angles-postcard.jpg'
  writePictureTo(postcard, postcardSaveIn)
  
  showInformation("Thank you for playing, your postcard is saved.")
  
  
  


def resizePicture(original, width, height):
  sizeDifference = getHeight(original)/height
  imageCopy = copyPic(original)
  if sizeDifference >= 4 and sizeDifference < 6:
    newImage = shrinkImageHorizontal(shrinkImageHorizontal(imageCopy))
  elif sizeDifference >= 2 and sizeDifference < 4:
    newImage = shrinkImageHorizontal(imageCopy)
  sizedImage = makeEmptyPicture(width, height)
  xDifference = getWidth(newImage)-getWidth(sizedImage)
  yDifference = getHeight(newImage)-getHeight(sizedImage)
  for x in range(0, getWidth(sizedImage)):
    for y in range(0, getHeight(sizedImage)):
      px1 = getPixel(newImage, x+(xDifference/2), y+(yDifference/2))
      px2 = getPixel(sizedImage, x, y)
      setColor(px2, getColor(px1))
  return sizedImage


def shrinkImageHorizontal(imageTo):
  imageCopy = copyPic(imageTo)
  newImage = makeEmptyPicture(getWidth(imageCopy)/2, getHeight(imageCopy)/2)
  for x in range(0, getWidth(imageCopy)-1, 2):
    for y in range(0, getHeight(imageCopy), 2):
      px1 = getPixel(imageCopy, x, y)
      px2 = getPixel(newImage, x/2, y/2)
      setColor(px2, getColor(px1))
  return newImage


def copyPic(original):
  copiedImage = makeEmptyPicture(getWidth(original), getHeight(original))
  for x in range(0, getWidth(original)):
    for y in range(0, getHeight(original)):
      px1 = getPixel(original, x, y)
      px2 = getPixel(copiedImage, x, y)
      setColor(px2, getColor(px1))
  return copiedImage







#