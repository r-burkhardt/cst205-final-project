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
LOCATIONS = []
LOCATIONS.append(Location("Beverly Hills", \
  "Have you got enough cash? Head down Rodeo Drive, your visit is here is going to take 8 hours to get through every store. The time here is going to cost you $1500", \
  1500, 8, \
  {'Beverly Hills':0,'Getty Museum':0.75,'Grauman\'s Chinese Theater':0.50,'Griffith Observatory':1.25,'LaBrea Tar Pits':0.50,'LACMA':0.50,'Los Angeles City Hall':1.25,'Los Angeles Zoo':1.50,'MONA':2.00,'Norton Simon Museum':2.25,'Olvera Street':1.25,'Santa Monica Pier':0.75,'UCLA':0.50,'Union Station':1.50,'Universal Studios':1.00,'West Hollywood':0.50}))

LOCATIONS.append(Location("Getty Museum", \
  "Art aficionado? You\'ve come to the right place. Getty\'s entrance fee is $100, and to appreciate every painting, you\'ll need to spend 4 hours here.", \
  100, 4, \
  {'Beverly Hills':0.75,'Getty Museum':0,'Grauman\'s Chinese Theater':1.25,'Griffith Observatory':1.75,'LaBrea Tar Pits':1,'LACMA':0.75,'Los Angeles City Hall':1.75,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.25,'Olvera Street':1.75,'Santa Monica Pier':1,'UCLA':0.5,'Union Station':1.75,'Universal Studios':1.5,'West Hollywood':0.75}))

LOCATIONS.append(Location("Grauman's Chinese Theater", \
  "", \
  150, 3,
  {'Beverly Hills':.5,'Getty Museum':1.25,'Grauman\'s Chinese Theater':0,'Griffith Observatory':0.5,'LaBrea Tar Pits':1,'LACMA':1,'Los Angeles City Hall':0.75,'Los Angeles Zoo':0.5,'MONA':0.75,'Norton Simon Museum':1.25,'Olvera Street':0.75,'Santa Monica Pier':1.75,'UCLA':1.25,'Union Station':0.75,'Universal Studios':0.75,'West Hollywood':0.75}))

LOCATIONS.append(Location("Griffith Observatory", \
  "Galileo? Copernicus? Thought they were dead? They come alive here at the observatory? $50 to use the telescope, and spend 4 hours here to really stargaze properly.", \
  50, 4, \
  {'Beverly Hills':1.25,'Getty Museum':1.75,'Grauman\'s Chinese Theater':0.5,'Griffith Observatory':0,'LaBrea Tar Pits':1,'LACMA':1,'Los Angeles City Hall':0.75,'Los Angeles Zoo':0.5,'MONA':0.75,'Norton Simon Museum':1.75,'Olvera Street':0.75,'Santa Monica Pier':2,'UCLA':2,'Union Station':0.75,'Universal Studios':0.75,'West Hollywood':1.25}))

