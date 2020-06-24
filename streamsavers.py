import pyglet
import time
from PIL import Image
import glob
import os


def main():
    path = 'E:\\Dev\\StreamSavers\\gifs\\1.gif'

    animation = pyglet.image.load_animation(path)
    animSprite = pyglet.sprite.Sprite(animation)
    
    duration = Image.open(path).info['duration']
    
    w = animSprite.width
    h = animSprite.height
    
    window = pyglet.window.Window(width=w, height=h)
    
    r,g,b,alpha = 0.5,0.5,0.8,0.5
    
    
    pyglet.gl.glClearColor(r,g,b,alpha)
    
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    def pauseAnim(self):
         time.sleep(4.0)
    
    pyglet.clock.schedule_interval(pauseAnim, duration)
    
    pyglet.app.run()

if __name__ == '__main__':
    main()