from object_class import Object
from useful import findOverlap

class Portal(Object):
    def __init__(self, x, y, screen_size):
        super().__init__(x,y,screen_size, "portal")
        self.__connected_pos = self.getPosition()
    
    def connect(self, second_portal_pos):
        self.__connected_pos = second_portal_pos
    
    def collide(self, player):

        if findOverlap(self.getPosition()[1], self.getPosition()[1] + self.getSize()[1], player.getPosition()[1], player.getPosition()[1]+player.getSize()[1])>=0.3*player.getSize()[1]:
            overlap = findOverlap(self.getPosition()[0], self.getPosition()[0] + self.getSize()[0], player.getPosition()[0], player.getPosition()[0]+player.getSize()[0])
            if overlap >= 0.2*self.getSize()[0]:
                #teleport
                if not player.isTeleporting():
                    player.setTeleporting([True, self.__connected_pos.copy()])
                    player.setPosition([self.__connected_pos[0], self.__connected_pos[1] + self.getSize()[1] - player.getSize()[1]])
            else:
                if player.returnTeleporting()[1] == self.getPosition():
                    player.setTeleporting([False,None])
        else:
                if player.returnTeleporting()[1] == self.getPosition():
                    player.setTeleporting([False,None])