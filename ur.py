#coding:utf-8
import math

def quadratic_equation(a,b,c):
    t = math.sqrt(b*b-4*a*c)
    return (-b+t)/2*a , (-b-t)/2*a
print (quadratic_equation(2,3,0))
print (quadratic_equation(1,-6,5))

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print (fact(10))

# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到b柱子上面去
def move(n, a, b, c):
# 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:
        print (a, '-->', c)
        returnb)
# 输出最下面个盘子移从a移到c的路径
# 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    move(n-1, a, c,
    print (a, '-->', c)
# 将b柱子上面的n-1个盘子移动到c柱子上面
    move(n-1, b, a, c)

move(2, 'A柱', 'B柱', 'C柱')