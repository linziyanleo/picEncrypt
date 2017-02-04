import sys
from PIL import Image

class Cube:
    def __init__(self):
        self.im = Image.open('ucsb.jpeg')
        #self.imenc = im
        self.cubeSize = 50
        self.size = self.im.size
    def Row(self):
        self.loop1 = self.size[0]
        self.loop2 = self.size[1]
        x = 0
        y = 0
		#for i in range(0,(self.size[0]//self.cubeSize)-2):
		#for k in range(0,(self.size[1]//self.cubeSize)-1):
	    x += self.cubeSize			
        box = (x-self.cubeSize , y , x , y+self.cubeSize)
	    leftbox = (x , y , self.loop1 , y+self.cubeSize)
    	box2 = (x+self.cubeSize , y , x+2*self.cubeSize , y+self.cubeSize)
    	self.region = self.im.crop(box)
    	self.region.load()
    	self.im.paste(self.region, box2)
#self.im.show()
c = Cube()
c.Row()
c.im.show()	
