import sys
from PIL import Image

class Cube:

    def __init__(self,filename,row,rowTime):
        self.im = Image.open(filename)
        #self.imenc = im
        self.cubeSize = 10
        self.size = self.im.size
        self.r = row
        self.rt = rowTime

    def Row(self,row,rowTime):
        self.loop1 = self.size[0]
        self.loop2 = self.size[1]
        self.r = row
        self.rt = rowTime
        x = 0
        y = (self.r-1)*self.cubeSize

        for i in range(0,self.rt):
            #for k in range(0,(self.size[1]//self.cubeSize)-1):
            x += self.cubeSize
            box = (x-self.cubeSize , y , x , y+self.cubeSize)
            leftbox = (x , y , self.loop1 , y+self.cubeSize)

            box2 = (self.loop1-self.cubeSize , y , self.loop1 , y+self.cubeSize)
            leftbox2 = (x-self.cubeSize , y , self.loop1-self.cubeSize , y+self.cubeSize)
            self.region = self.im.crop(box)
            self.leftregion = self.im.crop(leftbox)
            
            self.region.load()
            self.im.paste(self.region, box2)
            
            self.leftregion.load()
            self.im.paste(self.leftregion, leftbox2)

            y += self.cubeSize

#self.im.show()
c = Cube('witcher.jpg',3,4)
c.Row(3,4)
c.im.show()    
