class Valorant:
    def __init__(self, kills, map): #Initialize our objects using this constructor method
        self.kills = kills #self referencing object variables
        self.map = map
        
    def gameType(self):
        print('Valorant - Action 5 man PvP shooting FPS game')
        
    def agents(self):
        print('This game have a lot of agents')
        

class Jett(Valorant):
    def __init__(self, kills, map): #Initialize our objects using this constructor method
        self.kills = kills #self referencing object variables
        self.map = map
        
    def playType(self):
        print('Duelist')
        
    def ult(self):
        print('Cannot use ult properly')
        
        
class Chamber(Valorant):
    def __init__(self, kills, map): #Initialize our objects using this constructor method
        self.kills = kills #self referencing object variables
        self.map = map
        
    def role(self):
        print('Sentinel')
        
    def ult(self):
        print('Ult is op and much useful')
#Hierarchical inheritance": One class is inherited by more than one class.         
        
game1 = Jett(17, 'Ascent')
game1.gameType()
game1.ult()

game2 = Chamber(27, 'Ascent')
game2.agents()
game2.role()