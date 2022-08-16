seven = open('7Word.txt','r')
slines = seven.readlines()
longestLine = ''
longestnum = 999999999
for i in slines:
    i2 = i.removesuffix('\n')
    if len(i2) <= longestnum:
        longestLine = i2
        longestnum = len(i2)
print(longestLine.lower(),longestnum)