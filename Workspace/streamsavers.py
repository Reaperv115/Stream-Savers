import pyglet
import os
from os import listdir
import time
 
listdirs = os.listdir('C:\\Users\\rjs57\\gifs')
i = 3
timer = 0.0

animation = pyglet.image.load_animation('C:\\Users\\rjs57\\gifs\\' + listdirs[i])
animSprite = pyglet.sprite.Sprite(animation)
 
 
w = animSprite.width
h = animSprite.height
 
window = pyglet.window.Window(width=w, height=h)
 
r,g,b,alpha = 0.5,0.5,0.8,0.5
 
event_loop = pyglet.app.EventLoop()
 
pyglet.gl.glClearColor(r,g,b,alpha)
 
@window.event
def on_draw():
    window.clear()
    animSprite.draw()
    
@event_loop.event
def onWindowClose(window):
    event_loop.exit()
    return pyglet.event.EVENT_HANDLED


while True:
    pyglet.clock.tick()

    for window in pyglet.app.windows:
        event_loop.run()
        window.switch_to()
        window.dispatch_events()
        window.dispatch_event('on_draw')
        window.dispatch_event('onWindowClose')
        window.flip()

    
 
 
#pyglet.app.run()
