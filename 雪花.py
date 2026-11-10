import turtle as t

# 8个瓣，循环8次
for i in range(8):
    # 干支
    t.pensize(10)
    t.color('light pink')
    t.forward(120)
    t.backward(50)
    # 小分支
    t.left(60)
    t.forward(30)
    t.backward(30)
    t.right(120)
    t.forward(30)
    t.backward(30)
    t.left(60)
    # 前进一点点
    t.forward(25)
    # 大分支
    t.left(60)
    t.forward(40)
    t.backward(40)
    t.right(120)
    t.forward(40)
    t.backward(40)
    t.left(60)
    # 回到原点
    t.backward(95)
    # 旋转到下一个花瓣
    t.left(45)

# 中心圆，不用循环
t.fillcolor('white')
t.goto(0, -20)
t.begin_fill()
t.circle(20)
t.end_fill()

# 隐藏箭头
t.hideturtle()

# 画面停留
t.done()