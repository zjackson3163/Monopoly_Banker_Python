from player import Player

#creates array list of all players (min 2, max 6)
def createPlayers():
    amtPlayers = input("How many players will there be?: ")
    if int(amtPlayers) < 2:
        print("Sorry, the minimum amount of players is 2. Try again?")
        createPlayers()
    elif int(amtPlayers) > 6:
        print("Sorry, the maximum amount of players is 6. Try again?")
        createPlayers()
    else:
        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player()
        player5 = Player()
        player6 = Player()
        players = [player1, player2, player3, player4, player5, player6]
        i = 5
        while len(players) != int(amtPlayers):
            players.pop(i)
            i -= 1
        name = input("What is the first player's name?: ")
        player1.setName(name)
        i = 1
        while i != len(players):
            name = input("What is the next player's name?: ")
            players[i].setName(name)
            i += 1
        print("All players created!")
        return players

#main gameplay method. runs until end of program
def gameplay(players):  # players is an array of players created from createPlayers() method
    turn = 0
    finish = False
    while not finish:   #finish = if the user said game is finished
        turn = 0
        while turn < len(players):  #till the end of players array
            players[turn].playerAssets()
            action = input("What would you like to do for " + players[turn].getName() + "'s turn?: ")

            # skips players turn
            if action.lower() == "skip":
                print()
                turn += 1

            #allows player to buy property, houses, or hotels through buyProperty(), buyHouse(), or buyHotel() methods
            elif action.lower() == "buy":
                buyAns = input("What are you trying to buy? (Hint: property, house, or hotel): ")
                if buyAns.lower() == "property":
                    buyProperty(players[turn], propertyAvailability, properties, propertiesCost)
                    print()
                elif buyAns.lower() == "house":
                    property = input("What property are you trying to buy a house for?: ")
                    print()
                    if players[turn].ifColorSetOwned(players[turn].checkColor(property)):
                        players[turn].buyHouse(property)
                        for i in range(len(properties)):
                            if property.lower() == properties[i].lower():
                                players[turn].subBalance(propertiesCost[i])
                    print()
                elif buyAns.lower() == "hotel":
                    property = input("What property are you trying to buy a hotel for?: ")
                    if players[turn].ifColorSetOwned(players[turn].checkColor(property)):
                        players[turn].buyHotel(property)
                        for i in range(len(properties)):
                            if property.lower() == properties[i].lower():
                                players[turn].subBalance(propertiesCost[i])
                    else:
                        print("Sorry, you don't own all the prperties in the color set yet.")
                    print()
                else:
                    print("Sorry, that's not something you can buy. (Hint: Try property, house or hotel!)")
                    print()
            #allows player to pay bank or another player
            elif action.lower() == "pay":
                personToPay = input("Who would you like to pay? (Hint: bank or another player): ")
                found = False
                if personToPay == "bank":
                    amount = input("How much are you paying the bank?: ")
                    players[turn].subBalance(amount)
                else:
                    for i in range(len(players)):
                        if players[i].getName().lower() == personToPay.lower():
                            pay(players[turn],players[i])
                            found = True
                    if found == False:
                        print("Sorry, that's not a player. (Hint: Proper spelling is important!)")
            elif action.lower() == "add":
                amount = input("How much are you adding to players' balance?: ")
                players[turn].addBalance(amount)
            elif action.lower() == "bid":
                found = False
                bidPlayer = input("Who won the bidding?: ")
                for player in players:
                    if player.getName().lower() == bidPlayer.lower():
                        bidProperty(player, propertyAvailability, properties)
                        found = True
                    if found == False:
                        print("Sorry, that's not a player. (Hint: Proper spelling is important!)")
                #players[turn].bid()
            elif action.lower() == "trade":
                found = False
                personToTrade = input("Who are you trading with: ")
                for i in range(len(players)):
                    if players[i].getName().lower() == personToTrade.lower():
                        trade(players[turn], players[i])
                        found = True
                if found == False:
                    print("Sorry, that's not a player. (Hint: Proper spelling is important!)")

            else:
                print("Sorry, that's not an action available.")

            # if the player action was skip, then it was the end of their turn, no need to ask again (would skip 2 turns)
            if action != "skip":
                endOfTurn = input("Is this the end of your turn?: ")
                print()
                if endOfTurn == "yes":
                    #writes into gameData.txt each players assets after each turn
                    #will eventually use this to be able to resume old game, scrapped for now
                    gameData = open('gameData.txt', 'w')
                    for player in players:
                        gameData.write("Name: " + player.getName())
                        gameData.write("\nBalance: " + str(player.getBalance()))
                        gameData.write("\nOwned Properties: " + str(player.getProperties()))
                        gameData.write("\n\n")
                    gameData.close()
                    turn += 1

        #asks players if end of game, changes finish variable
        gameDone = input("Is this the end of your game?: ")
        print()
        if gameDone.lower() == "yes":
            finish = True
            

#pay method, lets player pay payee
def pay(player, payee):
    amount = input("How much are you paying them?: ")
    player.subBalance(amount)
    payee.addBalance(amount)


