# Monopoly Tracker

class Player(object):
    def __init__(self):
        self.name = " "
        self.balance = 1500
        self.properties = []

        #was going to try it with a dictionary, but i feel current method is more effective?
        #self.colorSet = {
        #    "brown":0,
        #    "lightBlue":0,
        #    "pink":0,
        #    "orange":0,
        #    "red": 0,
        #    "yellow": 0,
        #    "green":0,
        #    "darkBlue":0
        #}

        # initializes colors of properties player has
        self.brown = 0
        self.lightBlue = 0
        self.pink = 0
        self.orange = 0
        self.red = 0
        self.yellow = 0
        self.green = 0
        self.darkBlue = 0

        # initializes amt of houses player has
        self.brownHouses = [0]*2
        self.lightBlueHouses = [0]*3
        self.pinkHouses = [0]*3
        self.orangeHouses = [0]*3
        self.redHouses = [0]*3
        self.yellowHouses = [0]*3
        self.greenHouses = [0]*3
        self.darkBlueHouses = [0]*2

        # initializes amt of hotels player has
        self.brownHotels = [0]*2
        self.lightBlueHotels = [0]*3
        self.pinkHotels = [0]*3
        self.orangeHotels = [0]*3
        self.redHotels = [0]*3
        self.yellowHotels = [0]*3
        self.greenHotels = [0]*3
        self.darkBlueHotels = [0]*2

    #sets player name
    def setName(self, name):
        self.name = name

    #gets player name
    def getName(self):
        return self.name

    #gets player name
    def getBalance(self):
        return self.balance

    #subtracts money from player balance
    def subBalance(self, num):
        if self.balance >= int(num):
            self.balance -= int(num)
            return True
        else:
            print("Sorry, you don't have enough to make that payment.")
            return False

    #adds money to player balance
    def addBalance(self, num):
        self.balance += int(num)

    #returns array of player properties
    def getProperties(self):
        return self.properties

    #add property to player property array
    def addProperties(self, property):
        self.properties.append(property)

    def removeProperties(self, prop):
        self.properties.remove(prop)

    #returns last bought property 
    def lastBought(self):
        return self.properties[len(self.properties) - 1]

    #adds color to whatever color variable
    def addBrown(self):
            self.brown += 1

    def addLightBlue(self):
            self.lightBlue += 1

    def addPink(self):
            self.pink += 1

    def addOrange(self):
            self.orange += 1

    def addRed(self):
            self.red += 1

    def addYellow(self):
            self.yellow += 1

    def addGreen(self):
            self.green += 1

    def addDarkBlue(self):
            self.darkBlue += 1

