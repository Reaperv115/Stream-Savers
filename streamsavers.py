import pyglet
from pathlib import Path
import imageio
 
image_path = Path('gifs')
images = list(image_path.glob('*.gif'))


animation = pyglet.sprite.Sprite(images[0])

width = animation.width
height = animation.height

window = pyglet.window.Window(width, height)

@window.event
def onDraw():
    window.clear()
    animation.draw()

pyglet.app.run()

# animation = pyglet.image.load_animation('gifs/homer.gif')
# animSprite = pyglet.sprite.Sprite(animation)
 
 
# w = animSprite.width
# h = animSprite.height
 
# window = pyglet.window.Window(width=w, height=h)
 
# r,g,b,alpha = 0.5,0.5,0.8,0.5
 
 
# pyglet.gl.glClearColor(r,g,b,alpha)
 
# @window.event
# def on_draw():
#     window.clear()
#     animSprite.draw()
 
 
 
# pyglet.app.run()