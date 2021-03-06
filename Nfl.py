from Team import *

teams = ["Arizona Cardinals" ,"Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills" , "Carolina Panthers",  "Chicago Bears", "Cincinnati Bengals",  "Cleveland Browns",  "Dallas Cowboys", "Denver Broncos", "Detroit Lions","Green Bay Packers" ,"Houston Texans","Indianapolis Colts" ,"Jacksonville Jaguars" ,"Kansas City Chiefs","Miami Dolphins", "Minnesota Vikings", "New England Patriots" , "New Orleans Saints", "New York Giants", "New York Jets" ,"Oakland Raiders" , "Philadelphia Eagles", "Pittsburgh Steelers", "San Diego Chargers", "San Francisco 49ers", "Seattle Seahawks", "St. Louis Rams","Tampa Bay Buccaneers", "Tennessee Titans", "Washington Redskins"]

#checks if team name entered is valid
def isValidName(name):
    temp = name.split()
    name = ""
    for i in range(0,len(temp)):
        temp[i] = temp[i].capitalize()
        name += temp[i] + " "
    name = name.strip()   
    for team in teams:
        if name in team:
            name = team
            return name
    return False

def isTeamInGame(name, gameNumber):
    temp = name.split()
    name = ""
    for i in range(0,len(temp)):
        temp[i] = temp[i].capitalize()
        name += temp[i] + " "
    name = name.strip()
    for team in games[gameNumber]:
        if name in team:
            name = team
            return name
    return False

#pulls games this week from foxsports.com. Date handling is done by website
games = [] 
def getGamesThisWeek():
    page = urllib2.urlopen("http://www.foxsports.com/nfl/schedule")
    source = page.read()
    start = source.find("gameDetails")
    while start > 0:
        source = source[start:]
        game = [] #list of both teams 
        for i in range(0, 2):
            start = source.find("teamInfo")
            source = source[start:]
            start = source.find("<span>")
            source = source[start:]
            source = source[len("<span>"):]
            start = source.find("<span>")
            source = source[(start+ len("<span>")):]
            end = source.find("</span>")
            game.append(source[:end:])
        games.append(game)
        start = source.find("gameDetails")


getGamesThisWeek()
while(True):

    realGame = raw_input("Do you want to view a game this week? (y/n) ")
    realGame = realGame.lower()

    #waits until the user enters a valid response
    while True:
        if realGame == "y":
            realGame = True
            break
        elif realGame == "n":
            realGame = False
            break
        else:
            realGame = raw_input("Do you want to view a game this week? (y/n) ")
            realGame = realGame.lower()  

    if realGame:
        for i in range(0,len(games)):
            print
            for j in range(0,2):
                for team in teams:
                    if games[i][j] in team:
                        games[i][j] = team
                if j==0:
                    print "%d. %s vs." %(i+1,games[i][j]),
                else:
                    print games[i][j]
            print

        gameNum = raw_input("Pick a game (1-16) ")
        while not gameNum.isdigit() or (int(gameNum)  > 16 or int(gameNum) < 1):
            gameNum = raw_input("Enter a game between 1 and 16 ")

        gameNum = int(gameNum)
        gameNum = gameNum-1
        
        team1 = Team(games[gameNum][0])
        team2 = Team(games[gameNum][1])


    else:
        #prompts the user for team1
        team1Name = raw_input("Enter a team ")
        
        #waits until valid team1 name is entered
        while not isValidName(team1Name):
            team1Name = raw_input("Enter a valid team name ")
        
        team1Name = isValidName(team1Name)    
        
        #creates team1 object
        team1 = Team(team1Name)
        
        #prompts the user for team
        team2Name = raw_input("Enter the opposing team ")
        if isValidName(team2Name):
            team2Name = isValidName(team2Name)
        
        #waits until valid team2 name is entered and not the same as team1
        while team1Name == team2Name or not isValidName(team2Name):
            while not isValidName(team2Name):
                team2Name = raw_input("Enter the opposing team ")
            while team1Name == team2Name:
                team2Name = raw_input("Enter a different opposing team ")
                team2Name = isValidName(team2Name)
    
        #creates team2 object
        team2 = Team(team2Name)
    
    checkPointSpread = raw_input("Do you want the point spread to be accounted for in this prediction? (y/n) ")
    checkPointSpread = checkPointSpread.lower()
    
    #wait until user enters valid response
    while True:
        if checkPointSpread == "y":
            checkPointSpread = True
            break
        elif checkPointSpread == "n":
            checkPointSpread = False
            break
        else:
            checkPointSpread = raw_input("Do you want the point spread to be accounted for in this prediction? (y/n) ")
            checkPointSpread = checkPointSpread.lower()  
    
    if checkPointSpread:
        favoredTeam = raw_input("Enter the favored team ")
        if not realGame:
            while not (favoredTeam == team1Name or favoredTeam == team2Name) or not isValidName(team2Name):
                while not isValidName(favoredTeam):
                    favoredTeam = raw_input("Enter the favored team ")
                favoredTeam = isValidName(favoredTeam)
                while not (favoredTeam == team1Name or favoredTeam == team2Name):
                    favoredTeam = raw_input("Enter a team playing ")
                    favoredTeam = isValidName(favoredTeam)
        else:
            while not isTeamInGame(favoredTeam, gameNum):
                favoredTeam = raw_input("Enter the favored team " )

            favoredTeam = isTeamInGame(favoredTeam, gameNum)

        numPointsMustWinBy = raw_input("Enter the number of points they are giving up ")
        while not isinstance(numPointsMustWinBy, float):
            try:
                numPointsMustWinBy = float(numPointsMustWinBy)
            except ValueError:
                numPointsMustWinBy = raw_input("Enter the number of points they are giving up ")
        
        if favoredTeam == team1.name:
            underdogTeam = team2.name
        else:
            underdogTeam = team1.name
        
        gameHeader = "%s (-%.1f) vs %s" %(favoredTeam, numPointsMustWinBy, underdogTeam)
        
    else:
        gameHeader = "%s vs %s" %(team1.name, team2.name)
    
    print
    print gameHeader
    print
    print team1.name, "points scored:", team1.offense.averagePointsPerGame, "points given up:", team1.defense.averagePointsGivenUpPerGame, "points total:", team1.pointRatio
    print team2.name, "points scored:", team2.offense.averagePointsPerGame, "points given up:", team2.defense.averagePointsGivenUpPerGame, "points total:", team2.pointRatio
    print
    
    if team1.pointRatio > team2.pointRatio:
        winTeam = team1
    elif team2.pointRatio > team1.pointRatio:
        winTeam = team2
    else:
        winTeam = "neither of the teams"
        
    predictedScore = abs(team1.pointRatio - team2.pointRatio)
    
    print winTeam.name, "are predicted to win by", predictedScore , "points"
    print
    
    if checkPointSpread:
        if favoredTeam == winTeam.name and predictedScore > numPointsMustWinBy:
            print "Pick the %s." %(favoredTeam),
        elif predictedScore == numPointsMustWinBy:
            if not realGame:
                print "Pick the home team.",
            else:
                print "Pick the %s." %(team2.name),
        else:
            print "Pick the %s." %(underdogTeam),

        confidence = abs(predictedScore - numPointsMustWinBy)
        print "Confidence:", confidence
        if confidence < 1:
            print "NOTE: low confidence. Do not pick this game."
        print
    
    
