from object_class import Object

class Spike(Object):
    def __init__(self, x, y, screen_size):
        super().__init__(x,y,screen_size,"spike")
    
    def collide(self, player):
        collision = super().collide(player)
        if collision:
            player.respawn()
            player.setReset(True)