#allows players to trade properties
#player = player giving property
#tradee = player gaining property
def trade (player, tradee):
    property = input("What property are you trading?: ")
    for prop in player.getProperties():
        if property.lower() == prop.lower():
            tradee.addProperties(prop)
            player.removeProperties(prop)
            print("You've successfully traded '" + prop + "'!")
            if property.lower() == "mediterranean avenue":
                tradee.addBrown()
                player.remBrown()

            elif property.lower() == "baltic avenue":
                tradee.addBrown()
                player.remBrown()

            elif property.lower() == "oriental avenue":
                tradee.addLightBlue()
                player.remLightBlue()

            elif property.lower() == "vermont avenue":
                tradee.addLightBlue()
                player.remLightBlue()

            elif property.lower() == "connecticut avenue":
                tradee.addLightBlue()
                player.remLightBlue()

            elif property.lower() == "st. charles place":
                tradee.addPink()
                player.remPink()

            elif property.lower() == "states avenue":
                tradee.addPink()
                player.remPink()

            elif property.lower() == "virginia avenue":
                tradee.addPink()
                player.remPink()

            elif property.lower() == "st. james place":
                tradee.addOrange()
                player.remOrange()

            elif property.lower() == "tennessee avenue":
                tradee.addOrange()
                player.remOrange()

            elif property.lower() == "new york avenue":
                tradee.addOrange()
                player.remOrange()

            elif property.lower() == "kentucky avenue":
                tradee.addRed()
                player.remRed()

            elif property.lower() == "indiana avenue":
                tradee.addRed()
                player.remRed()

            elif property.lower() == "illinois avenue":
                tradee.addRed()
                player.remRed()

            elif property.lower() == "atlantic avenue":
                tradee.addYellow()
                player.remYellow()

            elif property.lower() == "ventnor avenue":
                tradee.addYellow()
                player.remYellow()

            elif property.lower() == "marvin gardens":
                tradee.addYellow()
                player.remYellow()

            elif property.lower() == "pacific avenue":
                tradee.addGreen()
                player.remGreen()

            elif property.lower() == "north carolina avenue":
                tradee.addGreen()
                player.remGreen()

            elif property.lower() == "pennsylvania avenue":
                tradee.addGreen()
                player.remGreen()

            elif property.lower() == "park place":
                tradee.addDarkBlue()
                player.remDarkBlue()

            elif property.lower() == "boardwalk":
                tradee.addDarkBlue()
                player.remDarkBlue()



#allows players to bid properties, the cost of the property is whatever cost came to at the bidding
#player = player that won bidding
#avail = availibility array
#prop = properties array
def bidProperty (player, avail, prop):
    #i = 0
    property = input("What property are you bidding?: ")
    for prop in prop:
        if property.lower() == prop.lower():
            if avail[i] == "available":
                bid = input("How much was the property bid for?: ")
                if player.subBalance(int(bid)) == True:
                    avail[i] = "taken"
                    player.addProperties(prop)
                    if property.lower() == "mediterranean avenue":
                        player.addBrown()

                    elif property.lower() == "baltic avenue":
                        player.addBrown()

                    elif property.lower() == "oriental avenue":
                        player.addLightBlue()

                    elif property.lower() == "vermont avenue":
                        player.addLightBlue()

                    elif property.lower() == "connecticut avenue":
                        player.addLightBlue()

                    elif property.lower() == "st. charles place":
                        player.addPink()

                    elif property.lower() == "states avenue":
                        player.addPink()

                    elif property.lower() == "virginia avenue":
                        player.addPink()

                    elif property.lower() == "st. james place":
                        player.addOrange()

                    elif property.lower() == "tennessee avenue":
                        player.addOrange()

                    elif property.lower() == "new york avenue":
                        player.addOrange()

                    elif property.lower() == "kentucky avenue":
                        player.addRed()

                    elif property.lower() == "indiana avenue":
                        player.addRed()

                    elif property.lower() == "illinois avenue":
                        player.addRed()

                    elif property.lower() == "atlantic avenue":
                        player.addYellow()

                    elif property.lower() == "ventnor avenue":
                        player.addYellow()

                    elif property.lower() == "marvin gardens":
                        player.addYellow()

                    elif property.lower() == "pacific avenue":
                        player.addGreen()

                    elif property.lower() == "north carolina avenue":
                        player.addGreen()

                    elif property.lower() == "pennsylvania avenue":
                        player.addGreen()

                    elif property.lower() == "park place":
                        player.addDarkBlue()

                    elif property.lower() == "boardwalk":
                        player.addDarkBlue()
                    print()
                    print("You've bought \"" + player.lastBought() + "\"!")
                    print("Current Balance: " + str(player.getBalance()))
                    print("Current Owned Properties: " + str(player.getProperties()))
            else:
                print("Sorry, that property isn't available.")
            return


