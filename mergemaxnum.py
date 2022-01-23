# 用贪心算法解决数字拼接问题

from functools import cmp_to_key#将比较函数转换为关键字函数

li = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):#自定义比较函数比较x，y的大小
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):    #将数字转换成字符串
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))#sort对列表进行排序，key主要是用来进行比较的元素，只有一个参数
    return "".join(li)#在li各个元素之间，用“”连接


print(number_join(li))
