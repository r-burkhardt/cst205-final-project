'''

  Program:  Name of Program
  File name:  location.py
  Files imported:  None
  Author:  name here
  Team:  MB Overloaders
  Date created:  2016/04/02
  Date last modified:  2016/04/02
  Version:  0.0.1

'''
import sys

# Begin Code

class Location(object):
  """A class that describes a location"""
  
  def __init__(self, name, locDesc, goNorth, goEast, goSouth, goWest):
    self.name = name
    self.locDesc = locDesc
    self.goNorth = goNorth
    self.goEast = goEast
    self.goSouth = goSouth
    self.goWest = goWest

  def displayLocation(self):
    returnString = "You are at " + self.name + "\n"
    returnString += self.locDesc + "\n"
    if self.goNorth != "":
      returnString += "To the North is " + self.goNorth + ".\n"
    if self.goEast != "":
      returnString += "To the North is " + self.goEast + ".\n"
    if self.goSouth != "":
      returnString += "To the North is " + self.goSouth + ".\n"
    if self.goWest != "":
      returnString += "To the North is " + self.goWest + ".\n"
    return returnString
    
    
santaMonicaPier = Location("Santa Monica", "You are standing on the beach in Santa Monica.", "", "Rodeo Drive, Beverly Hills", "", "")

print santaMonicaPier.displayLocation()