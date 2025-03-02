from stack import Stack


def to2(num, base):
    digits = '0123456789ABCDE'
    s = Stack()
    while num > 0:
        rem = num % base
        s.push(rem)
        num = num // base

    res = ""
    while not s.isEmpty():
        res += digits[s.pop()]

    print(res)


to2(42, 16)
