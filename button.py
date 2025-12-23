from object_class import Object
from useful import sameHeight, findOverlap
import pygame.image, pygame.transform

class Button(Object):
    def __init__(self, x, y, screen_size):
        super().__init__(x,y,screen_size, "button")
        self.__pressed = False
        self.__pressed_img = pygame.image.load("assets/button_p.png")
        self.__pressed_img = pygame.transform.scale(self.__pressed_img, self.getSize())
        self.__unpressed_img = pygame.image.load("assets/button.png")
        self.__unpressed_img = pygame.transform.scale(self.__unpressed_img, self.getSize())
    
    def setPressed(self, val):
        self.__pressed = val
    
    def getPressed(self):
        return self.__pressed
        
    def collide(self, player):
        if sameHeight(player, self):
            overlap = findOverlap(self.getPosition()[0], self.getPosition()[0] + self.getSize()[0], player.getPosition()[0], player.getPosition()[0]+player.getSize()[0])
            if overlap >= 0.2*self.getSize()[0]:
                return True
            return False

    def draw(self, window, opaque=True):
        if self.__pressed:
            image = self.__pressed_img
        else:
            image = self.__unpressed_img
        
        if not opaque:
            image = image.copy()
            image.set_alpha(100)
        
        window.blit(image, self.getPosition())


class Bounce(Object):
    def __init__(self, x, y, screen_size):
        super().__init__(x,y,screen_size, "button")
        self.__pressed = False
        self.__pressed_img = pygame.image.load("assets/bounce_pressed.png")
        self.__pressed_img = pygame.transform.scale(self.__pressed_img, self.getSize())
        self.__unpressed_img = pygame.image.load("assets/bounce_unpressed.png")
        self.__unpressed_img = pygame.transform.scale(self.__unpressed_img, self.getSize())
    
    def collide(self, player):
        if sameHeight(player, self):
            overlap = findOverlap(self.getPosition()[0], self.getPosition()[0] + self.getSize()[0], player.getPosition()[0], player.getPosition()[0]+player.getSize()[0])
            if overlap >= 0.2*self.getSize()[0]:
                self.__pressed = True
                player.jump(8)
            else:
                self.__pressed = False
        else:
            self.__pressed = False

    def draw(self, window, opaque=True):
        if self.__pressed:
            image = self.__pressed_img
        else:
            image = self.__unpressed_img

        window.blit(image, self.getPosition())
