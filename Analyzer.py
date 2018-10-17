import operator, pickle

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

def process_words(wordList, dicti):
    wordDict = dicti
    for i in wordList:
        if i in wordDict:
            x = wordDict[i]
            x += 1
            wordDict[i] = x
        else:
            wordDict[i] = 1
    return wordDict

def sort_words(wordDict):
    sorted_wordList = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_wordList

def create_final(sorted_wordList):
    finaDict = {}
    for i in sorted_wordList:
        finaDict[i[0]] = i[1]
    return finaDict

def main(d):
    fil = open('Analysed.dat','rb')
    dicti = pickle.load(fil)
    fil.close()
    x = extract_words(d)
    y = process_words(x, dicti)
    z = sort_words(y)
    a = create_final(z)
    return a

x = main('Grimm')
print(x['the'])

file = open('Analysed.dat','wb')
y = pickle.dump(x,file)
file.close()
