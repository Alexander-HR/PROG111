amount = int(input())
myList = [str(input().split(" ",amount))]

def starWarsOrder(flist,fnum):
    
    flist.sort()
    num = fnum // 3

    flist1 = flist[:num]
    flist2 = flist[num:(num * 2)]
    flist3 = flist[(num * 2):]

    flist4 = flist2 + flist1 + flist3

    return flist4

newList = starWarsOrder(myList,amount)

my_string = " ".join(newList)

print(my_string)