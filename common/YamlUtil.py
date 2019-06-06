#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/5/24
from yaml import load, load_all, dump, dump_all, FullLoader
import os


def get_detail_yaml(page, element=None):
    config = os.path.abspath('.\\source\\detail.yaml')
    y1 = load_yaml(config)
    if element is not None:
        if page == '环境':
            return y1[page]
        return y1[page][element]
    else:
        return y1[page]


def load_yaml(path):
    """
    :param path: 输入yaml路径
    :return: 返回字典类型数据
    """
    try:
        with open(path, encoding='utf-8', errors='ignore') as f:
            conf = f.read()
        return load(conf, Loader=FullLoader)
    except Exception as e:
        print(e)
        return None
