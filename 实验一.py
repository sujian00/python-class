x=input("请输入一个三位自然数：")
if x.isdigit() and len(x)==3:
    n=int(x)
    a=n//100
    b=(n%100)//10
    c=n%10
    num=a+b+c;
    print("个位:",c)
    print("十位:",b)
    print("百位:",a)

    print("按位相加=",num)

else:
    print("输入的三位数出现错误")

