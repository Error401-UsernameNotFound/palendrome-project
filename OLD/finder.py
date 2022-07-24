#probably going to be a slow script
from xml.dom.minidom import AttributeList


dic = open("dictionary.txt", 'r')
diclist = dic.readlines()
rev = open("sortedreverced.txt",'r')
revlist = rev.readlines()


GBPs = {
    'a':0,'b':16373,'c':17012,'d':30702,'e':61596,'f':118554,'g':119726,'h':139219,'i':145289,'j':148661,'k':148691,'l':152226,'m':170549,'n':180948,'o':206586,'p':210163,'q':212900,'r':212930,'s':233698,'t':309363,'u':330142,'v':330954,'w':331095,'x':332048,'y':333075,'z':368720
} #go back points


def search(word:str,letter:str):
    search = True
    count = 0
    found = []
    while search: #start the search
        dicw = diclist[GBPs[letter]+count].replace("\n","") #get the right letter
        if word.find(dicw) != -1 and revW != dicw: #if the dictionarty word is in the backword word add it
            found.append(dicw)
            print("found",word,dicw)
        if (len(dicw) == 1 or GBPs[letter]+count >= len(diclist)-1) and dicw != letter: #if we the next letter is found stop
            search = False
        count += 1
    return found


for revW in revlist:
    revW = revW.replace("\n","")
    count = 0
    found = []
    Letters = [] 
    for i in range(len(revW)): #split it into letters
        Letters.append(revW[i])
    #filter letters for same letters & last letter
    Letters.pop(len(Letters)-1) # the last letter will never have any word besides itself
    for i in Letters:
        for a in range(Letters.count(i)-1):
            Letters.remove(i) #removes all accurence but 1
    Letters.sort()
    for i in Letters:
        found += search(revW,i) #look through all letters
    #record data
    for i in found:
        for a in range(found.count(i)-1):
            found.remove(i) #removes duplicates
    joiner = '\t'
    Flist = open("found2.txt",'a')
    Flist.write(revW+'\t'+joiner.join(found)+'\n')
        
                



#garbage

#for revW in revlist:
#    revW = revW.replace("\n","")
#    found = []
#    for dicW in diclist:
#        dicW = dicW.replace("\n","")
#        if revW.find(dicW) != -1 and revW != dicW and len(dicW) != 1:
#            found.append(dicW)
#            print("found",revW,dicW)
#    tmp = '\t'
#    Flist = open("found.txt",'a')
#    Flist.write(revW+'\t'+tmp.join(found)+'\n')



