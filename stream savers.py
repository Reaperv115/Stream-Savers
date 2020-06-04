from PIL import Image

image = Image.open('E:/Dev/playing_with_python/gifs/simpsons.gif', 'r')

while 1:
    image.seek(image.tell()+1)
    print(image)