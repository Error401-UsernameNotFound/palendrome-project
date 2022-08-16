#shit to find 
#rev with heads
#rev with tails
#pal with heads done
#pal with tails done

#first step

#f = open('forwardheadTail.txt', 'r')
#flist = f.readlines()
#rev = open('fixed reverced.txt', 'r')
#revlist = rev.readlines()
#revheadtail = open('revheadtail.txt', 'a')
#for i in flist:
#    #split along ;
#    i = i.removesuffix('\n')
#    data = i.split(';')
#    #0 = full word 1 = head 2 = tail
#    if len (data[0]) > len(data[1]) and len(data[1]) > 3: #weird bug where head is massive
#        #rev head / tail
#        if revlist.count(data[1]+'\n') > 0 or revlist.count(data[2]+'\n') > 0:
#            revheadtail.write(';'.join([data[1],data[2]])+'\n')

            


#second step
#combine paltails and revhead tail



pal = open('palendromeTails.txt','r')
paltxt = pal.readlines()
rev = open('revheadtail.txt','r')
revtxt = rev.readlines()
ref = open('fixed reverced.txt', 'r')
reftxt = ref.readlines()

t = ';'
for i in revtxt:
    i = i.removesuffix('\n')
    revsplit = i.split(';')
    #find if rev is head or tail
    revhead = False #rev word location
    if reftxt.count(revsplit[0]+'\n') > 0:
        revhead = True

    for a in paltxt:
        #find if pal is head or tail
        a = a.removesuffix('\n')
        a = ''.join(reversed(a))
        palsplit = a.split('\t')
        palhead = False
        if reftxt.count(palsplit[0]+'\n') > 0:
            palhead = True
            
        if palhead and revhead: #both heads
            if revsplit[1] == ''.join(reversed(palsplit[1])):
                #if they are opisites 
                new3 = open('more3s.txt','a')
                new3.write(''.join(revsplit) + t +''.join(palsplit) + t + revsplit[0] +'\n')

        elif not palhead and not revhead: #both tails
            if revsplit[0] == ''.join(reversed(palsplit[0])):
                new3 = open('more3s.txt','a')
                new3.write(revsplit[1] + t + ''.join(palsplit) +t+ ''.join(revsplit) + '\n')
