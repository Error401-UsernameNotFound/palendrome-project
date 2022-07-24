with open("reverced.txt", "r") as rev:
    sortedrev = rev.readlines()
    sortedrev.sort()
    f = open("sortedReverced.txt", "w")
    f.writelines(sortedrev)