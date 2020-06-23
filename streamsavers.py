import pyglet
import time
from PIL import Image
import glob
import os


def main():
    path = 'D:\\Dev\\StreamSavers\\gifs\\*.gif'
    event_loop = pyglet.app.EventLoop()

    gifs = glob.glob(path, recursive=False)
    gifnum = 0

    event_loop = pyglet.app.base.EventLoop()
        
    animation = pyglet.image.load_animation(gifs[gifnum])

    abspath = os.path.abspath(gifs[gifnum])
    duration = Image.open(abspath).info['duration']

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
        

    @event_loop.event
    def on_Window_close():
        exit()

    def pauseAnim(self):
        time.sleep(4.0)
        

    pyglet.clock.schedule_interval(pauseAnim, duration)

    pyglet.app.EventLoop().run()

if __name__ == '__main__':
    main()