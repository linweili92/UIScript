#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/5/24


def init():
    """
    定义全局变量
    :return:
    """
    global gl_dict
    gl_dict = {}


def set_value(key, value):
    """
    赋值
    :param key:
    :param value:
    :return:
    """
    gl_dict[key] = value


def get_value(key):
    """
    正常返回对应value值，异常返回None
    :param key:
    :return:
    """
    try:
        return gl_dict[key]
    except Exception as e:
        print(e)
        return None
