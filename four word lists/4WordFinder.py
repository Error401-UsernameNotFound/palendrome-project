#find forward words with reverced tails
#find bacward words with reverced heads
from customDatabase import DataBace

databace = DataBace({})

ogListfile = open('forwardheadTail.txt','r')
ogList = ogListfile.readlines()

newList = []
newOg = []
for row in ogList:
    #rn the oglist is for, rev, head
    line = row.split(';')
    try:
        line.remove('\n')
    except:
        line[2] = line[2].replace('\n','')
        pass
    if line[0] != line[1]:
        if len(line) > 2:
            newOg.append(line.copy())
        #new line is for, rev , head ,rev head,rev for
        try:
            line.append(''.join(reversed(line[2]))) #joined reverced head
        except:
            pass
        line.append(''.join(reversed(line[0]))) #joined reverced forward
        newList.append(line)
for i in list(newList):
    if len(i) == 3:
        newList.remove(i)
#both og list and new list have been formed
databace.updateDataset('ogList',newOg)
databace.updateDataset('newList',newList)
databace.merge('ogList',2,'newList',3,'joinedList')
databace.mergeDataProcesser('mergetmp.txt','4 word.txt')
