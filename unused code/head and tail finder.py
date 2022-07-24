
dic = open('dictionary.txt','r')
rev = open('sortedReverced.txt', 'r')
dicLines = dic.readlines()
revLines = rev.readlines()


PDicwords:dict = {}
PDicWordLength = 0

PRevwords:dict = {}
PRevWordLength = 0

PrevWord = ''
PDicWord = ''

dicPointer = 0
revPointer = 0

go = True
while go:
    dicWord = dicLines[dicPointer].replace('\n','')
    revWord = revLines[revPointer].replace('\n','')
    print(dicWord,revWord)

    #look through and update dictionary's

    #rev side
    if len(revWord) >= PRevWordLength:
        #all prevous lengths are fine just need to update this one
        PRevwords.update({len(revWord):revWord})
    else:
        #all higher letter words need to be removed and replaced
        allkeys = PRevwords.keys()
        for i in list(allkeys):
            if i > len(revWord):
                PRevwords.pop(i)
            PRevwords.update({len(revWord):revWord})
    PWordLength = len(revWord)

    #dicionary side
    if len(dicWord) >= PDicWordLength:
        #all prevous lengths are fine just need to update this one
        PDicwords.update({len(dicWord):dicWord})
    else:
        #all higher letter words need to be removed and replaced
        allkeys = PDicwords.keys()
        for i in list(allkeys):
            if i > len(dicWord):
                PDicwords.pop(i)
            PDicwords.update({len(dicWord):dicWord})
    PDicWordLength = len(dicWord)

    tab = ';'

    blank = ''
    if PDicWord != dicWord:
        #checking for inside words (will also catch tails / heads)
        HeadTail = open('forwardheadTail.txt','a')
        for i in PRevwords.values():
            head = ''
            tail = ''
            minLen = min(len(dicWord),len(i))
            if dicWord[:minLen] == i[:minLen] and minLen >= 3:
                tail = (dicWord[minLen:])
                #head =(i[minLen:])
                HeadTail.write(dicWord+ tab + ''.join(reversed(i)) + tab + tails+ '\n')
    PDicWord = dicWord

    #if PrevWord != revWord:
    #    #checking for inside words (will also catch tails / heads)
    #    HeadTail = open('headsAndTails.txt','a')
    #    for i in PDicwords.values():
    #        head = ''
    #        tail = ''
    #        minLen = min(len(i),len(revWord))
    #        if i[:minLen] == revWord[:minLen] and minLen >= 3:
    #            tail = (i[minLen:])
    #            head =(revWord[minLen:])
    #            HeadTail.write(i+ tab + tail + tab + head+ tab +revWord + '\n')
    #PrevWord = revWord



    if dicWord > revWord:
        revPointer += 1
    elif dicWord < revWord:
        dicPointer += 1
    else:
        if dicLines[dicPointer+1] > revLines[revPointer+1]:
            revPointer += 1
        elif dicLines[dicPointer+1] < revLines[revPointer+1]:
            dicPointer += 1
        else:
            dicPointer += 1
            revPointer += 1

    if dicPointer >= len(dicLines) or revPointer >= len(revLines):
        go = False
            