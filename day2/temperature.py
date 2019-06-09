#! /user/local/bin/env python3
#coding:utf-8
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""
import math

#
#温度转换
#
def transTemp(temp):
    if 'C' in temp:
        temperature = 1.8 * eval(temp[:-1]) + 32
    elif 'F' in temp:
        temperature = (eval(temp[:-1]) - 32) / 1.8
    else:
        print('输入参数格式错误！')
        return 0
    print("华氏温度是 %f" % temperature)

# 计算圆的面积

def circle(r):
    if r <= 0:
        print('输入参数格式错误,半径必须大于0！')
        return 0
    else:
        area = math.pi * r * r
        circle_long = 2 * math.pi * r
        print('面积是 %f ,周长是 %f' % (area, circle_long))
 

def guessNum(num):
    flag = True
    countor = 0
    while flag:
        guess = input('guess a int!')
        if num > guess:
            print('太小')
        elif num < guess:
            print('太大')
        else:
            print('对了')
            flag = False
        countor += 1
    if countor > 7:
           print('you guess %d times : you definatily too weak' % countor)
    else:
        print('cool!')

def calendar99():
    for x in range(1,10):
        for y in range(1,10):
            if x >= y:
                print('{} x {} = {}'.format(x,y,x*y),end = ' ')
        print()
"""
打印各种三角形图案,注意python中自己实现的思路

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

def trangle(num):
    for x in range(0,num):
        for y in range(0,num):
            if x >= y:
                print("*" * x)
                break

    for x in range(num,0,-1):
       for y in range(0,num):
            if x >= y:
                print(" " * x + (num - x) * "*")
                break

    for x in range(1,num):
        if num >= 2*x - 1:
            print(  (num - ( 2*x - 1))//2 * ' ' + (2*x - 1) * '*' + (num -( 2*x - 1))//2  * ' ')


def tranglev2(num):
    # 一行行的输出
    for x in range(1,num):
        for _ in range(1,x):
            print("*",end=' ')
        print()
    # 一行行的输出，这种思路比上面的要好很多
    for x in range(1,num):
        for y in range(1,num):
            if  y <= num - x - 1:
                print(" ",end=' ')
            else:
                print("*",end=' ')
        print()
        # 纯粹一行一行的输出，这种方式简单容易理解
    for i in range(num):
        for _ in range(num - i - 1):
            print('-', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()
#
#
# # 计算水仙花数
# # 1^3 + 5^3+ 3^3 = 153
# def fleeper(num):
#     leng = len(str(num))
#     length = leng
#     sum = 0
#     while count:
#         sum += ( num//10  % 10 ) ** length
#         count =
#     else:
#
# if __name__ == '__main__':
#     # temperature = input('请输入温度值：')
#
#     # transTemp(temperature)
#     tranglev2(10)