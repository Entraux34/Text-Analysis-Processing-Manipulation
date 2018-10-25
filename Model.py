import pickle, random
	
class Word():
    def __init__(self,a,b,c,d):
        self.Word = a
        self.Occurances = b
        self.Common = c
        self.Followers = d

global pc, d, gc

file = open('relate.dat','rb')
d = pickle.load(file)
file.close()

pc = 0
gc = 0

def get_next(sw):
	global d
	starting_word = sw
	fl = find_followers(starting_word, d)
	rwn = random.randint(0,len(fl)-1)
	nw = fl[rwn]
	return nw

def find_followers(cw,d):
	x = cw
	wi = d[x]
	lf = wi.Common
	return lf

def main(sw,en):
#	global pc, gc
	global c, p
	nw = get_next(sw)
	print(nw, end = en)
	main(nw, ' ')
	c += 1
	p += 1
	if p >= 10:
		print('.', ' ')
		change_p()
#	pc += 1
#	gc += 1
#	if gc <= 100:
#		if pc < 10:
#			main(nw,' ')
#		elif pc == 10:
#			main(nw,'')
#			print('.', end = ' ')
#			pc = 0

def change_p():
	global p
	p = 0

global c, p
c = 0
p = 0
while c < 100:
	main('he',' ')







