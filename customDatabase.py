#stealing some stuff from my wordle project (better lists)
#the whole point of this is to preform a merge between 2 lists

#matchching merge logic
#peramaters l1Name l1Collem l2Name l2Collem


class DataBace:
    def __init__(self,alldata:dict[str:list]) -> None:
        self.alldata = alldata
    def updateDataset(self,Name:str,data:list) -> None:
        self.alldata.update({Name:data}) 
    def DataGraber(self,Name:str) -> list:
        return self.alldata[Name]
    def SortByCollom(self,Name:str, collom:int):
        data:list[list] = self.alldata[Name].copy()
        #data is a list of lists
        TempList =[]
        sortedList = []
        for row in data:
            TempList.append(';'.join([row.pop(collom)]+row))
        TempList.sort()
        for row in TempList:
            expanded = row.split(';')
            sortedList.append(expanded)
        return sortedList
    def mergeDataProcesser(self,fileName:str,NewFileName:str):
        file = open(fileName,'r')
        fileLines = file.readlines()
        f = open(NewFileName, 'w')
        for i in fileLines:
            i = i.replace('\n','')
            iList = i.split(';')

            #orginised the other way
            palendromeList = [iList[3],''.join(reversed(iList[2])),iList[0],''.join(reversed(iList[4]))]
            txt = ', '.join(palendromeList) + '; '+ ' '.join(palendromeList)
            nf = open(NewFileName, 'a')
            nf.write(txt+'\n')



    def merge(self,L1Name:str,L1Collom:int,L2Name:str,L2Collom:int,NewListName:str) -> None:
        list1 = self.SortByCollom(L1Name,L1Collom)
        list2 = self.SortByCollom(L2Name,L2Collom)
        #head, for, rev
        #rev head, for, rev ,head, rev for,



        #goal:
        #for, rev,rev,for other, rev rev other

        #assuming the lists are already seperated into internal lists
        list1Row = 0
        list2Row = 0

        list1Dict = {}
        list2Dict = {}

        Pword1 = ''
        Pword2 = ''
        print('starting merge')
        go = True
        f = open('mergetmp.txt', 'w')
        while go:
            #compare words in same was as head tail finder find matches
            word1 = list1[list1Row][0]
            word2 = list2[list2Row][0]
            row1 = list1[list1Row]
            row2 = list2[list2Row]
            
            if word1 == word2:
                if word1 != Pword1 and len(word1) > 1:
                    list1Dict.update({row1[1]:row1})
                if word2 != Pword2 and len(word2) > 1:
                    list2Dict.update({row2[1]:row2})
            else:
                for one in list1Dict.keys():
                    for two in list2Dict.keys():
                        w1 = list1Dict[one]
                        w2 = list2Dict[two]
                        print(w1[0],w2[0])
                        f = open('mergetmp.txt','a')
                        f.write(';'.join([w1[1],w1[2],''.join(reversed(w1[2])),w2[1],''.join(reversed(w2[2]))]) + '\n')
                list1Dict.clear()
                list2Dict.clear()

            if word1 > word2:
                list2Row += 1
            elif word1 < word2:
                list1Row += 1
            else:
                if list1[list1Row+1] > list2[list2Row+1]:
                    list2Row += 1
                elif list1[list1Row+1] < list2[list2Row+1]:
                    list1Row += 1
                else:
                    list1Row += 1
                    list2Row += 1
            if list1Row >= len(list1) or list2Row >= len(list2):
                go = False