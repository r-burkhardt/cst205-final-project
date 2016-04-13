'''

  Program:  Name of Program
  File name:  main.py
  Files imported:  None
  Author:  name here
  Team:  MB Overloaders
  Date created:  2016/04/02
  Date last modified:  2016/04/02
  Version:  0.0.1

'''

#Set path to classes and source files
from inspect import getsourcefile
from os.path import abspath

thisFile = "main.py"
thisFilePath = getsourcefile(lambda:0)
path = thisFilePath[:(len(thisFilePath)-len(thisFile)-1)]
setLibPath(path) 

#import location
from bin.location import *
#import help
#from help import *

santaMonicaPier = Location("Santa Monica", "You are standing on the beach in Santa Monica.", "", "Rodeo Drive, Beverly Hills", "", "")

print santaMonicaPier.displayLocation() #.locationDesc()


#