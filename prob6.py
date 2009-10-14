import zipfile
import urllib2
import cStringIO
import re

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
uh = urllib2.urlopen(url)
buf = cStringIO.StringIO(uh.read())
uh.close()
zfile = zipfile.ZipFile(buf)

print zfile.read('readme.txt')
print zfile.read('90052.txt')
nothing = "90052"
comments = ""
r = re.compile("(\d*)$")
def getnext(x):
	data = zfile.read('%s.txt'%x)
	m = r.search(data)
	if m is not None:
		answer = m.groups(1)[0]
		print "%s=>%s (%s)"%(x,answer,data)
		return answer
	else:
		raise "Can't match: %s"%data

while(nothing != ""):
	comments += zfile.getinfo('%s.txt'%nothing).comment
	nothing = getnext(nothing)

print comments