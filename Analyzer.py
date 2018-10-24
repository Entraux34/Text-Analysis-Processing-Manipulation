import operator, pickle

class Word():
    def __init__(self,a,b,c,d):
        self.Word = a
        self.Occurances = b
        self.Common = c
        self.Followers = d

#@profile
def followers(word, wordList, t):
    x = word
    if x in t:
        b = t[x].Followers
    else:
        b = {}
    for i in range(0,len(wordList)-1):
        if wordList[i] == x:
            if wordList[i+1] in b:
               y = b[wordList[i+1]]
               y += 1
               b[wordList[i+1]] = y
            else:
                b[wordList[i+1]] = 1

    h = sorted(b.items(), key=operator.itemgetter(1), reverse=True)
    s = {}
    
    for i in h:
        s[i[0]] = i[1]
        
    f = []
    c = 0
    for i in s:
        f.append(i)
        c+=1
        if c > 15:
            break
    return f, b

#@profile
def extract_words(source):
    file = open(source+'.txt','r')
    wordList = []
    try:
        x = file.readlines()
        for j in x:
            y = j.split(' ')
            for i in y:
                z = i.strip(',!?\n.":; ')
                if z != '':
                    wordList.append(z.lower())
                else:
                    continue
    except EOFError:
        print('File has been read')
    file.close()
    return wordList

#@profile
def process_words(wordList, dicti):
    wordDict = dicti
    for i in range (0,len(wordList)-1):
        if wordList[i] in wordDict:
            x = wordDict[wordList[i]]
            x += 1
            wordDict[wordList[i]] = x
        else:
            wordDict[wordList[i]] = 1
    return wordDict

#@profile
def sort_words(wordDict):
    sorted_wordList = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_wordList

#@profile
def create_final(sorted_wordList):
    finaDict = {}
    for i in sorted_wordList:
        finaDict[i[0]] = i[1]
    return finaDict

#@profile
def main(d):
    try:
        fil = open('Analysed.dat','rb')
        dicti = pickle.load(fil)
        fil.close()
    except:
        dicti = {}
    x = extract_words(d)
    y = process_words(x, dicti)
    z = sort_words(y)
    a = create_final(z)
    return a, x

x, l = main('Dracula')
print(x['the'])

file = open('Analysed.dat','wb')
y = pickle.dump(x,file)
file.close()

current = open('relate.dat','rb')
t = pickle.load(current)
current.close()

final = {}
c =0
for i in x:
    fl, fd = followers(i,l, t)
    obj = Word(i,x[i],fl,fd)
    final[i] = obj
    c += 1
#    if c > 30000:
#        break

Relate = open('relate.dat','wb')
pickle.dump(final, Relate)
Relate.close()



