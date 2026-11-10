from tkinter.font import names

money=50
print('当前红包余额；',money)
money=10
print('购买冰激淋；',money)
money=10
print('购买了可乐；',money)
money=30
print('最终，钱包还剩下；',money,'元')
#整数浮点数和字符串
print(type('黑马程序员'))
print(type(12))
print(type(12.3))
num_float=str(11.5)
print(type(num_float))
num_str=int("11")
print(type(num_str))
#
name="小橘"
print("我的名字是:"+ name +"，我可以教大家IT技能")
#字符串字面量之间的拼接
print("学IT"+"月薪百万")
#字符串字面量和字符串之间的拼接，“ + ” 不可以将数字占位但是下面的%s可以
name="小橘"
address="江西省赣州市客家大道156号"
print("我的名字是；"+name+"我的家庭住址是；" + address  )
#  %s 1.% 表示 ；我要占位  2.s 表示将变量变成字符串放在占位的地方   3.综合起来的意思是；我先占一个位置，等一会有一个变量过来，我想把它放在这里
name="黑马程序员"
message = "学IT就来 %s "% name
print(message)
class_num=57
avg_salary=16781
message = "Python大数据，北京%s期，毕业平均工资；%s" %(class_num , avg_salary)
print(message)
name1='传智播客'
stock_price=19.19
stock_code='003032'
stock_price_daily_growth_factor=1.2
growth_days=7
add=(f"公司；{name1},股票代码；{stock_code}，当前股价{stock_price}")
print(add+"每日增长系数；%1.f.经过%d天增长后，股价达到了；%2.f " %(stock_price_daily_growth_factor,growth_days,19.99*1.2**7))
user_name=input("请输入您的名字")
print("您好",user_name)
user_type=input("请输入您的vip等级")
print(user_type)
print("您是尊贵的SSSVIP用户，欢迎您的光临")
num1=1+1
num2=2+5
print("1+1=",num1==num2)

