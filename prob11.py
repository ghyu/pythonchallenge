from PIL import Image,ImageDraw

im = Image.open("cave.jpg")

(top,left,width,height) = im.getbbox()

o1 = Image.new('RGBA',(width/2,height/2))
o2 = Image.new('RGBA',(width,height))

imd = im.getdata()
o1d = ImageDraw.Draw(o1)
o2d = ImageDraw.Draw(o2)


for x in range(width):
	for y in range(height):
		if ((x%2)== 0 and (y%2)==0):
			o1d.point((x/2,y/2),fill=imd[y*width+x])

o1.show()

