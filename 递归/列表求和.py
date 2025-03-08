def listsum(sl):
    if len(sl) == 1:
        return sl[0]
    else:
        return sl[0] + listsum(sl[1:])


a = [1, 3, 5, 7, 9]
print(listsum(a))
