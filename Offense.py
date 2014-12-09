import urllib2

class Offense(object):
    
    def __init__(self, teamName):
        page = urllib2.urlopen("http://www.nfl.com/stats/categorystats?tabSeq=2&offensiveStatisticCategory=GAME_STATS&conference=ALL&role=TM&season=2014&seasonType=REG&d-447263-s=TOTAL_YARDS_GAME_AVG&d-447263-o=2&d-447263-n=1")
        source = page.read()
        start = source.find(teamName)        
        
        #cut to relevant statistics data
        start = source.find('<a href="/stats/categorystats?tabSeq=2&amp;season=2014&amp;seasonType=REG&amp;offensiveStatisticCategory=GAME_STATS&amp;role=TM&amp;d-447263-n=1&amp;d-447263-o=2&amp;d-447263-p=1&amp;conference=ALL&amp;d-447263-s=TURNOVER_RATIO">TO</a></th></tr>')
        end = source.find('<!-- End Data Table, if table is not null -->')
        source = source[start:end:]    
        
        #find data on team
        start = source.find(teamName)
        teamsource = source[start:]
        end = teamsource.find("</tr")
        teamsource = teamsource[:end]
        
        #splits data to a lsit of stats
        teamStats = teamsource.split("</td>")
        
        #cuts last item off list as it does not contain any relevant data
        teamStats = teamStats[:len(teamStats)-1:]
        
        #removes all irrelevant HTML tag data from statistics 
        for i in range(0,len(teamStats)):
            teamStats[i] = teamStats[i].replace("\n","")
            teamStats[i] = teamStats[i].replace("\t","")
            teamStats[i] = teamStats[i].replace("</a>","")
            j = 0
            while True and i>0:
                if not teamStats[i][j].isdigit() and not teamStats[i][j] == "." and not teamStats[i][j] == ":" and not teamStats[i][j] == "-":
                    teamStats[i] = teamStats[i].replace(teamStats[i][j],"")
                else:
                    j+=1
                if j == len(teamStats[i]):
                    break   
       #cast all num stats to floats/ints
        for i in range(1, len(teamStats)):
            try:
                teamStats[i] = int(teamStats[i])
            except ValueError:
                try:
                    teamStats[i] = float(teamStats[i])
                except ValueError:
                    pass
        
        self.gamesPlayed = teamStats[1]
        self.averagePointsPerGame = teamStats[2]
        self.totalPoints = teamStats[3]
        self.scrimmagePlays = teamStats[4]
        self.yardsPerGame = teamStats[5]
        self.yardsPerPlay = teamStats[6]
        self.firstDownsPerGame = teamStats[7]
        self.thirdDownsMade = teamStats[8]
        self.thirdDownsAttempted = teamStats[9]
        self.thirdDownPercentage = teamStats[10]
        self.fourthDownsMade = teamStats[11]
        self.fourthDownsAttempted = teamStats[12]
        self.fourthDownPercentage = teamStats[13]
        self.numOfPenalties = teamStats[13]
        self.numOfPenaltyYards = teamStats[14]
        self.timeOfPossetionPerGame = teamStats[15]
        self.numOfTotalFumbles = teamStats[16]
        self.numOfFumblesLost = teamStats[17]
        self.turnoverRatio = teamStats[18]
