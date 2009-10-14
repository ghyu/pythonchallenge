#a = [1, 11, 21, 1211, 111221, 
#len(a[30])?

def describe(x):
	ans = ''
	cur = ''
	count = 0
	for char in x:
		if cur == char:
			count +=1
		else:
			if count > 0:
				ans += '%d%s'%(count,cur)
			cur = char
			count = 1
	ans += '%d%s'%(count,cur)
	return ans

print describe('1')
print describe('1211')

def gendescs(seed):
	while(1):
	   yield seed
	   seed = describe(seed)

a = gendescs('1')

for i in range(31):
	print "len(a[%d]) = %d"%(i,len(a.next()))

