#the inverter
with open("dictionary.txt", "r") as dic:
    allwords = dic.readlines()
    new = open("reverced.txt", "w")
    for word in allwords:
        word.replace("\n","")
        nw = reversed(word)
        empty = ""
        new.write(empty.join(nw))