print("************第一题*****************")
n=input("请输入自然数的数字:")
s=0
for c in n:
    s+=int(c)
print("各位数字之和",s)

print("\n第二题***************")
a=set(map(int,input("输入集合A:").split(',')))
b=set(map(int,input("输入集合B:").split(',')))
jiaoji =a&b
bingji =a|b
chaji1=a-b
chaji2=b-a
print("交集：",jiaoji)
print("交集：",bingji)
print("交集：",chaji1)
print("交集：",chaji2)

print("\n第三题***************")
lst=list(map(float,input("输入列表，数字用逗号隔开").split(',')))
lst_sorted=sorted(lst)
max_val=max(lst)
avg=sum(lst)/len(lst)
print("排序后的列表：",lst_sorted)
print("最大值：",max_val)
print("均值：",avg)


