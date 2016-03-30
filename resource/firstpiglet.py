from resource import Player
import pyglet,random
from resource.carrots import carrot
game_window = pyglet.window.Window(800, 600)
pyglet.resource.path = ['../resource']
pyglet.resource.reindex()
player_image = pyglet.resource.image("player.jpg") 
asteroid_image = pyglet.resource.image("astr.jpg")
main_batch = pyglet.graphics.Batch()
player_ =Player.player(x=400,y=0,batch=main_batch)
player_.scale=0.5
def center_image(image): 
        """Sets an image's anchor point to its center""" 
        image.anchor_x = image.width/2 
        image.anchor_y = image.height/2
        
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575,batch=main_batch, color=(0, 0, 0, 255)) 
level_label = pyglet.text.Label(text="the  Game", x=400, y=575, anchor_x='center',batch=main_batch,color=(0, 0, 0, 255))
def carrot_add(num_asteroids): 
    carrots_ = [] 
    for i in range(num_asteroids): 
        new_carrot = carrot(asteroid_image,batch=main_batch)         
        new_carrot.rotation = random.randint(0, 180)
        new_carrot.x=random.randint(0,800)
        new_carrot.y = random.randint(530,600)
        carrots_.append(new_carrot) 
    return carrots_

carrotss = carrot_add(5)
sco=0
def update(dt): 
    if(random.randint(0,20)==0):
        new_carrot = carrot(asteroid_image,batch=main_batch)         
        new_carrot.rotation = random.randint(0, 180)
        new_carrot.x=random.randint(0,800)
        new_carrot.y = random.randint(530,600)
        carrotss.append(new_carrot) 
    player_.update(dt)
    for obj in carrotss: 
        obj.update(dt)
    score_label.text=player_.chek_collision(carrotss)
@game_window.event 
def on_draw():
    game_window.clear()
    main_batch.draw()
     

    
if __name__ == '__main__': 
    pyglet.gl.glClearColor(1,1,1,1)
    pyglet.clock.schedule_interval(update, 1/60.0)
    game_window.push_handlers(player_.key_handler)
    pyglet.app.run()

    