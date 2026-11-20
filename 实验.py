print("*********实验一*********")
lstA=list(map(int,input("输入lstA，空格分开：").split()))
lstB=list(map(int,input("输入lstB，空格分开：").split()))
n=min(len(lstA),len(lstB))
dict_res={lstA[i]:lstB[i] for i in range(n)}
print("第一题结果·",dict_res)

print("***********实验二*********")
lst2=list(map(int,input("输出第（2）题整数列表，空格分隔：").split()))
desc_lst=sorted(lst2,reverse=True)
print("第(2)题结果：", desc_lst)

# (3) 列表整数连乘
print("***********实验三***********")
lst3 = list(map(int, input("输入第(3)题整数列表，空格分隔：").split()))
mul = 1
for num in lst3:
    mul *= num
print("第(3)题连乘结果：", mul)

print("********实验四********")
# (4) 曼哈顿距离
p1 = list(map(int, input("输入第(4)题第一个坐标(x y)：").split()))
p2 = list(map(int, input("输入第(4)题第二个坐标(x y)：").split()))
manhattan = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print("第(4)题曼哈顿距离：", manhattan)
