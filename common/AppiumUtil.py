#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/5/24
from selenium.webdriver.support.ui import WebDriverWait
from common.YamlUtil import get_detail_yaml
from common import GlobalVar as gl
from common.LogUtil import loginfo, logerror
import time
gl.init()


def swipeUp(driver, t=500, n=1):
    """向上滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        loginfo('向上 滑动屏幕' + str(i+1) + '次')
        driver.swipe(x1, y1, x1, y2, t)


def swipeDown(driver, t=500, n=1):
    """向下滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.25  # 起始y坐标
    y2 = l['height'] * 0.75  # 终点y坐标
    for i in range(n):
        loginfo('向下 滑动屏幕' + str(i+1) + '次')
        driver.swipe(x1, y1, x1, y2, t)


def swipLeft(driver, t=500, n=1):
    """向左滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        loginfo('向左 滑动屏幕' + str(i+1) + '次')
        driver.swipe(x1, y1, x2, y1, t)


def swipRight(driver, t=500, n=1):
    """向右滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        loginfo('向右 滑动屏幕' + str(i+1) + '次')
        driver.swipe(x1, y1, x2, y1, t)


def clickElement(driver, page, element=None):
    """
    点击元素
    :param driver:
    :param page:
    :param element:
    :return:
    """
    et = finElement(driver, page, element)
    if et is not None:
        # loginfo('点击元素')
        et.click()
    else:
        # loginfo('检查是否存在弹窗')
        logerror('未找到元素 {}'.format(et))


def finElement(driver, page, element=None):
    """
    检查元素是否存在
    :param driver:
    :param page:
    :param element:
    :return:
    """
    et = get_detail_yaml(page, element)
    # loginfo('获取到信息: ')
    # loginfo('类型: ' + et['类型'])
    # loginfo('类型: ' + et['参数'])
    if page == '环境':
        # loginfo('获取到环境类型: ' + et['类型'] + ',保留参数：' + element)
        ele = waitElement(driver, et['类型'], element)
    else:
        ele = waitElement(driver, et['类型'], et['参数'])
    if ele is not None:
        loginfo('已找到元素: 【' + et['类型'] + '|' + et['参数'] + '】')
    else:
        logerror('未找到元素: 【' + et['类型'] + '|' + et['参数'] + '】')
    return ele


def accepAlert(driver, page, element=None):
    et = get_detail_yaml(page, element)
    el = getElement(driver, et['类型'], et['参数'])
    if el is not None:
        el.click()


def getElement(driver, e_type, param):
    """
    查找元素
    :param driver:
    :param e_type:
    :param param:
    :return element
    """
    i = 0
    element = None
    while i < 3:
        try:
            if e_type == 'id':
                element = driver.find_element_by_id(param)
            elif e_type == 'name':
                element = driver.find_element_by_name(param)
            elif e_type == 'className':
                element = driver.find_element_by_class_name(param)
            elif e_type == 'linkText':
                element = driver.find_element_by_link_text(param)
            elif e_type == 'xpath':
                element = driver.find_element_by_xpath(param)
            elif e_type == 'ios_predicate':
                element = driver.find_element_by_ios_predicate(param)
            elif e_type == 'android_uiautomator':
                element = driver.find_element_by_android_uiautomator('new UiSelector().text("'+ param +'")')
            break
        except:
            i = i + 1
            time.sleep(1)
    return element


def waitElement(driver, e_type, param):
    """
    等待元素出现
    :param driver:
    :param e_type:
    :param param:
    :return element
    """
    i = 0
    element = None
    while i < 3:
        accepAlert(driver, '以后再说')
        loginfo('开始查找元素: 【' + e_type + '|' + param + '】')
        try:
            if e_type == 'id':
                element = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_id(param))
            elif e_type == 'name':
                element = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_name(param))
            elif e_type == 'className':
                element = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_class_name(param))
            elif e_type == 'linkText':
                element = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_link_text(param))
            elif e_type == 'xpath':
                element = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_xpath(param))
            elif e_type == 'ios_predicate':
                element = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_ios_predicate(param))
            elif e_type == 'android_uiautomator':
                element = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_android_uiautomator('new UiSelector().text("'+ param +'")'))
            break
        except:
            logerror('查找元素超时: 【' + e_type + '|' + param + '】 ' + str(i+1) + '次')
            i = i + 1
            time.sleep(1)
    return element


def accept_alert(driver):
    """
    允许系统弹窗
    :param driver:
    :return:
    """
    loginfo('允许系统弹窗')
    driver.switch_to.alert.accept()


def get_text(driver, page):
    """
    获取元素文本
    :param page:
    :param driver:
    :return:
    """
    el = finElement(driver, page)
    if el is not None:
        return el.text


def get_toast_text(driver, msg, timeout=15, poll_frequency=0.01):
    """
    ########################################
    描述：获取Toast的文本信息
    参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
    返回值：返回与之匹配到的toast信息
    异常描述：none
    ########################################
    """
    # toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
    # toast = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_element))
    message = '//*[@text=\'{}\']'.format(msg)
    toast_element = WebDriverWait(driver, 5, timeout, poll_frequency).until(lambda x: x.find_element_by_xpath(message))
    print(toast_element.text)
    return toast_element.text
