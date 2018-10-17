import time as t
import random as r

alph = 'abcdefghijklmnopqrstuvwxyz'
alphl = list(alph)

x = 1
w = ''
count = 0

fil = open('dictionary.txt','r')
lines = fil.read().split()
fil.close()


def gen_Random(x,w,lines,c):
    file = open('indic.txt','w')
    fi = open('notindic.txt','w')
    fi1 = open('test.txt','w')
    biglist = []
    timeout = t.time() + 30
    for k in range(1000):
#    while t.time() < timeout:
        x = x+1
        wlen = r.randint(3,12)
        for i in range (wlen):
            y = r.randint(0,25)
            w += alphl[y]
        if w in lines:
            print (str(x)+' : '+w,file=file)
            biglist.append(w)
            c += 1
        else:
            print (str(x)+' : '+w,file=fi)
            biglist.append(w)
        w = ''
    log = open('log data :'+str(timeout)+'log.txt','w')
    print('There were',str(c),'real word in this test',file=log)
    print(biglist, file=fi1)
    log.close()
    file.close()
    fi.close()
    fi1.close()

gen_Random(x,w,lines,count)
