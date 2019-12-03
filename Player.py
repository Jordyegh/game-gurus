class Player:
    def __init__(self, name = 'Player', health = 5, armor = 0, id = 0):
        self.health = health
        self.armor = armor
        self.name = name
        self.KDRatio = [0, 0]
        self.inventory = []
        self.id = id
        
    def destroy(self):
        del self
