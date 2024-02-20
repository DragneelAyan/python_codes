#class
class Valorant:
    def __init__(self, kills, map): #Initialize our objects using this constructor method
        self.kills = kills #self referencing object variables
        self.map = map
        
    def type(self):
        print('Action 5 man PvP shooting FPS game')
        
    def agents(self):
        print('This game have a lot of agents')
        
'''        
#objects       
game1 = Valorant()
game1.type()

#attributes
game1.kills = 30
game1.map = 'Breeze'

print(game1.kills)
print(game1.map)


game2 = Valorant()
print(game2.kills) #AttributeError: 'Valorant' object has no attribute 'kills'

game2 = Valorant()
game2.agent = 'Cypher'
print(game2.agent)
'''
game3 = Valorant(30, 'Breeze') #Take argument using constructor
print(game3.kills)


