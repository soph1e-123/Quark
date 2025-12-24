from object_class import Object
from useful import sameHeight, findOverlap
import pygame

class Box(Object):
    def __init__(self, x, y, screen_size):
        super().__init__(x,y,screen_size, "box")
    
    def getVelocity(self):
        return [0,0]
    
    def collide(self, player):
        self.leftRightBounds()
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
                
        if sameHeight(self,player):
            if player.getSize()[0] + player.getPosition()[0] >= self.getPosition()[0] and player.getVelocity()[0] >= 0 and player.getSize()[0] + player.getPosition()[0] <= self.getPosition()[0] + self.getSize()[0]:
                self.setPosition([player.getSize()[0] + player.getPosition()[0], self.getPosition()[1]])

            if  player.getPosition()[0] - self.getSize()[0] <= self.getPosition()[0] and player.getVelocity()[0] <= 0 and player.getPosition()[0] >= self.getPosition()[0]:
                self.setPosition([player.getPosition()[0] - self.getSize()[0], self.getPosition()[1]])
            
            #TODO: deal with edges of screen

            if player.getPosition()[0] < 0 and self.getPosition()[0]<0 and player.getVelocity()[0] >= 0:
                self.setPosition([player.getSize()[0] + player.getPosition()[0], self.getPosition()[1]])

    


class Platform(Object):
    def __init__(self, x, y, screen_size, ratio):
        super().__init__(x,y,screen_size, "box")
        self.setSize((self.getSize()[0]*ratio, self.getSize()[1]/4))
    
    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), pygame.Rect(self.getPosition()[0], self.getPosition()[1], self.getSize()[0], self.getSize()[1]))


class Door(Object):
    def __init__(self, x, y, screen_size):
        super().__init__(x,y,screen_size, "door")
        self.setSize((self.getSize()[0], self.getSize()[1]*1.5))
        self.setPosition([x, y-self.getSize()[1]])
        self.__open = False
        self.__open_img = pygame.image.load("assets/door_open.png")
        self.__open_img = pygame.transform.scale(self.__open_img, self.getSize())
        self.__closed_img = pygame.image.load("assets/door.png")
        self.__closed_img = pygame.transform.scale(self.__closed_img, self.getSize())
    
    def draw(self, window):
        if self.__open:
            window.blit(self.__open_img, self.getPosition())
        else:
            window.blit(self.__closed_img, self.getPosition())

    def open(self):
        self.__open = True

    def collide(self, player):
        if self.__open:
            if findOverlap(self.getPosition()[1], self.getPosition()[1] + self.getSize()[1], player.getPosition()[1], player.getPosition()[1]+player.getSize()[1])>=0.3*player.getSize()[1]:
                overlap = findOverlap(self.getPosition()[0], self.getPosition()[0] + self.getSize()[0], player.getPosition()[0], player.getPosition()[0]+player.getSize()[0])
                if overlap >= 0.2*self.getSize()[0]:
                    player.setWon(True)
                    player.setPosition([self.getPosition()[0], self.getPosition()[1] + self.getSize()[1] - player.getSize()[1]])
