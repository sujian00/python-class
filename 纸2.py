name = ( " 传智播客 " )
stock_code= 19.19
stock_price= " 003032 "
stock_price_daily_growth_factor= 1.2
growth_day= 7
finally_prince= stock_code*stock_price_daily_growth_factor**growth_day
print(f"公司；{name},股票价格；{stock_code},股票代码：{stock_code}")
print( "每日增长系数；%1.f.经过%d天增长后，股价达到了；%2.f "%(stock_price_daily_growth_factor,growth_day,finally_prince))
#练习二
#比较运算符的应用

#==,相等，  ！=不等  ，>= 大于等于    <=小于等于

num1 = 10
num2 = 10
print ( f"10==10的结果是;{num1==num2}")
print ( f"10!=10的结果是；{num1!=num2}")
num3=20
num4=30
print(f"20=30的结果;{num3==num4}")
print(f"20<=30的结果是；{num3<=num4}")
#练习三
print("欢迎来到动植物游乐公园。儿童免费，成人需要门票钱")
age =int(input("请输入你的年龄:"))
if age >=18:
    print("您已经成年了，游玩请输入20元钱作为门票")
else:
    print("您未成年，不需要门票，可以免费游玩")
height=int(input('请您输入您的身高（cm）'))
if height >= 110:
    print("您的身高已满足110cm及以上，请缴费30元")
else:
    print('您的身高未满足110cm，您可以免费游玩')
print("祝您游玩愉快")




