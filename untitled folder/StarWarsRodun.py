amount = int(input())

myList = list(map(int, input().split()))

def starWarsOrder(flist):
    flist.sort()
    third = len(flist) // 3
    
    first = flist[:third]
    middle = flist[third:third*2]
    last = flist[third*2:]

    nList = middle + first + last

    return nList

newList = starWarsOrder(myList)

print(" ".join(map(str, newList)))