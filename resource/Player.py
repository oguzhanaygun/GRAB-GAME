import math 
import pyglet
from pyglet.window import key 
from resource import carrots

class player(carrots.carrot): 
    def __init__(self, *args, **kwargs): 
        self.key_handler = key.KeyStateHandler()
        super(player, self).__init__(img= pyglet.resource.image("player.jpg") , *args, **kwargs)
        self.thrust = 300.0
        self.keys = dict(left=False, right=False)
        self.sco=0
        self.counter=0
    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.x -= self.thrust * dt
        if self.key_handler[key.RIGHT]:
            self.x += self.thrust * dt
        self.check_bounds()
        self.counter+=1
    def check_bounds(self):
        min_x = -5 
        max_x = 795  
    
        if self.x < min_x: 
            self.x = min_x 
        elif self.x > max_x: 
            self.x = max_x 
            
        
    def chek_collision(self,carrot):
        k=-1
        for i in range (len(carrot)):
            if( carrot[i].y < 155 and carrot[i].y>0  ):
                if(carrot[i].x<self.x+80 and self.x-10<carrot[i].x ):
                    k=i
        if(k>-1):
            carrot.pop(k)
            k=-1
            self.sco+=1
        return str(self.sco)