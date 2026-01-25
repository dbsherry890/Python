def uniqueOccurrences(arr) -> bool:
    mydict = {}
    for i in arr:
        if i in mydict:
            mydict[i] += 1
        if i not in mydict:
            mydict[i] = 1
    return print(len(mydict.values()) == len(set(mydict.values())))


print(uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
# should be true
