import pyglet
import time

    
animation = pyglet.image.load_animation('gifs/JOJO_Animated.gif')
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

def pauseAnim(self):
    time.sleep(1.0)

pyglet.clock.schedule_interval_soft(pauseAnim, 2.7)
pyglet.app.run()