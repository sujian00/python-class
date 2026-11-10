# 1. 构建一个随机变量
import random
from mimetypes import guess_type

num=random.randint(1,10)
guess_num=int(input("输入你要猜测的数字"))
if guess_num==num:
     print("恭喜第一次就猜中了")
else:
    if  guess_num>num:
        print("你猜测的数字大了")
    else :
        print("你猜测的数字小了")

    guess_num = int(input("再次输入你要猜测的数字"))
    if guess_num == num:
        print("恭喜第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("再次输入你要猜测的数字"))
        if guess_num == num:
            print("恭喜第三次猜中了")
        else:
            if guess_num > num:
                print("你猜测的数字大了")
            elif guess_num < num:
                print("你猜测的数字小了")

                print("三次机会就没了，没有猜中。")
