def searchBinary(alist, item):
    frist = 0
    laster = len(alist) + 1
    found = False

    while frist < laster and not found:
        pos = (frist + laster) // 2
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] < item:
                frist = pos + 1
            else:
                laster = pos - 1

    return found


def searchBinary2(alist, iterm):
    if len(alist) == 0:
        return False
    else:
        pos = len(alist) // 2
        if alist[pos] == iterm:
            return True
        else:
            if alist[pos] > iterm:
                return searchBinary2(alist[:pos], iterm)
            else:
                return searchBinary2(alist[pos+1:], iterm)


a = [1, 3, 5, 7, 9, 11, 14, 16, 18, 21]
print(searchBinary2(a, 15))
