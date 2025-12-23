import pygame
from copy import copy



class Level():
    def __init__(self, player1, objects1, panel1, buttons, boxes1, door, background):
        self.__background = background
        self.__player = [player1, None]
        self.__objects = [objects1, []]
        self.__buttons = [buttons, []] #change to one button affects the other
        self.__boxes = [boxes1, []]
        self.__panels = [panel1, None]
        self.__door = door
        self.__copy = None
    
    def getPlayer(self, index):
        return self.__player[index]
    
    def getObjects(self, index):
        return self.__objects[index]
    
    def getPanel(self, index):
        return self.__panels[index]

    def getDoor(self):
        return self.__door

    def getBoxes(self, index):
        return self.__boxes[index]
    
    def getButtons(self, index):
        return self.__buttons[index]

    def setDoor(self, val):
        self.__door = val

    def merge(self):
        self.__panels[1] = None
        self.__objects[1] = []
        self.__player[1] = None
        self.__buttons[1] = []
        self.__boxes[1] = []

    def make_copy(self):
        copy_player = copy(self.__player[0])
        copy_objects = []
        copy_boxes = []
        copy_buttons = []
        for item in self.__objects[0]:
            copy_objects.append(copy(item))
        for box in self.__boxes[0]:
            copy_boxes.append(copy(box))
        for button in self.__buttons[0]:
            copy_buttons.append(copy(button))
        copy_panel = copy(self.__panels[0])

        self.__copy = Level(copy_player, copy_objects, copy_panel, copy_buttons, copy_boxes, copy(self.__door), self.__background) 


    
    def split(self):
        self.__player[1] = copy(self.__player[0])
        copy_player = copy(self.__player[0])
        self.__objects[1] = []
        copy_objects = []
        copy_boxes = []
        copy_buttons = []
        for item in self.__objects[0]:
            self.__objects[1].append(copy(item))
            copy_objects.append(copy(item))
        for box in self.__boxes[0]:
            self.__boxes[1].append(copy(box))
            copy_boxes.append(copy(box))
        for button in self.__buttons[0]:
            self.__buttons[1].append(button)
            copy_buttons.append(copy(button))
            
        self.__panels[1] = copy(self.__panels[0])
        copy_panel = copy(self.__panels[0])

        self.__copy = Level(copy_player, copy_objects, copy_panel, copy_buttons, copy_boxes, copy(self.__door), self.__background) 


    def get_copy(self):
        return self.__copy
    
    def displayCopy(self):
        #only display the things that can move or change state
        for box in self.__copy.getBoxes(0):
            box.draw(self.__panels[0], opaque=False)
            box.draw(self.__panels[1], opaque=False)

        for button in self.__copy.getButtons(0):
            button.draw(self.__panels[0], opaque=False)
            button.draw(self.__panels[1], opaque=False)

        self.__copy.getPlayer(0).draw(self.__panels[0], opaque=False)
        self.__copy.getPlayer(0).draw(self.__panels[1], opaque=False)

        
    def display(self, window, screen_size):
        window.fill((41,18,64))
        #display copy but translucent

        if self.__panels[1] is not None:
            self.__panels[0].blit(self.__background, (0,0))
            self.__panels[1].blit(self.__background, (0,0))
            
            if self.__copy is not None:
               self.displayCopy()

            for i in range(0,2):
                self.__door.draw(self.__panels[i])

                objects = self.__objects[i]
                for item in objects:
                    item.draw(self.__panels[i])
                
                for box in self.__boxes[i]:
                    box.draw(self.__panels[i])

                for button in self.__buttons[i]:
                    button.draw(self.__panels[i])

                self.__player[i].draw(self.__panels[i])

            window.blit(self.__panels[0], (0, 0))
            window.blit(self.__panels[1], (0, screen_size[1]/2))
            pygame.draw.line(window, (255,255,255), (0,screen_size[1]/2), (screen_size[0], screen_size[1]/2), 5)

        else:
            self.__panels[0].blit(self.__background, (0,0))
            self.__door.draw(self.__panels[0])
            objects = self.__objects[0]
            for item in objects:
                item.draw(self.__panels[0])
            for box in self.__boxes[0]:
                box.draw(self.__panels[0])

            for button in self.__buttons[0]:
                button.draw(self.__panels[0])
            self.__player[0].draw(self.__panels[0])
            window.blit(self.__panels[0], (0, screen_size[1]/4))
            pygame.draw.line(window, (255,255,255), (0,screen_size[1]/4), (screen_size[0], screen_size[1]/4), 5)
            pygame.draw.line(window, (255,255,255), (0,3*screen_size[1]/4), (screen_size[0], 3*screen_size[1]/4), 5)   

    def checkCollisions(self, current_panel):
        
        self.__door.collide(self.__player[current_panel])
        for item in self.__objects[current_panel]:
            item.collide(self.__player[current_panel])

        for box in self.__boxes[current_panel]:
            box.collide(self.__player[current_panel])

        for button in self.__buttons[current_panel]:
            pressed = False
            if button.collide(self.__player[0]):
                pressed = True
            
            for box in self.__boxes[0]:
                if button.collide(box):
                    pressed = True
            
            if self.__panels[1] is not None:
                if button.collide(self.__player[1]):
                    pressed = True
            
                for box in self.__boxes[1]:
                    if button.collide(box):
                        pressed = True
            
            button.setPressed(pressed)
        
    def allPressed(self):
        for button in self.__buttons[0]:
            if not button.getPressed():
                return False
        return True