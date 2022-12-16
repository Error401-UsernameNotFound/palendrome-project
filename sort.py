with open("7long4.txt", "r") as rev:
    sortedrev = rev.readlines()
    tobeSorted = []
    for i in sortedrev:
        split1 = i.split('; ')
        tobeSorted.append([int(split1[0]),split1[1]])
    tobeSorted.sort(reverse=True)
    f = open("Long7SortedAsFour.txt", "w")
    sortedCombined = []
    for i in tobeSorted:
        sortedCombined.append(str(i[0])+'; '+i[1])
    f.writelines(''.join(sortedCombined))