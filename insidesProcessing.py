#tasks
#read a line split into word and all reverce words inside it
#put words the words inside (if any) on both sides of the word and check for paledrome

def palendromCheck(word:str):
    if word == ''.join(reversed(word)):
        return True
    else:
        return False

insides = open('insides.txt','r')
insidelist = insides.readlines()


tab = '\t'
for i in insidelist:
    i = i.replace('\n','')
    firstSplit = i.split(tab)
    word = firstSplit.pop(0)
    print(word)
    try :
        firstSplit.pop(firstSplit.index(''))
    except:
        pass
    for a in firstSplit: #whatever's left
        #combine in 2 ways, a +word or word + a
        #way 1
        fappend = open('head and tail.txt','a')
        #find head / tail
        aPos = word.find(''.join(reversed(a)))
        if aPos != -1:
            if aPos == 0:
                #a has a tail
                #find tail
                tail = ''
                for b in range(len(word)):
                    if b > len(a)-1:
                        tail += word[b]
                fappend.write(word+tab + ',' + tab + a +tab+ tail + '\n')
            else:
                head = ''
                tail = ''
                for b in range(len(word)):
                    if b < aPos:
                        head += word[b]
                    if b > len(a)-1 + aPos:
                        tail += word[b]
                fappend.write(word+tab + head + tab + a +tab+ tail + '\n')
            


