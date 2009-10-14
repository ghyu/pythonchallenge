from PIL import Image

im = Image.open("oxygen.png")

(top, left, width,height) = im.getbbox()

row = height / 2
data = im.getdata()
colour = 0
uniques = []

step = 0
cur = data[row*width]
while (data[row*width + step] == cur):
	step += 1

print "Step: %d"%step
step = 10
for i in range(row*width, (row+1)*width,7):
	newcol = data[i][0]
	colour = newcol
	uniques.append(colour)

print "".join([chr(x) for x in uniques])
dat =  [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join([chr(x) for x in dat])
#im.show()
