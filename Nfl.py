from Team import *

teams = ["Arizona Cardinals" ,"Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills" , "Carolina Panthers",  "Chicago Bears", "Cincinnati Bengals",  "Cleveland Browns",  "Dallas Cowboys", "Denver Broncos", "Detroit Lions","Green Bay Packers" ,"Houston Texans","Indianapolis Colts" ,"Jacksonville Jaguars" ,"Kansas City Chiefs","Miami Dolphins", "Minnesotta Vikings", "New England Patriots" , "New Orleans Saints", "New York Jets" ,"Oakland Raiders" , "Philadelphia Eagles", "Pittsburgh Steelers", "San Diego Chargers", "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Redskins"]


#prompts the user for teams
team1Name = raw_input("Enter a team ")
temp = team1Name.split()
team1Name = ""
for i in range(0,len(temp)):
    temp[i] = temp[i].capitalize()
    team1Name += temp[i] + " "
team1Name = team1Name.strip()


cityOrName = False
for team in teams:
    if team1Name in team:
        cityOrName = True
        team1Name = team

#waits until valid team name is entered
while not cityOrName:
    team1Name = raw_input("Enter a valid team name ")
    temp = team1Name.split()
    team1Name = ""
    for i in range(0,len(temp)):
        temp[i] = temp[i].capitalize()
        team1Name += temp[i] + " "
    team1Name = team1Name.strip() 
    for team in teams:
        if team1Name in team:
            cityOrName = True
            team1Name = team    
    
#creates team objects
team1 = Team(team1Name)

#prompts the user for teams
team2Name = raw_input("Enter the opposing team ")
temp = team2Name.split()
team2Name = ""
for i in range(0,len(temp)):
    temp[i] = temp[i].capitalize()
    team2Name += temp[i] + " "
team2Name = team2Name.strip()

cityOrName = False
for team in teams:
    if team2Name in team:
        team2Name = team
        if team2Name != team1Name:
                cityOrName = True


#waits until valid team name is entered
while not cityOrName or team1Name == team2Name:
    team2Name = raw_input("Enter a valid team name ")
    temp = team2Name.split()
    team2Name = ""
    for i in range(0,len(temp)):
        temp[i] = temp[i].capitalize()
        team2Name += temp[i] + " "
    team2Name = team2Name.strip() 
    for team in teams:
        if team2Name in team:
            cityOrName = True
            team2Name = team    

team2 = Team(team2Name)


team1Total = team1.offense.averagePointsPerGame - team1.defense.averagePointsGivenUpPerGame
team2Total = team2.offense.averagePointsPerGame - team2.defense.averagePointsGivenUpPerGame

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
    favoredTeam = favoredTeam.capitalize()
    
    numPointsMustWinBy = float(raw_input("Enter the number of points they are giving up "))
    
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
print team1.name, "points scored:", team1.offense.averagePointsPerGame, "points given up:", team1.defense.averagePointsGivenUpPerGame, "points total:", team1Total
print team2.name, "points scored:", team2.offense.averagePointsPerGame, "points given up:", team2.defense.averagePointsGivenUpPerGame, "points total:", team2Total
print

if team1Total > team2Total:
    winTeam = team1
elif team2Total > team1Total:
    winTeam = team2
else:
    winTeam = "neither of the teams"


print winTeam.name, "are predicted to win by", abs(team1Total - team2Total), "points"
print

if checkPointSpread:
    if favoredTeam == winTeam.name and abs(team1Total - team2Total) > numPointsMustWinBy:
        print "Pick the", favoredTeam
    elif abs(team1Total - team2Total) == numPointsMustWinBy:
        print "Pick the home team"
    else:
        print "Pick the", underdogTeam


