import pyglet
class carrot(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(carrot, self).__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        
    def update(self, dt=None): 
        self.y -= 5
        self.rotation+=2
        
        
    def check_bounds(self):
        min_x = 0 
        min_y = 0 
        max_x = 775  
        max_y = 575 
        if self.x < min_x: 
            self.x = max_x 
        elif self.x > max_x: 
            self.x = min_x
