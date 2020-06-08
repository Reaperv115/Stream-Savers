import pyglet
import os
from os import listdir
 
listdirs = os.listdir('C:\\Users\\rjs57\\gifs')
i = 0
timer = 0.0

animation = pyglet.image.load_animation('C:\\Users\\rjs57\\gifs\\' + listdirs[i])
animSprite = pyglet.sprite.Sprite(animation)
 
 
w = animSprite.width
h = animSprite.height
 
window = pyglet.window.Window(width=w, height=h)
 
r,g,b,alpha = 0.5,0.5,0.8,0.5
 
 
pyglet.gl.glClearColor(r,g,b,alpha)
 
@window.event
def on_draw():
    window.clear()
    animSprite.draw()

    # if timer >= 5.0:
    #     if i > listdirs.__sizeof__:
    #     i += 1
 
 
 
pyglet.app.run()
