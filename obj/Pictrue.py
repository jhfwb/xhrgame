# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2021/11/17 30:07
# @Author  : xhr
# @FileName: Pictrue.py
class Dot:
    def __init__(self, x, y, sign=None):
        self.site = (x, y)
        if sign is None:
            self.__sign = str(self.site)
        else:
            self.__sign = sign
        self.size = len(self.__sign)

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, a):
        self.size=len(a)
        self.__sign=a

    def __str__(self):
        return str(self.__sign)
        # return str(' * ')


class Picture:
    def __init__(self, x=100, y=100, sign=None):
        self.x = x
        self.y = y
        self.arr = []
        for j in range(x):
            for i in range(y):
                self.arr.append(Dot(i, j,sign=sign))
        self.arr.reverse()

    def get_dot(self, x, y):
        return self.arr[len(self.arr)-(self.x*y+x+1)]

    def show(self, l=-1):
        s = []
        for i in self.arr:

            if i.site[0] == 0:
                s.append(i)
                s.reverse()
                for ss in s:
                    cc=ss.sign
                    if ss.size<=l:
                       cc=ss.sign+' '*(l-ss.size)
                    else:
                        raise ValueError('长度不够:只有'+str(l)+',这将导致输出异常。至少要大于等于'+str(ss.size))
                    print(cc, end='')
                s = []
                print()
            else:
                s.append(i)


if __name__ == '__main__':
    print((80, 10))
    p=Picture(x=20,y=160,sign='*')

    # p.get_dot(0, 0).sign = '*'
    # p.get_dot(60, 60).sign = '*'
    p.show(l=1)
