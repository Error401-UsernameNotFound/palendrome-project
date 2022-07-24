#check all reverce words to make sure they are real words

with open("sortedreverced.txt", "r") as rev:
    dic = open("dictionary.txt", "r")
    diclist = dic.readlines()
    revlist = rev.readlines()

    GBP:int = 0 #go back point
    for check in diclist:
        check = check.replace("\n","")
        go = True
        count = 0
        #print(check)
        while go:
            revword = revlist[count+GBP].replace("\n","")
            if revword == check:
                GBP += count
                fixed = open("fixed reverced.txt",'a')
                fixed.write(check+"\n")
                go = False
                print('found',check)
            if count+GBP > len(revlist) or check < revword:
                go = False
                print('passed in alphabet',check,revword)
            count +=1