# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2021/11/11 29:06
# @Author  : xhr
# @FileName: 角色.py
"""
角色管理器。（1.创建角色 2.通知所有角色执行某行为 3.内部有个集合存放着所有角色 4.销毁角色 5.暂存角色）
    角色创建系统 （不管下面工厂是啥，都能够管理下面工厂）
        玩家创建工厂
        怪物创建工厂
        Npc创建工厂
        ...
    角色维护系统（执行所有角色中的特定方法，更新所有角色中的状态）
        玩家管理器
        怪物管理器
        Npc管理器
        ...
角色（视野。field:blood_max, name, blood_current, quick, defence ; func:die(), move(), attack() )（插槽脚本：附属物们 用于扩展新特性）
    玩家 ...(后续可能产生新属性或者新方法)
    怪物
    NPC
    宠物
    ...（后续可能存在新特性）

附属物：(隶属于角色)
    装备：
        武器
        衣服
        ...
"""
from abc import ABCMeta, abstractmethod


class Belonging(metaclass=ABCMeta):
    @abstractmethod
    def plug(self, role):
        pass


class EquipmentSite(Belonging):
    def __init__(self):
        self.__clothes = None
        self.__weapon = None
        self.__weapon_2 = None
        self.__pants = None
        self.__cap = None
        self.__arms = None
        self.role = None

    @property
    def clothes(self):
        return self.__clothes

    @clothes.setter
    def clothes(self, clothes):
        # 类型检测
        self.__clothes.unload(self.role)
        self.__clothes = clothes
        self.__clothes.load(self.role)

    def plug(self, role):
        self.role = role
        role.equipment = self
        # 装备逻辑


class Equipment(metaclass=ABCMeta):
    # 1.增加数值 2.改变战斗方式
    @abstractmethod
    def unload(self, role):
        pass

    @abstractmethod
    def load(self, role):
        pass


class Clothes(Equipment):
    def __init__(self, name=None, quality=None, attribute=None):
        self.name = name
        self.quality = quality
        self.attribute = attribute

    def unload(self, role):
        role.attribute -= self.attribute

    def load(self, role):
        role.attribute += self.attribute


class Attribute:
    def __init__(self, att=None, defence=None, quick=None, blood_max=None):
        self.__blood_max = blood_max
        self.__blood_current = self.__blood_max
        self.__quick = quick
        self.__att = att
        self.__defence = defence

    def add_attribute(self, attribute):
        if self.__blood_max is not None and attribute.__blood_max is not None:
            self.__blood_max += attribute.__blood_max
        if self.__blood_current is not None and attribute.__blood_current is not None:
            self.__blood_current += attribute.__blood_current
        if self.__blood_current is not None and attribute.__blood_current is not None:
            self.__quick += attribute.__blood_current
        if self.__defence is not None and attribute.__defence is not None:
            self.__defence += attribute.__defence
        if self.__att is not None and attribute.__att is not None:
            self.__att += attribute.__att

    def red_attribute(self, attribute):
        if self.__blood_max is not None and attribute.__blood_max is not None:
            self.__blood_max -= attribute.__blood_max
        if self.__blood_current is not None and attribute.__blood_current is not None:
            self.__blood_current -= attribute.__blood_current
        if self.__blood_current is not None and attribute.__blood_current is not None:
            self.__quick -= attribute.__blood_current
        if self.__defence is not None and attribute.__defence is not None:
            self.__defence -= attribute.__defence
        if self.__att is not None and attribute.__att is not None:
            self.__att -= attribute.__att

    @property
    def quick(self):
        return self.__quick

    @quick.setter
    def quick(self, data):
        return self.__quick

    @property
    def blood_current(self):
        return self.__blood_current

    @blood_current.setter
    def blood_current(self, data):
        self.__blood_current = data
        if data <= 0:
            pass
            # self.die()
        return data


class Role(metaclass=ABCMeta):
    def __init__(self, name=None, attribute=None, belongings=[]):
        self.attribute = attribute
        self.belongings = belongings
        self.name=  name
        # 开启扩展属性
        self.socket()

    def socket(self):
        for belonging in self.belongings:
            belonging.plug(self)

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def die(self):
        pass


class ZeroRole(Role, metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def attack(self, weapon):
        pass

    def move(self):
        pass

    def die(self):
        pass


if __name__ == '__main__':
    SuperMan().attack()
