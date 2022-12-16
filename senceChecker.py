import csv

ForWordFile = open('tmore3s.txt','r')
forWordList = ForWordFile.readlines()
f = open('3wordSence.txt','w')
wordPopularity = open('wordPopularity.csv','r')
reader = csv.reader(wordPopularity)
wordDict = {rows[0]:rows[1] for rows in reader}

for i in forWordList:
    i = i.replace('\n','')
    split1 = i.split(': ')[0].split(';')
    numbers = []
    minNum = 0
    for a in split1:
        try:
           numbers += [int(wordDict[a.lower()])]
        except:
            numbers += [0]
        try:
            minNum = min(numbers)
        except:
            minNum = 0
    file = open('3wordSence.txt','a')
    file.write(str(minNum)+ '; '+ ' '.join(split1)+'\n')