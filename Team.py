from Offense import *
from Defense import *

class Team(object):
    
    def __init__(self, teamName):
        self.name = teamName
        self.offense = Offense(self.name)
        self.defense = Defense(self.name)
        self.pointRatio = self.offense.averagePointsPerGame - self.defense.averagePointsGivenUpPerGame #used to compare with other teams: not really a ratio, just didn't know what else to name it
    
    def __str__(self):
        return self.name
    
    def __gt__(self, other):
        if int(self.pointRatio) > int(other.pointRatio):
            return self
        else:
            return other
        
    def __lt__(self, other):
        if int(self.pointRatio) < int(other.pointRatio):
            return self
        else:
            return other
            