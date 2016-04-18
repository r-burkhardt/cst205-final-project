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

### Imports
from bin.location import *
from random import *


### Set Locations
global LOCATIONS
LOCATIONS = {}
LOCATIONS['Beverly Hills'] = Location("Beverly Hills", \
  "Have you got enough cash? Head down Rodeo Drive, your visit is here is going to take 8 hours to get through every store. The time here is going to cost you $1500", \
  1500, 8, \
  {'Beverly Hills':0,'Getty Center':0.75,'Grauman\'s Chinese Theater':0.50,'Griffith Observatory':1.25,'LaBrea Tar Pits':0.50,'LACMA':0.50,'Los Angeles City Hall':1.25,'Los Angeles Zoo':1.50,'MONA':2.00,'Norton Simon Museum':2.25,'Olvera Street':1.25,'Santa Monica Pier':0.75,'UCLA':0.50,'Union Station':1.50,'Universal Studios':1.00,'West Hollywood':0.50})

LOCATIONS['Getty Center'] = Location("Getty Center", \
  "Art aficionado? You\'ve come to the right place. Getty\'s entrance fee is $100, and to appreciate every painting, you\'ll need to spend 4 hours here.", \
  100, 4, \
  {'Beverly Hills':0.75,'Getty Center':0,'Grauman\'s Chinese Theater':1.25,'Griffith Observatory':1.75,'LaBrea Tar Pits':1,'LACMA':0.75,'Los Angeles City Hall':1.75,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.25,'Olvera Street':1.75,'Santa Monica Pier':1,'UCLA':0.5,'Union Station':1.75,'Universal Studios':1.5,'West Hollywood':0.75})

LOCATIONS['Grauman\'s Chinese Theater'] = Location("Grauman\'s Chinese Theater", \
  "", \
  150, 3,
  {'Beverly Hills':.5,'Getty Center':1.25,'Grauman\'s Chinese Theater':0,'Griffith Observatory':0.5,'LaBrea Tar Pits':1,'LACMA':1,'Los Angeles City Hall':0.75,'Los Angeles Zoo':0.5,'MONA':0.75,'Norton Simon Museum':1.25,'Olvera Street':0.75,'Santa Monica Pier':1.75,'UCLA':1.25,'Union Station':0.75,'Universal Studios':0.75,'West Hollywood':0.75})

LOCATIONS['Griffith Observatory'] = Location("Griffith Observatory", \
  "Galileo? Copernicus? Thought they were dead? They come alive here at the observatory? $50 to use the telescope, and spend 4 hours here to really stargaze properly.", \
  50, 4, \
  {'Beverly Hills':1.25,'Getty Center':1.75,'Grauman\'s Chinese Theater':0.5,'Griffith Observatory':0,'LaBrea Tar Pits':1,'LACMA':1,'Los Angeles City Hall':0.75,'Los Angeles Zoo':0.5,'MONA':0.75,'Norton Simon Museum':1.75,'Olvera Street':0.75,'Santa Monica Pier':2,'UCLA':2,'Union Station':0.75,'Universal Studios':0.75,'West Hollywood':1.25})

