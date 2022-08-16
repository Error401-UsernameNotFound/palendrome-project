#the goal is to find 2 diffrent types of palendromes
#pure and ones with tails and or heads
#how to find pure palendromes; reverse it and compare it to itself
#how to find reverced palendromes, reverce it and use find on the dictionary

#how to find palendromes with tails + heads:
#have a dictionary with wordlength + last word of that length 
#use 2 lists the regular dictionary and a reverced dictionary
#compare reverced dictionary to regular using the list above
#run through both lists moving the 2 pointers as needed
#if a word on the reverced list has any of the words in the dictionary in it mark it down
#after marking all things down increment the list thats behind.

#compare logic
#keys: length of the word
#value:the word itself
#when word length goes up/stays the same replace or add that word length to the dictionary
#when word length goes down remove all entries longer than current word


dic = open("dictionary.txt",'r')
diclist = dic.readlines()
rev = open("sortedReverced.txt",'r')
revlist = rev.readlines()
dic.close()
rev.close()

Pwords:dict = {}
PWordLength = 0
PrevWord = ''
PDicWord = ''

dicPointer = 0
revPointer = 0

go = True
while go:
    dicWord = diclist[dicPointer].replace('\n','')
    revWord = revlist[revPointer].replace('\n','')
    logs = open('logs.txt','a')
    logs.write(dicWord+'\t'+revWord+'\n')
    print(dicWord,revWord)
    diclogs = open('dictionarylogs.txt','a')
    #update the dictionary

    #look through and update pwords
    if len(revWord) >= PWordLength:
        #all prevous lengths are fine just need to update this one
        Pwords.update({len(revWord):revWord})
    else:
        #all higher letter words need to be removed and replaced
        allkeys = Pwords.keys()
        for i in list(allkeys):
            if i > len(revWord):
                Pwords.pop(i)
        Pwords.update({len(revWord):revWord})
    PWordLength = len(revWord)
    tab = '\t'
    diclogs.write(tab.join(Pwords.values())+'\n')
    
    #compare words

    #dictionary check
    blank = ''
    if PDicWord != dicWord:
        #check for palendrome's
        if dicWord == blank.join(reversed(dicWord)):
            f = open('palendromes.txt','a')
            f.write(dicWord+'\n')

        #checking for inside words (will also catch tails / heads)
        insidesFound = []
        for i in Pwords.values():
            if dicWord.find(i) != -1 and i != dicWord:
                insidesFound.append(blank.join(reversed(i)))
        insides = open('insides.txt','a')
        insides.write(dicWord+'\t'+tab.join(insidesFound)+'\n')
    PDicWord = dicWord
    
    #reverce word check's
    if PrevWord != revWord:
        #check for starting or ending palendromes
        point  = 0
        for i in range(len(revWord)-1):
            point +=1
            #split word into letters and recombine
            splitWord = list(revWord)
            split1 = ''
            split2 = ''
            for a in range(len(revWord)):
                if a < point:
                    split1 += revWord[a]
                else:
                    split2 += revWord[a]
            split = [split1,split2]
            for a in split:
                if a == blank.join(reversed(a)) and len(a) > 3:
                    #one of the split is a palendrome
                    f = open('palendromeTails.txt','a')
                    f.write(tab.join(split)+'\n')   
    PrevWord = revWord

    #increment counter(s)
    if dicWord > revWord:
        revPointer += 1
    elif dicWord < revWord:
        dicPointer += 1
    else:
        if diclist[dicPointer+1] > revlist[revPointer+1]:
            revPointer += 1
        elif diclist[dicPointer+1] < revlist[revPointer+1]:
            dicPointer += 1
        else:
            dicPointer += 1
            revPointer += 1

    if dicPointer >= len(diclist) or revPointer >= len(revlist):
        go = False
