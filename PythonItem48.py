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
blist = [89,23,33,45,10,12,45,45,45]
bubbleSort(alist)
print (alist)
bubbleSort(blist)
print (blist)