LOCATIONS.append(Location("LaBrea Tar Pits", \
  "Travel back in time to the Ice Age. Explore fossils here and visit the tar pits from those olden days. Incidentally, you\'ll need to pay $50 for this adventure, and spend 2 hours here.", \
  50, 2, \
  {'Beverly Hills':0.5,'Getty Museum':1,'Grauman\'s Chinese Theater':1,'Griffith Observatory':1,'LaBrea Tar Pits':0,'LACMA':0.25,'Los Angeles City Hall':1,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':1,'Santa Monica Pier':1,'UCLA':0.5,'Union Station':1,'Universal Studios':1.5,'West Hollywood':0.75}))
  
LOCATIONS.append(Location("LACMA", \
  "We\'ve got special exhibits here, plus a great collection of art. Spend 4 hours here before moving on, and don\'t forget to pay the $100 entrance fee.", \
  100, 4, \
  {'Beverly Hills':1,'Getty Museum':0.75,'Grauman\'s Chinese Theater':1,'Griffith Observatory':1,'LaBrea Tar Pits':0.25,'LACMA':0,'Los Angeles City Hall':1.25,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':1.25,'Santa Monica Pier':1.25,'UCLA':0.5,'Union Station':1.25,'Universal Studios':1.75,'West Hollywood':0.75,}))

LOCATIONS.append(Location("Los Angeles City Hall", \
  "Want to bother your city officials to lower your water bill. City Hall is the place! It\'s even free, but they\'re very stubborn, so allot at least an hour for your conversation.", \
  0, 1, \
  {'Beverly Hills':1.25,'Getty Museum':1.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1,'LACMA':1.25,'Los Angeles City Hall':0,'Los Angeles Zoo':1.25,'MONA':1.25,'Norton Simon Museum':1.5,'Olvera Street':0.25,'Santa Monica Pier':1.75,'UCLA':1.5,'Union Station':0.25,'Universal Studios':1.5,'West Hollywood':1.75}))

LOCATIONS.append(Location("Los Angeles Zoo", \
  "Welcome to the LA Zoo, where you\'re in the company of lions, tigers, and zebras. Admission is $90, and you\'ll need to spend another $10 to hydrate yourself. 4 hours will give you enough time to pet every animal.", \
  100, 4, \
  {'Beverly Hills':1.5,'Getty Museum':1.75,'Grauman\'s Chinese Theater':0.5,'Griffith Observatory':0.5,'LaBrea Tar Pits':1.75,'LACMA':1.75,'Los Angeles City Hall':1.25,'Los Angeles Zoo':0,'MONA':0.5,'Norton Simon Museum':1,'Olvera Street':1.25,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':1.25,'Universal Studios':0.75,'West Hollywood':1.75}))

LOCATIONS.append(Location("MONA", \
  "", \
  100, 4, \
  {'Beverly Hills':2,'Getty Museum':2,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':2,'LACMA':2,'Los Angeles City Hall':1.25,'Los Angeles Zoo':0.5,'MONA':0,'Norton Simon Museum':0.75,'Olvera Street':1.25,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':1.25,'Universal Studios':1.5,'West Hollywood':2}))

LOCATIONS.append(Location("Norton Simon Museum", \
  "", \
  100, 4, \
  {'Beverly Hills':2.25,'Getty Museum':2.25,'Grauman\'s Chinese Theater':1.25,'Griffith Observatory':1.75,'LaBrea Tar Pits':2.5,'LACMA':2.5,'Los Angeles City Hall':1.5,'Los Angeles Zoo':1,'MONA':0.75,'Norton Simon Museum':0,'Olvera Street':1,'Santa Monica Pier':2.5,'UCLA':2.25,'Union Station':1,'Universal Studios':1.75,'West Hollywood':2.5}))

LOCATIONS.append(Location("Olvera Street", \
  "Love a good bargain? Come visit Olvera Street and haggle the prices. You\'re on LA\'s first street. You\'ll be surprised how much money you\'ll need: $400, but with 3 hours of shopping, you\'ll come home with arms loaded.", \
  400, 3, \
  {'Beverly Hills':1.25,'Getty Museum':1.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1,'LACMA':1.25,'Los Angeles City Hall':0.25,'Los Angeles Zoo':1.25,'MONA':1.25,'Norton Simon Museum':1,'Olvera Street':0,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':0.25,'Universal Studios':1.5,'West Hollywood':1.75}))

LOCATIONS.append(Location("Santa Monica Pier", \
  "", \
  300, 4, \
  {'Beverly Hills':0.75,'Getty Museum':1,'Grauman\'s Chinese Theater':1.75,'Griffith Observatory':2,'LaBrea Tar Pits':1,'LACMA':1.25,'Los Angeles City Hall':1.75,'Los Angeles Zoo':2,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':2,'Santa Monica Pier':0,'UCLA':0.75,'Union Station':2,'Universal Studios':2,'West Hollywood':1.25}))

LOCATIONS.append(Location("UCLA", \
  "Ready to get smart? You\'re at UCLA, one of the top public universities nationally. You need to study for an exam for 3 hours, so head straight to the library! The textbook will cost you $100.", \
  100, 3, \
  {'Beverly Hills':0.5,'Getty Museum':0.5,'Grauman\'s Chinese Theater':1.25,'Griffith Observatory':2,'LaBrea Tar Pits':0.5,'LACMA':0.5,'Los Angeles City Hall':1.5,'Los Angeles Zoo':1.75,'MONA':1.75,'Norton Simon Museum':2.25,'Olvera Street':1.75,'Santa Monica Pier':0.75,'UCLA':0,'Union Station':1.75,'Universal Studios':1.75,'West Hollywood':0.75}))

LOCATIONS.append(Location("Union Station", \
  "", \
  50, 2, \
  {'Beverly Hills':1.5,'Getty Museum':1.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1,'LACMA':1,'Los Angeles City Hall':0.25,'Los Angeles Zoo':1.25,'MONA':1.25,'Norton Simon Museum':1,'Olvera Street':0.25,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':0,'Universal Studios':1.75,'West Hollywood':1.5}))

LOCATIONS.append(Location("Universal Studios", \
  "Needed an adrenaline rush? You\'re at Universal? Tickets will cost you $500, and you\'ll need to spend 8 hours here because the lines are interminable.", \
  500, 8, \
  {'Beverly Hills':1,'Getty Museum':1.5,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':0.75,'LaBrea Tar Pits':1.5,'LACMA':1.5,'Los Angeles City Hall':1.5,'Los Angeles Zoo':0.75,'MONA':1.5,'Norton Simon Museum':1.75,'Olvera Street':1.5,'Santa Monica Pier':2,'UCLA':1.75,'Union Station':1.76,'Universal Studios':0,'West Hollywood':1.5}))

LOCATIONS.append(Location("West Hollywood", \
  "Welcome to WeHo! Early AM hours are your best bet here. Walk down the Sunset Strip and stop at all the clubs. You\'ll need to pay $300 in entrance fees, and it\'ll take about 5 hours.", \
  300, 5, \
  {'Beverly Hills':0.5,'Getty Museum':0.75,'Grauman\'s Chinese Theater':0.75,'Griffith Observatory':1.25,'LaBrea Tar Pits':0.75,'LACMA':0.75,'Los Angeles City Hall':0.75,'Los Angeles Zoo':1.75,'MONA':2,'Norton Simon Museum':2.5,'Olvera Street':1.75,'Santa Monica Pier':1.25,'UCLA':0.75,'Union Station':1.5,'Universal Studios':1.5,'West Hollywood':0}))

### Set Map Image
if path[0] == "/":
  mapFile = path + "/sources/map.png"
else:
  mapFile = path + "\\sources\\map.png"
global mapImage
mapImage = makePicture(mapFile)

### Defines Global Variables
global CURRENTLOCATION
global PREVIOUSLOCATION
global VISITEDLOCATIONS
global MONEY
global TIME

### Primary Game Play
def playGame():
  ### Set Time and Money with Random
  global MONEY
  MONEY = randrange(2900,6000,100)
  global TIME
  TIME = randrange(56,112,2)
  
  startMessage = "Welcome to BEAT LOS ANGELES\n\n"
  startMessage += "The objective of the game is to see as many sights\n"
  startMessage += "in Los Angeles on your given budget and in the\n"
  startMessage += "given amount of time. As you tour the city, a map\n"
  startMessage += "will display display to giving you an the opperunity\n"
  startMessage += "to see where you have been.\n\n"
  startMessage += "Directions: here\n"
  startMessage += "Enter \"map\" at any move prompt for the help info.\n"
  startMessage += "Enter \"help\" at any move prompt for the help info.\n"
  startMessage += "Enter \"exit\" at any move prompt to exit the game.\n"

  showInformation(startMessage)
  
  show(mapImage)

  gameInPlay = true

  while gameInPlay:
    userChoice = ""
  
    choiceIsGood = false
  
    while choiceIsGood == false:
      userChoice = requestString('Enter your option.')
      choiceIsGood = validateChoice(userChoice.lower())
      
      gameInPlay = processChoice(userChoice.lower())
      
      




def validateChoice(choice):
  if choice == "beverly hills" or \
    choice == "getty center" or \
    choice == "getty museum" or \
    choice == "getty" or \
    choice == "grauman\'s chinese theater" or \
    choice == "chinese theater" or \
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

def processChoice(choice):
  global CURRENTLOCATION
  global PREVIOUSLOCATION
  global VISTEDLOCATIONS
  global TIME
  global MONEY
  
  processString = ""
  
  if choice == "beverly hills":
    processString += LOCATIONS[0].displayLocation() + "\n"
    print LOCATIONS[0].getTravelTime('Getty Museum')
    
  elif choice == "getty center" or \
    choice == "getty museum" or \
    choice == "getty":
    processString += LOCATIONS[1].displayLocation() + "\n"
  
  elif choice == "grauman\'s chinese theatre" or \
    choice == "chinese theatre":
    processString += LOCATIONS[2].displayLocation() + "\n"
  
  elif choice == "griffith observatory" or \
    choice == "observatory":
    processString += LOCATIONS[3].displayLocation() + "\n"
  
  elif choice == "labrea tar pits" or \
    choice == "la brea tar pits" or \
    choice == "tar pits":
    processString += LOCATIONS[4].displayLocation() + "\n"
  
  elif choice == "lacma":
    processString += LOCATIONS[5].displayLocation() + "\n"
  
  elif choice == "los angeles city hall" or \
    choice == "la city hall" or \
    choice == "city hall":
    processString += LOCATIONS[6].displayLocation() + "\n"
  
  elif choice == "los angeles zoo" or \
    choice == "la zoo" or \
    choice == "zoo":
    processString += LOCATIONS[7].displayLocation() + "\n"
  
  elif choice == "mona":
    processString += LOCATIONS[8].displayLocation() + "\n"
  
  elif choice == "norton simon museum" or \
    choice == "norton simon":
    processString += LOCATIONS[9].displayLocation() + "\n"
  
  elif choice == "olvera street":
    processString += LOCATIONS[10].displayLocation() + "\n"
  
  elif choice == "santa monica pier" or \
    choice == "santa monica" or \
    choice == "pier":
    processString += LOCATIONS[11].displayLocation() + "\n"
  
  elif choice == "ucla":
    processString += LOCATIONS[12].displayLocation() + "\n"
  
  elif choice == "union station":
    processString += LOCATIONS[13].displayLocation() + "\n"
  
  elif choice == "universal studios":
    processString += LOCATIONS[14].displayLocation() + "\n"
  
  elif choice == "west hollywood" or \
    choice == "weho":
    processString += LOCATIONS[15].displayLocation() + "\n"
  
  elif choice == "help":
    processString += "HELP" + "\n"
  
  elif choice == "list":
    processString += "LIST" + "\n"
  
  elif choice == "map":
    processString += "MAP" + "\n"
  
  elif choice == "exit":
    exitYesOrNo = requestString("Are you sure want to exit? (yes/no)")
    if exitYesOrNo.lower() == "yes":
      exitMessage = "Thank you for playing!\n"
      exitMessage += "Please click the OK button below,and give us a moment to\n"
      exitMessage += "process your postcard with the images of the places you visited."
      showInformation(exitMessage)
      return false
  else:
    return true
  
  showInformation(processString)
  return true

#def









#