def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


alist = [21, 56, 89, 12, 67, 31, 34, 56, 1, 4, 3, 2]
bubbleSort(alist)
print(alist)
