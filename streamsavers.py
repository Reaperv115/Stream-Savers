import pyglet
import os
from os import listdir
 
def main():
    
    cwd = os.getcwd()
    listdirs = os.listdir('D:\\Dev\\Stream-Savers\\gifs') 
    print(cwd)
    i = 0
    fullDirect = 'D:\\Dev\\Stream-Savers\\gifs\\color_ball_frames'

    file = open(fullDirect, 'rb')
    images = pyglet.resource.image(file)

    animation = pyglet.image.Animation.from_image_sequence(images, duration=5, loop=True)
    animSprite = pyglet.sprite.Sprite(animation)
    
    
    w = animSprite.width
    h = animSprite.height

    w, h = 600, 600
    
    window = pyglet.window.Window(width=w, height=h)
    
    r,g,b,alpha = 0.5,0.5,0.8,0.5
    
    event_loop = pyglet.app.EventLoop()
    
    pyglet.gl.glClearColor(r,g,b,alpha)

    
    
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
        
    @event_loop.event
    def on_window_close(window):
        event_loop.exit()
        return pyglet.event.EVENT_HANDLED

    pyglet.app.run()
    on_draw()
    on_window_close(window)

if __name__ == "__main__":
    main()
