# Author: Shelley Tennison
# Python 3.6.2


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist = [67, 45, 2, 13, 1, 998]
bubbleSort(alist)
print (alist)



def bubbleSort(blist):
    for passnum in range(len(blist)-1,0,-1):
        for i in range(passnum):
            if blist[i]>blist[i+1]:
                temp = blist[i]
                blist[i] = blist[i+1]
                blist[i+1] = temp
blist = [89,23,33,45,10,12,45,45,45]
bubbleSort(blist)
print (blist)
