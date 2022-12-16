seven = open('7Word.txt','r')

slines = seven.readlines()
long3 = open("7long4.txt",'a')
for i in slines:
    i2 = i.removesuffix('\n')
    #i3 = ' '.join(i2.split(": ")[0].split(";"))
    i4 = i2.split(' ')
    i5 = ' '.join([i4[0],i4[1],i4[5],i4[4]])
    long3.write(str(len(i5))+"; "+i2+'\n')