#nest 3 word inside of 4 word
T3WordFile = open('3wordSence.txt', 'r')
F4WordFile = open("senceMaker.txt" , 'r')
T3Word = T3WordFile.readlines()
F4Word = F4WordFile.readlines()

f = open("7Word.txt",'w')
f.close()
nf = open("7word.txt",'a')
#split the number from the palendrome
tab = ' '
for i in F4Word:
    Fsplit1 = i.removesuffix('\n').split('; ')
    combined = []
    if int(Fsplit1[0]) >= 1127729: #this number to get the most intrtsting one
        for a in T3Word:
            Tsplit1 = a.removesuffix('\n').split('; ')
            if int(Tsplit1[0]) >= 1000000:
                Fsplit2 = Fsplit1[1].split(' ')
                combined.append(Fsplit2[0] + tab + Fsplit2[1] + tab + Tsplit1[1] + tab + Fsplit2[2] + tab + Fsplit2[3] + '\n')
    nf.writelines(combined)