LOCATIONS['LaBrea Tar Pits'] = Location("LaBrea Tar Pits", \
  "Travel back in time to the Ice Age. Explore fossils here and visit the tar pits from those olden days. Incidentally, you\'ll need to pay $50 for this adventure, and spend 2 hours here.", \
  50, 2, \
  {'Beverly Hills':0.5,'Getty Center':1,'Grauman\'s Chinese Theater':1,'Griffith Observatory':1,'LaBrea Tar Pits':0,'LACMA':0.25,'Los Angeles City Hall':1,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':1,'Santa Monica Pier':1,'UCLA':0.5,'Union Station':1,'Universal Studios':1.5,'West Hollywood':0.75})
  
LOCATIONS['LACMA'] = Location("LACMA", \
  "We\'ve got special exhibits here, plus a great collection of art. Spend 4 hours here before moving on, and don\'t forget to pay the $100 entrance fee.", \
  100, 4, \
  {'Beverly Hills':1,'Getty Center':0.75,'Grauman\'s Chinese Theater':1,'Griffith Observatory':1,'LaBrea Tar Pits':0.25,'LACMA':0,'Los Angeles City Hall':1.25,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':1.25,'Santa Monica Pier':1.25,'UCLA':0.5,'Union Station':1.25,'Universal Studios':1.75,'West Hollywood':0.75,})

LOCATIONS['Los Angeles City Hall'] = Location("Los Angeles City Hall", \
  "Want to bother your city officials to lower your water bill. City Hall is the place! It\'s even free, but they\'re very stubborn, so allot at least an hour for your conversation.", \
  0, 1, \
  {'Beverly Hills':1.25,'Getty Center':1.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1,'LACMA':1.25,'Los Angeles City Hall':0,'Los Angeles Zoo':1.25,'MONA':1.25,'Norton Simon Museum':1.5,'Olvera Street':0.25,'Santa Monica Pier':1.75,'UCLA':1.5,'Union Station':0.25,'Universal Studios':1.5,'West Hollywood':1.75})

LOCATIONS['Los Angeles Zoo'] = Location("Los Angeles Zoo", \
  "Welcome to the LA Zoo, where you\'re in the company of lions, tigers, and zebras. Admission is $90, and you\'ll need to spend another $10 to hydrate yourself. 4 hours will give you enough time to pet every animal.", \
  100, 4, \
  {'Beverly Hills':1.5,'Getty Center':1.75,'Grauman\'s Chinese Theater':0.5,'Griffith Observatory':0.5,'LaBrea Tar Pits':1.75,'LACMA':1.75,'Los Angeles City Hall':1.25,'Los Angeles Zoo':0,'MONA':0.5,'Norton Simon Museum':1,'Olvera Street':1.25,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':1.25,'Universal Studios':0.75,'West Hollywood':1.75})

LOCATIONS['MONA'] = Location("MONA", \
  "", \
  100, 4, \
  {'Beverly Hills':2,'Getty Center':2,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':2,'LACMA':2,'Los Angeles City Hall':1.25,'Los Angeles Zoo':0.5,'MONA':0,'Norton Simon Museum':0.75,'Olvera Street':1.25,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':1.25,'Universal Studios':1.5,'West Hollywood':2})

LOCATIONS['Norton Simon Museum'] = Location("Norton Simon Museum", \
  "", \
  100, 4, \
  {'Beverly Hills':2.25,'Getty Center':2.25,'Grauman\'s Chinese Theater':1.25,'Griffith Observatory':1.75,'LaBrea Tar Pits':2.5,'LACMA':2.5,'Los Angeles City Hall':1.5,'Los Angeles Zoo':1,'MONA':0.75,'Norton Simon Museum':0,'Olvera Street':1,'Santa Monica Pier':2.5,'UCLA':2.25,'Union Station':1,'Universal Studios':1.75,'West Hollywood':2.5})

LOCATIONS['Olvera Street'] = Location("Olvera Street", \
  "Love a good bargain? Come visit Olvera Street and haggle the prices. You\'re on LA\'s first street. You\'ll be surprised how much money you\'ll need: $400, but with 3 hours of shopping, you\'ll come home with arms loaded.", \
  400, 3, \
  {'Beverly Hills':1.25,'Getty Center':1.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1,'LACMA':1.25,'Los Angeles City Hall':0.25,'Los Angeles Zoo':1.25,'MONA':1.25,'Norton Simon Museum':1,'Olvera Street':0,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':0.25,'Universal Studios':1.5,'West Hollywood':1.75})

LOCATIONS['Santa Monica Pier'] = Location("Santa Monica Pier", \
  "", \
  300, 4, \
  {'Beverly Hills':0.75,'Getty Center':1,'Grauman\'s Chinese Theater':1.75,'Griffith Observatory':2,'LaBrea Tar Pits':1,'LACMA':1.25,'Los Angeles City Hall':1.75,'Los Angeles Zoo':2,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':2,'Santa Monica Pier':0,'UCLA':0.75,'Union Station':2,'Universal Studios':2,'West Hollywood':1.25})

LOCATIONS['UCLA'] = Location("UCLA", \
  "Ready to get smart? You\'re at UCLA, one of the top public universities nationally. You need to study for an exam for 3 hours, so head straight to the library! The textbook will cost you $100.", \
  100, 3, \
  {'Beverly Hills':0.5,'Getty Center':0.5,'Grauman\'s Chinese Theater':1.25,'Griffith Observatory':2,'LaBrea Tar Pits':0.5,'LACMA':0.5,'Los Angeles City Hall':1.5,'Los Angeles Zoo':1.75,'MONA':1.75,'Norton Simon Museum':2.25,'Olvera Street':1.75,'Santa Monica Pier':0.75,'UCLA':0,'Union Station':1.75,'Universal Studios':1.75,'West Hollywood':0.75})

LOCATIONS['Union Station'] = Location("Union Station", \
  "", \
  50, 2, \
  {'Beverly Hills':1.5,'Getty Center':1.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1,'LACMA':1,'Los Angeles City Hall':0.25,'Los Angeles Zoo':1.25,'MONA':1.25,'Norton Simon Museum':1,'Olvera Street':0.25,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':0,'Universal Studios':1.75,'West Hollywood':1.5})

LOCATIONS['Universal Studios'] = Location("Universal Studios", \
  "Needed an adrenaline rush? You\'re at Universal? Tickets will cost you $500, and you\'ll need to spend 8 hours here because the lines are interminable.", \
  500, 8, \
  {'Beverly Hills':1,'Getty Center':1.5,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1.5,'LACMA':1.5,'Los Angeles City Hall':1.5,'Los Angeles Zoo':0.75,'MONA':1.5,'Norton Simon Museum':1.75,'Olvera Street':1.5,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':1.76,'Universal Studios':0,'West Hollywood':1.5})

LOCATIONS['West Hollywood'] = Location("West Hollywood", \
  "Welcome to WeHo! Early AM hours are your best bet here. Walk down the Sunset Strip and stop at all the clubs. You\'ll need to pay $300 in entrance fees, and it\'ll take about 5 hours.", \
  300, 5, \
  {'Beverly Hills':0.5,'Getty Center':0.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':1.25,'LaBrea Tar Pits':0.75,'LACMA':0.75,'Los Angeles City Hall':0.75,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':1.75,'Santa Monica Pier':1.25,'UCLA':0.75,'Union Station':1.5,'Universal Studios':1.5,'West Hollywood':0})
  
### Set Map Image
if path[0] == "/":
  mapFile = path + "/sources/map.png"
else:
  mapFile = path + "\\sources\\map.png"
global mapImage
mapImage = makePicture(mapFile)

### Initalizes Global Variables
global CURRENTLOCATION
global PREVIOUSLOCATION
global VISITEDLOCATIONS
global MONEY
global TIME

### Primary Game Play
def playGame():
  ### Defines Global Variables
  global CURRENTLOCATION
  CURRENTLOCATION = ""
  global PREVIOUSLOCATION
  PREVIOUSLOCATION = ""
  global VISITEDLOCATIONS
  VISITEDLOCATIONS = []
  global MONEY
  MONEY = randrange(1800,4800,100) ### Set Money with Random
  global TIME
  TIME = randrange(36,96,3) ### Set Time with Random

  gameInPlay = true
  playCount = 0
  attemptFailures = 3
  
  startMessage = "Welcome to BEAT LOS ANGELES\n\n"
  startMessage += "The objective of the game is to see as many sights\n"
  startMessage += "in Los Angeles on your given budget and in the\n"
  startMessage += "given amount of time. As you tour the city, a map\n"
  startMessage += "will display display to giving you an the opperunity\n"
  startMessage += "to see where you have been.\n\n"
  startMessage += "Directions: In the input box you will input the location\n"
  startMessage += "you would like to visit. Beware someplaces maybe\n"
  startMessage += "expensive and could burn up a good chunk of your time.\n\n"
  startMessage += "Enter \"help\" at any move prompt for the help info.\n"
  startMessage += "Enter \"list\" at any move prompt for the list cities.\n"
  startMessage += "Enter \"map\" at any move prompt to open the map of Los Angeles.\n"
  startMessage += "Enter \"exit\" at any move prompt to exit the game.\n"
    
  showInformation(startMessage)
  show(mapImage)

  while gameInPlay:
    userChoice = ""
  
    if playCount == 0:
      questionMessage = 'Your Starting Budget for touring Los Angels:\n'
      questionMessage += "Money: $%.2f and Time: %s\n\n" % (MONEY, convertTimeHourMin(TIME))
      questionMessage += 'Enter your first stop in Los Angeles.'
    else:
      questionMessage = 'Your Remainin Budget for touring Los Angels:\n'
      questionMessage += "Money: $%.2f and Time: %s\n\n" % (MONEY, convertTimeHourMin(TIME))
      questionMessage += 'Enter your next stop in Los Angeles.'
      
    choiceIsGood = false        
    while choiceIsGood == false:
      userChoice = requestString(questionMessage)
      choiceIsGood = validateChoice(userChoice.lower())
      if choiceIsGood:
        if userChoice.lower() == "exit":
          exitYesOrNo = requestString("Are you sure want to exit? (yes/no)")
          if exitYesOrNo.lower() == "yes":
            exitMessage = "Thank you for playing!\n"
            if len(VISITEDLOCATIONS) > 0:
              exitMessage += "Please click the OK button below,and give us a moment to"
              exitMessage += "process your postcard with the images of the places you visited."
            showInformation(exitMessage)
            gameInPlay = false
        elif userChoice.lower() == "help":
          showInformation(gameHelp())
        elif userChoice.lower() == "list":
          showInformation(listLocations())
        elif userChoice.lower() == "map":
          show(mapImage)
        else:
          correctKey = correctName(userChoice.lower())
          if CURRENTLOCATION == "":
            if checkPurse(LOCATIONS[correctKey]):
              gameInPlay = processChoice(userChoice.lower())
              playCount += 1
            else:
              if MONEY > 40 and TIME >3:
                showInformation("You don\'t have enough money or time to go to " + correctKey + "!")
                choiceIsGood = true
              else:
                showInformation("You don\'t have enough money or time to go to " + correctKey + "!")
                attemptFailures -= 1
                choiceIsGood = true
          else:
            if checkIfMoneyTimeGood(LOCATIONS[CURRENTLOCATION], LOCATIONS[correctKey]):
              if MONEY > 100 and TIME >4:
                showInformation("You don\'t have enough money or time to go to " + correctKey + "!")
                choiceIsGood = true
              else:
                showInformation("You don\'t have enough money or time to go to " + correctKey + "!")
                attemptFailures -= 1
                choiceIsGood = true
            else:
              gameInPlay = processChoice(userChoice.lower())
              playCount += 1
        if attemptFailures == 0:
          sorryMessage = "SORRY! GAME OVER!\n"
          sorryMessage += "Sorry you have made three unsuccesful attempts to\n"
          sorryMessage += "travel. You have run out of Money or Time to continue\n"
          sorryMessage += "your tour of Los Angeles. Please click the OK button\n"
          sorryMessage += "below, and give us a moment to process your postcard\n"
          sorryMessage += "with the images of the places you visited."
          showInformation(sorryMessage)
          gameInPlay = false
      

### Verifies that the User's Choice is valid for any of the locations in the game
def validateChoice(choice):
  if choice == "beverly hills" or \
    choice == "getty center" or \
    choice == "getty" or \
    choice == "grauman\'s chinese theatre" or \
    choice == "chinese theatre" or \
    choice == "griffith observatory" or \
    choice == "observatory" or \
    choice == "labrea tar pits" or \
    choice == "la brea tar pits" or \
    choice == "tar pits" or \
    choice == "lacma" or \
    choice == "los angeles city hall" or \
    choice == "la city hall" or \
    choice == "city hall" or \
    choice == "los angeles zoo" or \
    choice == "la zoo" or \
    choice == "zoo" or \
    choice == "mona" or \
    choice == "norton simon museum" or \
    choice == "norton simon" or \
    choice == "olvera street" or \
    choice == "santa monica pier" or \
    choice == "santa monica" or \
    choice == "pier" or \
    choice == "ucla" or \
    choice == "union station" or \
    choice == "universal studios" or \
    choice == "west hollywood" or \
    choice == "weho" or \
    choice == "exit" or \
    choice == "help" or \
    choice == "list" or \
    choice == "map":
    return true
  else:
    showError("Invalid entry!")
    return false

### Used to make sure the User's Choice is in correct form
### to be used as a key for the LOCATIONS dictonary    
def correctName(choice):
  if choice == "beverly hills":
    return "Beverly Hills"
  elif choice == "getty center" or \
    choice == "getty":
    return "Getty Center"
  elif choice == "grauman\'s chinese theatre" or \
    choice == "chinese theatre":
    return "Grauman\'s Chinese Theatre"
  elif choice == "griffith observatory" or \
    choice == "observatory":
    return "Griffith Observatory"
  elif choice == "labrea tar pits" or \
    choice == "la brea tar pits" or \
    choice == "tar pits":
    return "LaBrea Tar Pits"
  elif choice == "lacma":
    return "LACMA"
  elif choice == "los angeles city hall" or \
    choice == "la city hall" or \
    choice == "city hall":
    return "Los Angeles City Hall"
  elif choice == "los angeles zoo" or \
    choice == "la zoo" or \
    choice == "zoo":
    return "Los Angeles Zoo"
  elif choice == "mona":
    return "MONA"
  elif choice == "norton simon museum" or \
    choice == "norton simon":
    return "Norton Simon Museum"
  elif choice == "olvera street":
    return "Olvera Street"
  elif choice == "santa monica pier" or \
    choice == "santa monica" or \
    choice == "pier":
    return "Santa Monica Pier"
  elif choice == "ucla":
    return "UCLA"
  elif choice == "union station":
    return "Union Station"
  elif choice == "universal studios":
    return "Universal Studios"
  elif choice == "west hollywood" or \
    choice == "weho":
    return "West Hollywood"
  else:
    return ""

### Acts upon the User's Choice
def processChoice(choice):
  processString = ""
  
  if choice == "beverly hills":
    processString = processLocation(LOCATIONS['Beverly Hills'])
    
  elif choice == "getty center" or \
    choice == "getty":
    processString = processLocation(LOCATIONS['Getty Center'])
  
  elif choice == "grauman\'s chinese theatre" or \
    choice == "chinese theatre":
    processString = processLocation(LOCATIONS['Grauman\'s Chinese Theatre'])
  
  elif choice == "griffith observatory" or \
    choice == "observatory":
    processString = processLocation(LOCATIONS['Griffith Observatory'])
  
  elif choice == "labrea tar pits" or \
    choice == "la brea tar pits" or \
    choice == "tar pits":
    processString = processLocation(LOCATIONS['LaBrea Tar Pits'])
  
  elif choice == "lacma":
    processString = processLocation(LOCATIONS['LACMA'])
  
  elif choice == "los angeles city hall" or \
    choice == "la city hall" or \
    choice == "city hall":
    processString = processLocation(LOCATIONS['Los Angeles City Hall'])
  
  elif choice == "los angeles zoo" or \
    choice == "la zoo" or \
    choice == "zoo":
    processString = processLocation(LOCATIONS['Los Angeles Zoo'])
  
  elif choice == "mona":
    processString = processLocation(LOCATIONS['MONA'])
  
  elif choice == "norton simon museum" or \
    choice == "norton simon":
    processString = processLocation(LOCATIONS['Norton Simon Museum'])
  
  elif choice == "olvera street":
    processString = processLocation(LOCATIONS['Olvera Street'])
  
  elif choice == "santa monica pier" or \
    choice == "santa monica" or \
    choice == "pier":
    processString = processLocation(LOCATIONS['Santa Monica Pier'])
  
  elif choice == "ucla":
    processString = processLocation(LOCATIONS['UCLA'])
  
  elif choice == "union station":
    processString = processLocation(LOCATIONS['Union Station'])
  
  elif choice == "universal studios":
    processString = processLocation(LOCATIONS['Universal Studios'])
  
  elif choice == "west hollywood" or \
    choice == "weho":
    processString = processLocation(LOCATIONS['West Hollywood'])
  
  elif choice == "help":
    processString += "HELP" + "\n"
  
  elif choice == "list":
    processString += "LIST" + "\n"
  
  elif choice == "map":
    processString += "MAP" + "\n"
  else:
    return true
  
  showInformation(processString)
  return true

### Takes location to go to and process it, returning a string for display to player
def processLocation(location):
  global CURRENTLOCATION
  global PREVIOUSLOCATION
  global VISTEDLOCATIONS
  global TIME
  global MONEY
  
  travelTime = 0
  travelCost = 0
  PREVIOUSLOCATION = CURRENTLOCATION
  CURRENTLOCATION = location.name
  addToVisited(CURRENTLOCATION)
  returnString = location.displayLocation() + "\n"
  if PREVIOUSLOCATION != "" and PREVIOUSLOCATION != CURRENTLOCATION:
    travelTime = location.getTravelTime(PREVIOUSLOCATION)
    travelCost = travelTime * 20
    returnString += "Cost of time to travel here is " + convertTimeHourMin(travelTime) + " and $ %.2f.\n" % (travelCost)
  TIME = TIME - location.time - travelTime
  MONEY = MONEY - location.cost - travelCost
  returnString += "You have $%.2f and %s remaining in your visit to Los Angeles!" % (MONEY, convertTimeHourMin(TIME))
  return returnString

### Adds visited location to VISITEDLOCATIONS list
def addToVisited(location):
  global VISITEDLOCATIONS
  exists = false
  for visited in VISITEDLOCATIONS:
    if visited == location:
      visited = true
  if exists == false:
    VISITEDLOCATIONS.append(location)
      
### Converts Decimal time to worded string
def convertTimeHourMin(time):
  timeInMin = time * 60
  if timeInMin < 60:
    return str(int(timeInMin)) + " minutes"
  else:
    timeHour = int(time)
    timeMin = (time - float(int(time)))*60
    if timeHour > 1:
      if timeMin > 0:
        return str(timeHour) + " hours, " + str(int(timeMin)) + " minutes"
      else:
        return str(timeHour) + " hours"
    else:
      if timeMin > 0:
        return str(1) + " hour, " + str(int(timeMin)) + " minutes"
      else:
        return str(1) + " hour"

### Checks if player has enough money to go to the first location                
def checkPurse(location):
  if MONEY > location.cost:
    if TIME > location.time:
      return true
    else:
      return false
  else:
    return false
      
### Makes sure player has enough money to go from
### current location to new location before allowing travel      
def checkIfMoneyTimeGood(current, desired):
  travelToDesiredTime = current.travelTable[desired.name]
  requiredTime = desired.time + travelToDesiredTime
  requiredCost = desired.cost + (travelToDesiredTime * 20)
  if requiredCost > MONEY:
    return true
  elif requiredTime > TIME:
    return true
  else:
    return false
    
### Creates List of locations for the player to viewer
def listLocations():
  alphaList = []
  returnString = ""
  for place in LOCATIONS:
    alphaList.append(LOCATIONS[place].name)
  alphaList.sort()
  for word in alphaList:
    returnString += word + "\n"
  return returnString

def gameHelp():
  returnString = "The objective of the game is to see as many sights\n"
  returnString += "in Los Angeles on your given budget and in the\n"
  returnString += "given amount of time. As you tour the city, a map\n"
  returnString += "will display display to giving you an the opperunity\n"
  returnString += "to see where you have been.\n\n"
  returnString += "Directions: In the input box you will input the location\n"
  returnString += "you would like to visit. Beware someplaces maybe\n"
  returnString += "expensive and could burn up a good chunk of your time.\n\n"
  returnString += "Enter \"help\" at any move prompt for the help info.\n"
  returnString += "Enter \"list\" at any move prompt for the list cities.\n"
  returnString += "Enter \"map\" at any move prompt to open the map of Los Angeles.\n"
  returnString += "Enter \"exit\" at any move prompt to exit the game.\n"
  return returnString






#