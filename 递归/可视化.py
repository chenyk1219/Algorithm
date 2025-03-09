import turtle


def wjx():
    t = turtle.Turtle()
    t.pencolor('red')
    t.pensize(3)
    for i in range(5):
        t.forward(100)
        t.right(144)

    t.hideturtle()


def ds(t, linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        ds(t, linelen - 5)


def tree(branch_len):

    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)


# ds(t, 100)
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done()
