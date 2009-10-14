import re
import urllib2

nothing = "12345"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

r = re.compile("([0-9]*)$")

def findnext(n):
	uh = urllib2.urlopen(url%n)
	dat = uh.read()
	uh.close()
	m = r.search(dat)
	if m is None:
		raise "Can't find number in text: %s"%dat
	else:
		answer =  m.groups(1)[0]
		print "%s=>%s (%s)"%(n,answer,dat)
		return answer
nothing = "46059"
while(nothing != ""):
	nothing = findnext(nothing)
