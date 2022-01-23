# python中运算符
# 标准运算符：+、-、*、/、//（整除）;取余运算符：%、幂运算符:**
print(1 / 2)  # 除法运算

print(11 // 2)  # 整除
print(-9 / -4)
print(9 // -4)  # 结果为-3
print(-9 // 4)  # 结果为-3因为一正一负的整除公式向下取整

print(2 ** 2)  # 幂运算

print(9 % 4)
print(9 % -4)  # 结果为-3   9-（-4）*（-3） 9-12=-3
print(-9 % 4)  # 结果为3    -9-4*（-3）即-9+12=3
# 赋值运算符 运算顺序从左到右
a = b = c = 20  # 链式赋值
print((a, id(a)))
print((b, id(b)))
print((c, id(c)))
# 参数赋值
a += 30
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 3
print(a)
print(type(a))  # float类型
a //= 2
print(a)
a %= 3
print(a)
# 解包赋值
a, b, c = 20, 30, 40
print(a, b, c)
# a,b=20,30,40  报错，因为左右变量个数和值的个数不对应
# 交换两个变量的值
a, b = 10, 20
print("交换之前", a, b)
a, b = b, a
print("交换之后", a, b)
# 逻辑运算符
print("a>b吗？", a > b)  # False逻辑运算符：>、<、<=、>=、==、!=
a = 10
b = 10
print(a == b)
print(a is b)  # is与=相同
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)  # True比较的是value值
print(list1 is list2)  # False比较的是id值
# 布尔运算符：and、or、not、in
s = "helloworld"
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
# 位运算符
print(4&8)  # 0100与1000按位与，结果为0000
print(4|8)  # 0100与1000按位或，结果为1100（12）
print(4<<1)  # 向左移动一位 00000100->00001000(8）
print(4<<2)  # 向左移动两位 00000100->00010000(16)

print(4>>1)  # 向右移动一位 00000100->00000010(2）
print(4>>2)  # 向右移动两位 00000100->00000001(1）
# 顺序结构
print('-------------程序开始---------------')
print('1,把冰箱门打开')
print('2,把大象放在冰箱里')
print('3,把冰箱门关上')
print('-----------程序结束-----------------')
# 测试对象的布尔值
print('---------以下对象布尔值均为False------')
print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(None))  # False
print(bool(''))  # False
print(bool(""))  # False
print(bool([]))  # False 空列表
print(bool(list()))  # False 空列表
print(bool(()))  # False 空元组
print(bool(tuple()))  # False 空元组
print(bool(dict()))  # False 空字典
print(bool(set()))  # False 空集合

print('---------其他对象布尔值均为True------')
print(bool(18))
print(bool(True))
print(bool('Hello world'))

# 选择结构
  # 单分支结构
money=1000  # 余额
s=int(input('请输入取款金额'))  # 取款金额
# 判断余额是否充足
if money>=s:
    money=money-s
    print('取款成功，余额为：',money)
  # 双分支结构
num=int(input('请输入一个整数'))

# 条件判断
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')

  # 多分支结构
score=int(input('请输入一个成绩：'))
# 判断
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不在成绩的有效范围')
# 分支嵌套
answer=input('您是会员吗？y/n')
money =float(input('请输入您的购物金额：'))
# 外层判断是否是会员
if answer=='y':  # 会员
    if money>=200:
        print('打8折付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)
else:  # 非会员
    if money>=200:
        print('打9.5折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)

# 条件表达式
num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))
# 比较大小
if num_a>num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)

print('使用条件表达式进行比较')
print(  str(num_a)+'大于等于'+str(num_b)   if num_a>=num_b else  str(num_a)+'小于'+str(num_b)   )

# range函数
# 第一种创建方式
r=range(10)  # [0,1,2,3,4,5,6,7,8,9],默认从0开始，默认相差1位步长
print(r)  # range(0,10)
print(list(r))  # 用于查看range对象中的整数序列
# 第二种创建方式
r = range(1,10)  # 指定了起始值，从1开始，到10结束（不包含10），默认步长为1
print(list(r))  # [1,2,3,4,5,6,7,8,9]

# 第三种创建方式
r=range(1,10,2)
print(list(r))  # [1,3,5,7,9]

#  判断指定的整数在序列中是否存在 in ，not in
print(10 in r)  # False ,10不在当前的r这个整数序列中
print(9 in r)  # True，9在当前的r这个整数序列中

print(10 not in r)  # False
print(9 not in r)  # True

print(range(1,20,1))  # [1,...19]
print(range(1,101,1))  # [1,.....100]

# 循环结构
a=1
# 判断条件表达式
while a<10:
    #执行条件执行体
     print(a)
     a+=1
# 条件判断
b=0
sum1=0
while b<5:
    sum1+=b
    b+=1
    print('和为',sum1)

# for循环
for item in 'Python':
    print(item)

# range() 产生一个整数序列，--》也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为"_"
for _ in range(5):
    print('人生苦短，我用Python')
print('使用for循环，计算1到100之间的偶数和')
sum=0
for item in range(1,101):
    if item %2==0:
        sum+=item

print('1到100之间的偶数和为:',sum)

# 输出100到999之间的水仙花数
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    # print(ge,shi,bai)
    # 判断
    if ge**3+shi**3+bai**3==item:
        print(item)

# break语句
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

# continue语句

for item in range(1,5):
    if item%5!=0:
        continue
    print(item)

# else语句

a=0
while a<3:
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
        # 改变变量
    a+=1
else:
    print('对不起，三次密码均输入错误')

# 嵌套循环
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')
    print()
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()

# 流程控制语句中break与continue在二重循环中的使用
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()

# 列表
a=10
lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)

# 创建列表的第二种方式，使用内置函数list（）

lst2=list(['hello','world',98])

# 列表的查询

lst=['hello','world',98,'hello']
print(lst,index('hello'))
print(lst,index('hello',1,4))
lst=['hello','']














