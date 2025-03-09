import sys

sys.getrecursionlimit()
sys.setrecursionlimit(300)


def jzzh(base, num):
    cs = "0123456789ABCDEF"
    if num < base:
        return cs[num]
    else:
        return jzzh(base, num // base) + cs[num % base]


print(jzzh(2, 1 << 21))
