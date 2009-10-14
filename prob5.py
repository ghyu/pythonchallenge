import pickle
import urllib2

url = "http://www.pythonchallenge.com/pc/def/banner.p"

uh = urllib2.urlopen(url)
p = pickle.load(uh)
uh.close()
print p
banner = ""
for row in p:
	for (c,r) in row:
		banner += c * r
	banner += "\n"
print banner
	