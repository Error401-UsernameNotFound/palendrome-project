import csv

ForWordFile = open('4 word.txt','r')
forWordList = ForWordFile.readlines()
f = open('senceMaker.txt','w')
wordPopularity = open('wordPopularity.csv','r')
reader = csv.reader(wordPopularity)
wordDict = {rows[0]:rows[1] for rows in reader}

for i in forWordList:
    i = i.replace('\n','')
    split1 = i.split('; ')
    split2 = split1[1].split(' ')
    numbers = []
    minNum = 0
    for a in split2:
        try:
           numbers += [int(wordDict[a.lower()])]
        except:
            numbers += [0]
        try:
            minNum = min(numbers)
        except:
            minNum = 0
    file = open('senceMaker.txt','a')
    file.write(str(minNum)+ '; '+ ' '.join(split2)+'\n')