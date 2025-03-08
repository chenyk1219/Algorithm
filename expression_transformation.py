from stack import Stack


def expression_transformation(expressions: str):
    prex = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }
    tokens = expressions.split()
    s = Stack()
    result = []
    for token in tokens:
        if token.isalnum() or token.isalpha():
            result.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            t = s.pop()
            while t != '(':
                result.append(t)
                t = s.pop()
        else:
            while (not s.isEmpty()) and (prex[s.peek()] >= prex[token]):
                result.append(s.pop())
            s.push(token)

    while not s.isEmpty():
        result.append(s.pop())

    print(" ".join(result))


expression_transformation("A * B + C * D")

