import pyglet
import glob
import os
import msvcrt

directory = os.getcwd()

path = 'gifs/*.gif'
gifnum = 0

if msvcrt.kbhit():
    gifnum = gifnum + 1

gifs = glob.glob(path, recursive=False)

# images = [pyglet.resource.image('gifs/patrick_frames/0.gif'),
#           pyglet.resource.image('gifs/patrick_frames/1.gif'),
#           pyglet.resource.image('gifs/patrick_frames/3.gif')]

# animation = pyglet.image.Animation.from_image_sequence(images, duration=0.1, loop = True)

animation = pyglet.image.load_animation(gifs[gifnum])
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
 
 
 
if __name__ == "__main__":
    pyglet.app.run()