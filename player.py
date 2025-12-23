import pygame
from object_class import Object
from useful import sameHeight, findOverlap
#TODO: Fix sameHeight and collisions in general


class Player(Object):
    def __init__(self, x, y, screen_size):
        super().__init__(x,y,screen_size, "player")
        self.__start_pos = [x,y].copy()
        self.__speed = screen_size[0]/700
        self.__current_velocity = [0,0].copy()
        self.__is_jumping = False
        self.__screen_size = screen_size
        self.__frame = 0
        self.__images = [[],[],[]]
        self.__won = False
        self.__teleporting = [False,None]

        for i in range(1,5):
            current = pygame.image.load("assets/R"+str(i)+".png")
            current = pygame.transform.scale(current, self.getSize())
            self.__images[1].append(current)
            self.__images[0].append(pygame.transform.flip(current, True, False))

            forward = pygame.image.load("assets/F"+str(i%2+1)+".png")
            forward = pygame.transform.scale(forward, self.getSize())
            self.__images[2].append(forward)
        
        current = pygame.image.load("assets/jump.png")
        current = pygame.transform.scale(current, self.getSize())
        self.__images[1].append(current)
        self.__images[0].append(pygame.transform.flip(current, True, False))
        forward = pygame.image.load("assets/F2.png")
        forward = pygame.transform.scale(forward, self.getSize())
        self.__images[2].append(forward)


    def getVelocity(self):
        return self.__current_velocity

    def setVelocity(self, new_vel):
        self.__current_velocity = new_vel.copy()

    def isTeleporting(self):
        return self.__teleporting[0]
    
    def setTeleporting(self, vals):
        self.__teleporting = vals.copy()
    
    def returnTeleporting(self):
        return self.__teleporting
    
    def getWon(self):
        return self.__won

    def setWon(self, val):
        self.__won = val
    
    def isJumping(self):
        return self.__is_jumping
    
    def setJumping(self, val):
        self.__is_jumping = val
    
    def jump(self,height):
        self.__is_jumping = True
        self.__current_velocity[1] = -height*self.__speed


    def draw(self, window, opaque=True):

        if self.__current_velocity[0] < 0:
            #left
            direction = 0
        elif self.__current_velocity[0] > 0:
            #right
            direction = 1
        else:
            direction = 2
        
        if self.__is_jumping:
            frame = 4
        else:
            frame = self.__frame//20

        image = self.__images[direction][frame]
        if not opaque:
            image = image.copy()
            image.set_alpha(100)

        window.blit(image, self.getPosition())

    def animate(self):
        if not self.isJumping():
            self.__frame = (self.__frame + 1)%((len(self.__images[0])-1)*20)

    def move(self, direction):

        self.__current_velocity = [self.__speed*direction, self.__current_velocity[1] + self.__speed/4].copy()
        
        self.setPosition([self.getPosition()[0] + self.__current_velocity[0], self.getPosition()[1] + self.__current_velocity[1]])

        self.leftRightBounds()
        
        if self.getPosition()[1] > self.__screen_size[1]-self.getSize()[1]:
            self.getPosition()[1] = self.__screen_size[1]-self.getSize()[1]
            self.__current_velocity[1] = 0
            self.__is_jumping = False
        
    
    def collision(self, obj):
        y_overlap = overlap = findOverlap(self.getPosition()[1],self.getPosition()[1]+self.getSize()[1],obj.getPosition()[1],obj.getPosition()[1]+obj.getSize()[1])
        if y_overlap > 0 and y_overlap < 0.5*self.getSize()[1]:
                
            #if ((self.getPosition()[0] <= obj.getPosition()[0] + obj.getSize()[0]) and self.getPosition()[0] >= obj.getPosition()[0]) or ((self.getPosition()[0]+self.getSize()[0] >= obj.getPosition()[0])
                    #and self.getPosition()[0]+self.getSize()[0] <= obj.getPosition()[0] + obj.getSize()[0]):
                overlap = findOverlap(self.getPosition()[0], self.getPosition()[0] + self.getSize()[0], obj.getPosition()[0], obj.getPosition()[0]+obj.getSize()[0])
                if overlap >= 0.3*self.getSize()[0]:
                    if self.getPosition()[1]<obj.getPosition()[1]: #collision below player
                        self.__is_jumping = False
                        self.__current_velocity[1] = 0
                        self.setPosition([self.getPosition()[0], obj.getPosition()[1]-self.getSize()[1]])
                    else:
                        if self.__current_velocity[1] < 0:
                            self.__current_velocity[1] *= -1
                        self.setPosition([self.getPosition()[0], obj.getPosition()[1]+obj.getSize()[1]])
        else:
            if sameHeight(self, obj):
                if ((self.getPosition()[0] < obj.getPosition()[0] + obj.getSize()[0])
                    and self.getPosition()[0] > obj.getPosition()[0]):
                    self.setPosition([obj.getPosition()[0] + obj.getSize()[0], self.getPosition()[1]])


                if ((self.getPosition()[0]+self.getSize()[0] > obj.getPosition()[0])
                    and self.getPosition()[0]+self.getSize()[0] < obj.getPosition()[0] + obj.getSize()[0]):
                    if self.__current_velocity[0] > 0:
                        self.setPosition([obj.getPosition()[0] + obj.getSize()[0], self.getPosition()[1]])
    
    def respawn(self):
        self.setPosition(self.__start_pos.copy())
        self.__is_jumping = False
        self.__current_velocity = [0,0]