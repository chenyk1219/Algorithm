# 判断变位词
def anagram1(str1, str2):
    list1 = list(str1)
    list2 = list(str2)

    list1.sort()
    list2.sort()

    is_match = True
    for i in range(len(str1)):
        if list1[i] != list2[i]:
            is_match = False

    print(is_match)


def anagram2(str1, str2):
    list1 = [0] * 26
    list2 = [0] * 26

    for i in str1:
        pos = ord(str(i)) - ord('a')
        list1[pos] += 1

    for i in str2:
        pos = ord(str(i)) - ord('a')
        list2[pos] += 1

    is_match = True
    for i in range(26):
        if list1[i] != list2[i]:
            is_match = False

    print(is_match)


def anagram3(str1, str2):
    dict1 = {}
    dict2 = {}

    for i in str1:
        dict1[str(i)] = dict1[str(i)] + 1 if str(i) in dict1.keys() else 1

    for i in str2:
        dict2[str(i)] = dict2[str(i)] + 1 if str(i) in dict2.keys() else 1

    is_match = True
    for key, value in dict1.items():
        if dict2[key] != value:
            is_match = False
    print(is_match)


a = "qwee"
b = "eweq"
anagram1(a, b)
anagram2(a, b)
anagram3(a, b)
