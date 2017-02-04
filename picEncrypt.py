import sys
from PIL import Image

class Cube:
    def __init__(self):
        self.im = Image.open('cat.jpg')
        #self.imenc = im
        self.cubeSize = 8
        self.size = self.im.size
    def Row(self):
        self.loop1 = self.size[0]
        self.loop2 = self.size[1]
        x = 0
        y = (rowLine-1)*self.cubeSize
        
        for i in range(0,(self.size[0]//self.cubeSize)-1):
            #for k in range(0,(self.size[1]//self.cubeSize)-1):
            x += i*self.cubeSize
            box = (x,x,y,y)
            box2 = (x+8,x+8,y,y)
            region = im.crop(box)
            im.paste(region, box2)
