# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2021/11/17 30:07
# @Author  : xhr
# @FileName: Pictrue.py
class Dot:
    def __init__(self,x,y,sign='*'):
        self.site= (x,y)

    def __str__(self):
        return str(self.site)
class Picture:
    def __init__(self,x=100,y=100):
        self.x=x
        self.y=y
        self.arr=[]
        for j in range(x):
            for i in range(y):
                self.arr.append(Dot(i, j))
        self.arr.reverse()

    def show(self):
        s = []
        for i in self.arr:
            # print(i, end='')
            if i.site[0] ==0:
                s.append(i)
                s.reverse()
                for ss in s:
                    print(ss, end='')
                s = []
                print()
            else:
                s.append(i)





if __name__ == '__main__':
    Picture().show()
