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
from string import *

# Begin Code

class Location(object):
  """A class that describes a location"""
  
  def __init__(self, name, locDesc, cost, time, travelTable):
    self.name = name
    self.locDesc = locDesc
    self.cost = cost
    self.time = time
    self.travelTable = travelTable

  def displayLocation(self):
    returnString = "You have arrived at " + self.name + "\n"
    returnString += self.locDesc + "\n"
    return returnString
    
  def displayLocCostTime(self):
    return '%s  Cost: %.2f  Time: %.2f' % (self.name, self.cost, self.time)
    
  def getTravelTime(self, fromLocation):
    return self.travelTable[fromLocation]
    
    
santaMonicaPier = Location("Santa Monica", "You are standing on the beach in Santa Monica.",100.00, 4, {'Beverly Hills':1,'Getty Museum':0.75,'Grauman\'s Chinese Theater':1,'Griffith Observatory':1,'LaBrea Tar Pits':0.25,'LACMA':0,'Los Angeles City Hall':1.25,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':1.25,'Santa Monica Pier':1.25,'UCLA':0.5,'Union Station':1.25,'Universal Studios':1.75,'West Hollywood':0.75,})

#print santaMonicaPier.displayLocation()
#print santaMonicaPier.displayLocCostTime()
#print santaMonicaPier.getTravelTime('Beverly Hills')
#print str(santaMonicaPier.displayLocCostTime())
