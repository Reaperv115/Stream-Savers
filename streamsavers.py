import pyglet
from pathlib import Path
import imageio
 
image_path = Path('gifs')
images = list(image_path.glob('*.gif'))
print(images)


# animation = pyglet.sprite.Sprite(images[0])

# width = animation.width
# height = animation.height

# window = pyglet.window.Window(width, height)

# @window.event
# def onDraw():
#     window.clear()
#     animation.draw()

# pyglet.app.run()