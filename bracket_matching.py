# 括号匹配
from stack import Stack


def bracket_matching(str1):
    s = Stack()
    is_match = True
    index = 0
    while index < len(str1) and is_match:
        symbol = str1[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                is_match = False
            else:
                l = s.pop()
                if not matches(l, symbol):
                    is_match = False
        index += 1

    if s.isEmpty() and is_match:
        exit("匹配成功")
    else:
        exit("匹配失败")


def matches(l, r):
    left_symbol = '({['
    right_symbol = ')}]'

    if left_symbol.index(l) == right_symbol.index(r):
        return True
    else:
        return False


bracket_matching("({}{}[)")
