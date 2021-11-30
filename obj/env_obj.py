# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2021/11/13 29:14
# @Author  : xhr
# @FileName: env_obj.py
"""
地图：
实体-形状
1.边界
2.可移动边界（不同的移动算法，）
3.内部将有实体
4.

"""
from abc import ABCMeta, abstractmethod


class Map(metaclass=ABCMeta):
    """
    1. 地图工具
    2. 可移动区域（不同的形状）
    3. 地图名称
    """
    def __init__(self, x, y, name, border_sites=[], useless_sites=[], border_func=None):
        self.x = x
        self.y = y
        self.name = name
        self.border_func = border_func
        self.border_sites = border_sites
        self.useless_sites = useless_sites

    def is_in_map(self, dots):
        """
        判断某个点是否在该函数中
        :param check_func:
        :param dots:
        :return:
        """
        if self.border_func is None:
            if dots in self.border_sites:
                return True
            else:
                return False
        return self.border_func(self, dots)



class MapFactory:
    pass