#buyProperty method allows player to add property to their property array
#player = player using method
#avail = availability array
#prop = properties array
#propCost = propertiesCost array
#probably a more efficient way to do this, update in future?
def buyProperty(player, avail, prop, propCost):
    property = input("What property are you buying?: ")
    for i in range(len(prop)):
        if property.lower() == prop[i].lower():
            if avail[i] == "available":
                if player.subBalance(int(propCost[i])) == True:
                    avail[i] = "taken"
                    player.addProperties(prop[i])
                    if property.lower() == "mediterranean avenue":
                        player.addBrown()

                    elif property.lower() == "baltic avenue":
                         player.addBrown()

                    elif property.lower() == "oriental avenue":
                         player.addLightBlue()

                    elif property.lower() == "vermont avenue":
                         player.addLightBlue()

                    elif property.lower() == "connecticut avenue":
                         player.addLightBlue()

                    elif property.lower() == "st. charles place":
                         player.addPink()

                    elif property.lower() == "states avenue":
                         player.addPink()

                    elif property.lower() == "virginia avenue":
                         player.addPink()

                    elif property.lower() == "st. james place":
                         player.addOrange()

                    elif property.lower() == "tennessee avenue":
                         player.addOrange()

                    elif property.lower() == "new york avenue":
                         player.addOrange()

                    elif property.lower() == "kentucky avenue":
                         player.addRed()

                    elif property.lower() == "indiana avenue":
                         player.addRed()

                    elif property.lower() == "illinois avenue":
                         player.addRed()

                    elif property.lower() == "atlantic avenue":
                         player.addYellow()

                    elif property.lower() == "ventnor avenue":
                         player.addYellow()

                    elif property.lower() == "marvin gardens":
                         player.addYellow()

                    elif property.lower() == "pacific avenue":
                         player.addGreen()

                    elif property.lower() == "north carolina avenue":
                         player.addGreen()

                    elif property.lower() == "pennsylvania avenue":
                         player.addGreen()

                    elif property.lower() == "park place":
                         player.addDarkBlue()

                    elif property.lower() == "boardwalk":
                         player.addDarkBlue()

                    print()
                    print("You've bought \"" + player.lastBought() + "\"!")
                    print("Current Balance: " + str(player.getBalance()))
                    print("Current Owned Properties: " + str(player.getProperties()))
            else:
                print("Sorry, that property isn't available.")
            return
    print("Sorry, that isn't a property. (Tip: Make sure spelling is correct!)")


                                    #scrapped for now, never used, thought i would
                                    #def findPropertyIndex(property):
                                     #   i = 0
                                     #   for line in propertyList:
                                      #      if properties.append(line.strip()).lower() == property.lower():
                                       #         return int(i)
                                        #    i += 1


# initializes arrays for all property information

properties = []
propertiesCost = []
propertiesColors = []
buildingCosts = []
propertyAvailability = ["available"] * 28

#scrapped for now
    #opens file with former game data?

    #prevGameData = open('gameData.txt')

# opens files with property information to populate arrays
propertyList = open('Monopoly Properties.txt', 'r')
propertyCostList = open('Monopoly Properties Cost.txt', 'r')
propertyColor = open('colors.txt', 'r')
buildingCost = open('buildingCost.txt', 'r')

# populates properties array
for line in propertyList:
    properties.append(line.strip())

# populates propertiesCost array
for line in propertyCostList:
    propertiesCost.append(line.strip())

# populates propertiesColors array
for line in propertyColor:
    propertiesColors.append(line.strip())

# populates buildingCosts array
for line in buildingCost:
    buildingCosts.append(line.strip())

#formatting
print()

#intro paragraph
print(
    "Welcome to Monopoly Banker! This makes it easy to keep track of each players' balance, properties, & other assets!")
    

userAnswer = input("Would you like to see common commands?: ")
print()

#if player wants instructions or not
if userAnswer.lower() == "yes":
    print("Common commands include... \n\tskip: this will skip a player's turn (used if they are in jail) "
          "\n\tbuy: this will allow the player to buy property, houses, or hotels from the property manager and add it to their owned properties "
          "\n\tpay: this will allow the player to pay the bank or pay/donate to another player "
          "\n\tadd: this will add to the current players balance (use if passed go or got money from community chest)"
          "\n\ttrade: this will allow the player to trade properties with another player"
          "\n\tbid: this allows properties to be bid")
    print()
print("Okay! Let's get started!")


#trying to figure out a way to use old game data to resume game by creating players array with the text from the gameData file, scrapped for now,
#don't have the time, already late whoops

        #returningUser = input("Are you returning to resume a game?: ")
        #if returningUser.lower() == "yes":
        #    gameData = open("gameData.txt")
        #    for line in gameData:
        #        if line.startswith("Name: "):
        #        elif line.startswith("Balance: ")
        #        elif line.startswith("Owned Properties: ")
        #else:
            #creates array of players using createPlayers() method
        #    players = createPlayers()
        #    print()


#creates array of players using createPlayers() method
players = createPlayers()
print()

#prints array of players
i = 0
while i != len(players):
    print("Player " + str(i + 1) + ": ", end="")
    players[i].print()
    i += 1

print()
gameplay(players)
print("Thank you for using Monopoly Banker! I hope you enjoyed your game!")
