import urllib2

class Defense(object):
    
    def __init__(self, teamName):    
    
        #open and read entire defense stats webpage 
        page = urllib2.urlopen("http://www.nfl.com/stats/categorystats?tabSeq=2&defensiveStatisticCategory=GAME_STATS&conference=ALL&role=OPP&season=2014&seasonType=REG&d-447263-s=TOTAL_YARDS_GAME_AVG&d-447263-o=1&d-447263-n=1")
        source = page.read()
        
        #cut to relevant statistics data
        start = source.find('<a href="/stats/categorystats?tabSeq=2&amp;season=2014&amp;seasonType=REG&amp;role=OPP&amp;d-447263-n=1&amp;d-447263-o=2&amp;d-447263-p=1&amp;conference=ALL&amp;defensiveStatisticCategory=GAME_STATS&amp;d-447263-s=FUMBLES_LOST">Lost</a></th></tr>')
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
        self.averagePointsGivenUpPerGame = teamStats[2]
        self.totalPointsGivenUp = teamStats[3]
        self.scrimmagePlays = teamStats[4]
        self.yardsGivenUpPerGame = teamStats[5]
        self.yardsGivenUpPerPlay = teamStats[6]
        self.firstDownsGivenUpPerGame = teamStats[7]
        self.thirdDownsAllowed = teamStats[8]
        self.thirdDownsAttemptedOn = teamStats[9]
        self.thirdDownPercentage = teamStats[10]
        self.fourthDownsAllowed = teamStats[11]
        self.fourthDownsAttemptedOn = teamStats[12]
        self.fourthDownPercentage = teamStats[13]
        self.numOfPenalties = teamStats[13]
        self.numOfPenaltyYards = teamStats[14]
        self.timeOfPossetionPerGame = teamStats[15]
        self.numOfTotalFumblesRecovered = teamStats[16]
        self.numOfFumblesLost = teamStats[17]
    