# removes color from whatever color variable
    def remBrown(self):
        self.brown -= 1

    def remLightBlue(self):
        self.lightBlue -= 1

    def remPink(self):
        self.pink -= 1

    def remOrange(self):
        self.orange -= 1

    def remRed(self):
        self.red -= 1

    def remYellow(self):
        self.yellow -= 1

    def remGreen(self):
        self.green -= 1

    def remDarkBlue(self):
        self.darkBlue -= 1


    #checks color of each property
    def checkColor(self, property):
        if property.lower() == "mediterranean avenue":
            return "brown"

        elif property.lower() == "baltic avenue":
            return "brown"

        elif property.lower() == "oriental avenue":
            return "lightBlue"

        elif property.lower() == "vermont avenue":
            return "lightBlue"

        elif property.lower() == "connecticut avenue":
            return "lightBlue"

        elif property.lower() == "st. charles place":
            return "pink"

        elif property.lower() == "states avenue":
            return "pink"

        elif property.lower() == "virginia avenue":
            return "pink"

        elif property.lower() == "st. james place":
            return "orange"

        elif property.lower() == "tennessee avenue":
            return "orange"

        elif property.lower() == "new york avenue":
            return "orange"

        elif property.lower() == "kentucky avenue":
            return "red"

        elif property.lower() == "indiana avenue":
            return "red"

        elif property.lower() == "illinois avenue":
            return "red"

        elif property.lower() == "atlantic avenue":
            return "yellow"

        elif property.lower() == "ventnor avenue":
            return "yellow"

        elif property.lower() == "marvin gardens":
            return "yellow"

        elif property.lower() == "pacific avenue":
            return "green"

        elif property.lower() == "north carolina avenue":
            return "green"

        elif property.lower() == "pennsylvania avenue":
            return "green"

        elif property.lower() == "park place":
            return "darkBlue"

        elif property.lower() == "boardwalk":
            return "darkBlue"

    #returns true if player owns all properties in color set and false if not
    def ifColorSetOwned(self, color):
        if color == "brown":
            if self.brown == 2:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False
        elif color == "lightBlue":
            if self.lightBlue == 3:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False
        elif color == "pink":
            if self.pink == 3:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False
        elif color == "orange":
            if self.orange == 3:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False
        elif color == "red":
            if self.red == 3:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False
        elif color == "yellow":
            if self.yellow == 3:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False
        elif color == "green":
            if self.green == 3:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False
        else:
            if self.darkBlue == 2:
                return True
            else:
                print("Sorry, you don't own the full color set yet.")
                return False

    #checks if player has houses on property, if more than 4 returns false, if not true, meaning they can buy more
    def checkHouses(self, property):
        if property.lower() == "mediterranean avenue" :
            if self.brownHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "baltic avenue" :
            if self.brownHouses[1] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "oriental avenue" :
            if self.lightBlueHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "vermont avenue" :
            if self.lightBlueHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "connecticut avenue" :
            if self.lightBlueHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "st. charles place" :
            if self.pinkHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "states avenue" :
            if self.pinkHouses[1] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "virginia avenue" :
            if self.pinkHouses[2] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False

        elif property.lower() == "st. james place" :
            if self.orangeHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "tennessee avenue" :
            if self.orangeHouses[1] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "new york avenue" :
            if self.orangeHouses[2] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "kentucky avenue" :
            if self.redHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "indiana avenue" :
            if self.redHouses[1] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "illinois avenue" :
            if self.redHouses[2] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "atlantic avenue" :
            if self.yellowHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "ventnor avenue" :
            if self.yellowHouses[1] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "marvin gardens" :
            if self.yellowHouses[2] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "pacific avenue" :
            if self.greenHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "north carolina avenue" :
            if self.greenHouses[1] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "pennsylvania avenue" :
            if self.greenHouses[2] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "park place" :
            if self.darkBlueHouses[0] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        elif property.lower() == "boardwalk" :
            if self.darkBlueHouses[1] < 4:
                return True
            else:
                print("You aready have the max amount of houses on this property (4).")
                return False
        else:
            "Sorry, that's not a property. (Tip: Make sure spelling is correct!)"
            return False

    #checks if player has hotels on property if more than 1 returns false, if less than one, return true, meaning they can buy more
    def checkHotels(self, property):
        if property.lower() == "mediterranean avenue" :
            if self.brownHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "baltic avenue" :
            if self.brownHotels[1] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "oriental avenue" :
            if self.lightBlueHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "vermont avenue" :
            if self.lightBlueHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "connecticut avenue" :
            if self.lightBlueHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "st. charles place" :
            if self.pinkHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "states avenue" :
            if self.pinkHotels[1] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "virginia avenue" :
            if self.pinkHotels[2] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False

        elif property.lower() == "st. james place" :
            if self.orangeHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "tennessee avenue" :
            if self.orangeHotels[1] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "new york avenue" :
            if self.orangeHotels[2] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "kentucky avenue" :
            if self.redHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "indiana avenue" :
            if self.redHotels[1] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "illinois avenue" :
            if self.redHotels[2] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "atlantic avenue" :
            if self.yellowHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "ventnor avenue" :
            if self.yellowHotels[1] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "marvin gardens" :
            if self.yellowHotels[2] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "pacific avenue" :
            if self.greenHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "north carolina avenue" :
            if self.greenHotels[1] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "pennsylvania avenue" :
            if self.greenHotels[2] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "park place" :
            if self.darkBlueHotels[0] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        elif property.lower() == "boardwalk" :
            if self.darkBlueHotels[1] < 1:
                return True
            else:
                print("You aready have the max amount of hotels on this property (1).")
                return False
        else:
            "Sorry, that's not a property. (Tip: Make sure spelling is correct!)"
            return False

    #adds to *color*Houses[] array, checks if houses more than 4, if not returns true
    def buyHouse(self, property):
        if property.lower() == "mediterranean avenue":
            if self.checkHouses(property):
                self.brownHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "baltic avenue":
            if self.checkHouses(property):
                self.brownHouses[1] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "oriental avenue":
            if self.checkHouses(property):
                self.lightBlueHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "vermont avenue":
            if self.checkHouses(property):
                self.lightBlueHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "connecticut avenue":
            if self.checkHouses(property):
                self.lightBlueHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "st. charles place":
            if self.checkHouses(property):
                self.pinkHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "states avenue":
            if self.checkHouses(property):
                self.pinkHouses[1] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "virginia avenue":
            if self.checkHouses(property):
                self.pinkHouses[2] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "st. james place":
            if self.checkHouses(property):
                self.orangeHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "tennessee avenue":
            if self.checkHouses(property):
                self.orangeHouses[1] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "new york avenue":
            if self.checkHouses(property):
                self.orangeHouses[2] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "kentucky avenue":
            if self.checkHouses(property):
                self.redHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "indiana avenue":
            if self.checkHouses(property):
                self.redHouses[1] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "illinois avenue":
            if self.checkHouses(property):
                self.redHouses[2] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "atlantic avenue":
            if self.checkHouses(property):
                self.yellowHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "ventnor avenue":
            if self.checkHouses(property):
                self.yellowHouses[1] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "marvin gardens":
            if self.checkHouses(property):
                self.yellowHouses[2] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "pacific avenue":
            if self.checkHouses(property):
                self.greenHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "north carolina avenue":
            if self.checkHouses(property):
                self.greenHouses[1] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "pennsylvania avenue":
            if self.checkHouses(property):
                self.greenHouses[2] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "park place":
            if self.checkHouses(property):
                self.darkBlueHouses[0] += 1
                print("You've bought one house.")
                return True
        elif property.lower() == "boardwalk":
            if self.checkHouses(property):
                self.darkBlueHouses[1] += 1
                print("You've bought one house.")
                return True
        else:
            "Sorry, that's not a property. (Tip: Make sure spelling is correct!)"
            return False

    # adds to *color*Hotels[] array, checks if hotels more than 4, if not returns true
    def buyHotel(self, property):
        if property.lower() == "mediterranean avenue":
            if self.checkHotels(property):
                self.brownHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "baltic avenue":
            if self.checkHotels(property):
                self.brownHotels[1] += 1
                print("You've bought one hotel. " )
        elif property.lower() == "oriental avenue":
            if self.checkHotels(property):
                self.lightBlueHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "vermont avenue":
            if self.checkHotels(property):
                self.lightBlueHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "connecticut avenue":
            if self.checkHotels(property):
                self.lightBlueHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "st. charles place":
            if self.checkHotels(property):
                self.pinkHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "states avenue":
            if self.checkHotels(property):
                self.pinkHotels[1] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "virginia avenue":
            if self.checkHotels(property):
                self.pinkHotels[2] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "st. james place":
            if self.checkHotels(property):
                self.orangeHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "tennessee avenue":
            if self.checkHotels(property):
                self.orangeHotels[1] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "new york avenue":
            if self.checkHotels(property):
                self.orangeHotels[2] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "kentucky avenue":
            if self.checkHotels(property):
                self.redHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "indiana avenue":
            if self.checkHotels(property):
                self.redHotels[1] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "illinois avenue":
            if self.checkHotels(property):
                self.redHotels[2] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "atlantic avenue":
            if self.checkHotels(property):
                self.yellowHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "ventnor avenue":
            if self.checkHotels(property):
                self.yellowHotels[1] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "marvin gardens":
            if self.checkHotels(property):
                self.yellowHotels[2] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "pacific avenue":
            if self.checkHotels(property):
                self.greenHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "north carolina avenue":
            if self.checkHotels(property):
                self.greenHotels[1] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "pennsylvania avenue":
            if self.checkHotels(property):
                self.greenHotels[2] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "park place":
            if self.checkHotels(property):
                self.darkBlueHotels[0] += 1
                print("You've bought one hotel. ")
        elif property.lower() == "boardwalk":
            if self.checkHotels(property):
                self.darkBlueHotels[1] += 1
                print("You've bought one hotel. ")
        else:
            "Sorry, that's not a property. (Tip: Make sure spelling is correct!)"

    #print players stats/assets
    def playerAssets(self):
        print(self.name + "\nBalance: $" + str(self.balance) + "\nOwned properties: " + str(self.properties))

    #prints player name
    def print(self):
        print(self.name)
