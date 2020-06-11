import pyglet
import os
from os import listdir
import time
 
listdirs = os.listdir('C:\\Users\\rjs57\\gifs')
print(listdirs)
# i = 0
# timer = 0.0

# animation = pyglet.image.Animation.from_image_sequence('C:\\Users\\rjs57\\gifs\\' + listdirs[i], 5, True)
# animSprite = pyglet.sprite.Sprite(animation)
 
 
# w = animSprite.width
# h = animSprite.height
 
# window = pyglet.window.Window(width=w, height=h)
 
# r,g,b,alpha = 0.5,0.5,0.8,0.5
 
# event_loop = pyglet.app.EventLoop()
 
# pyglet.gl.glClearColor(r,g,b,alpha)

# @window.event
# def nextAnim():
#     if animSprite.on_animation_end(animSprite):
#         i += 1
 
# @window.event
# def on_draw():
#     window.clear()
#     animSprite.draw()
    
# @event_loop.event
# def on_window_close(window):
#     event_loop.exit()
#     return pyglet.event.EVENT_HANDLED

# pyglet.app.run()
