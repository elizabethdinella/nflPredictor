from Offense import *
from Defense import *

class Team(object):
    
    def __init__(self, teamName):
        self.name = teamName
        self.offense = Offense(self.name)
        self.defense = Defense(self.name)
    
    def __str__(self):
        return self.name