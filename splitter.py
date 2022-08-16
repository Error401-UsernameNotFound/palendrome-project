
f = open("7Word.txt", "r")
fread = f.readlines() #this might not work
split1 = open("7wordA.txt", 'a')
split2 = open("7wordB.txt", 'a')
leng = len(fread)
for i in range(leng):
    if i < int(leng/2):
        split1.write(fread[i])
    else:
        split2.write(fread[i])