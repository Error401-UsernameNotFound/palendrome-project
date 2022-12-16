#use fixed fixed reversed + palendrome list to make many many 3 word palendromes
f = open('3word.txt','w')
f.close()
nf = open('3word.txt','a')
pals = open("palendromes.txt", 'r')
rev = open("fixed fixed reversed.txt", 'r')
palsTxt = pals.readlines()
revTxt = rev.readlines()


tab = ';'
for i in revTxt:
    split = i.removesuffix('\n').split('\t')
    combined = []
    for a in palsTxt: #creates some but not all. uses rev words and a palendrome. 
        a = a.removesuffix('\n')
        if len(a) > 3 and len(split[0]) >3 and len(split[1]):
            combined.append(split[0]+ tab + a + tab + split[1] + '\n')
            #combined.append(split[1]+ tab + a + tab + split[0] + '\n')
    nf.writelines(combined)

#now we make one using heads and tails

