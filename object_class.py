import pygame
from useful import sameHeight, findOverlap

class Object:
    def __init__(self, x, y, screen_size, object_type):
        self.__size = [screen_size[0]/20, screen_size[0]/20]
        self.__position = [x,y-self.__size[1]].copy()
        self.__image = pygame.image.load("assets/"+ object_type +".png")
        self.__image = pygame.transform.scale(self.__image, self.__size)
        self.__screen_size = screen_size

    def getPosition(self):
        return self.__position
    
    def setPosition(self, new):
        self.__position = new.copy()

    def getSize(self):
        return self.__size
    
    def setSize(self, new):
        self.__size = new
    
    def draw(self, window, opaque=True):
        if opaque:
            window.blit(self.__image, self.__position)
        else:
            image = self.__image.copy()
            image.set_alpha(100)
            window.blit(image, self.__position)
    
    def leftRightBounds(self):
        self.__position[0] = (self.__position[0]+self.getSize()[0])%(self.__screen_size[0]+self.getSize()[0])-self.getSize()[0]

        """if self.getPosition()[0]+0.5*self.__size[0] < 0:
            self.__position[0] = self.__screen_size[0]+self.getPosition()[0]
        
        elif self.getPosition()[0]+0.5*self.__size[0] > self.__screen_size[0]:
            self.__position[0] = self.getPosition()[0]-self.__screen_size[0]"""
    
    def collide(self, player):
        obj = self
        y_overlap = overlap = findOverlap(player.getPosition()[1],player.getPosition()[1]+player.getSize()[1],obj.getPosition()[1],obj.getPosition()[1]+obj.getSize()[1])
        if y_overlap > 0 and y_overlap < 0.5*player.getSize()[1]:
                
            #if ((player.getPosition()[0] <= obj.getPosition()[0] + obj.getSize()[0]) and player.getPosition()[0] >= obj.getPosition()[0]) or ((player.getPosition()[0]+player.getSize()[0] >= obj.getPosition()[0])
                    #and player.getPosition()[0]+player.getSize()[0] <= obj.getPosition()[0] + obj.getSize()[0]):
                overlap = findOverlap(player.getPosition()[0], player.getPosition()[0] + player.getSize()[0], obj.getPosition()[0], obj.getPosition()[0]+obj.getSize()[0])
                if overlap >= 0.3*player.getSize()[0]:
                    if player.getPosition()[1]<obj.getPosition()[1]: #collision below player
                        player.setJumping(False)
                        player.setVelocity([player.getVelocity()[0], 0])
                        player.setPosition([player.getPosition()[0], obj.getPosition()[1]-player.getSize()[1]])

                    else:
                        if player.getVelocity()[1] < 0:
                            player.getVelocity()[1] *= -1
                        player.setPosition([player.getPosition()[0], obj.getPosition()[1]+obj.getSize()[1]])
                    return True
        else:
            if sameHeight(player, obj):
                if ((player.getPosition()[0] < obj.getPosition()[0] + obj.getSize()[0])
                    and player.getPosition()[0] > obj.getPosition()[0]):
                    player.setPosition([obj.getPosition()[0] + obj.getSize()[0], player.getPosition()[1]])
                    return True

                if ((player.getPosition()[0]+player.getSize()[0] > obj.getPosition()[0])
                    and player.getPosition()[0]+player.getSize()[0] < obj.getPosition()[0] + obj.getSize()[0]):
                    if player.getVelocity()[0] > 0:
                        player.setPosition([obj.getPosition()[0] + obj.getSize()[0], player.getPosition()[1]])
                    return True
        return False