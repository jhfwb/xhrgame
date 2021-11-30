# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2021/11/07 30:52
# @Author  : xhr
# @FileName: Shape.py
"""
图形设置：
1. 点 (颜色)
2. 线段
3. 形状
4. 立体图形

"""
import math
from abc import ABCMeta, abstractmethod


class ShapeMaker:
    pass


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def function(self):
        pass


class CircleShape(Shape):
    def __init__(self, certain=(0, 0), r=1):
        self.__o = certain
        self.__r = r
        self.shape = None

    def func(self, site):
        if math.pow(site[0], 2)+math.pow(site[1], 2) == self.__r:
            return True
        return False

    def search_func(self):
        pass

    def create(self):
        base_dot = (self.__o[0], self.__o[1]+self.__r)  # 基点:用于开始图形的绘制
        self.shape = Dot(site=base_dot)
        while True:
            self.func(base_dot)


class ShapeDot(metaclass=ABCMeta):
    @abstractmethod
    def next(self):
        pass


class Dot(ShapeDot):
    def __init__(self, site, next_dot=None):
        self.value = site
        self.__next = next_dot

    def __str__(self):
        return self.value

    def add_next_dot(self, shape_dot):
        self.__next = shape_dot

    def next(self):
        return self.__next

