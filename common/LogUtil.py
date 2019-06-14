#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/14
import logging
import sys

logger = logging.getLogger('CarHouse-UITest')
logger.setLevel(logging.DEBUG)

# 创建一个流处理器handler并设置其日志级别为DEBUG
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# 创建一个格式器formatter并将其添加到处理器handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 为日志器logger添加上面创建的处理器handler
logger.addHandler(handler)


def loginfo(msg):
    logger.info(msg)


def logerror(msg):
    logger.error(msg)