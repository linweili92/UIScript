#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/5/24
from appium import webdriver
from behave import *
from common.AppiumUtil import swipLeft, clickElement, finElement
from common import GlobalVar as gl
import time
gl.init()

if __name__ == '__main__':
    self.driver = webdriver.Remote()


@when('启动APP')
def start_app(self):
    self.driver.wait_activity('.activity.welcome.SplashActivity', 5)
    swipLeft(self.driver, n=3)
    clickElement(self.driver, '开始体验')
    clickElement(self.driver, '以后再说')
    # el1 = self.driver.find_element_by_id("cn.carhouse.yctone:id/no")
    #
    # if el1 is not None:
    #     el1.click()


@then('重新启动APP')
def restart_app(self):
    self.driver.start_activity('cn.carhouse.yctone', '.activity.welcome.SplashActivity')
    # context.driver.find_element_by_accessibility_id("爱车小屋商户").click()
    self.driver.wait_activity('.activity.welcome.SplashActivity', 3)
    # web_driver_wait(self.driver, 'cn.carhouse.yctone:id/tab_icon')
    time.sleep(5)


@given('未登录')
def un_login(self):
    if gl.get_value('login') is True:
        clickElement(self.driver, '我')
        if finElement(self.driver, '我', '请登录账户') is None:
            clickElement(self.driver, '我', '设置')
            clickElement(self.driver, '我', '退出登录')
            if finElement(self.driver, '我', '请登录账户') is not None:
                gl.set_value('login', False)
                print('用户已退出登录')
    else:
        print('用户未登录')
        gl.set_value('login', False)


@given('已登录')
def is_login(self):
    if gl.get_value('login') is False:
        clickElement(self.driver, '我')
        if finElement(self.driver, '我', '请登录账户') is not None:
            clickElement(self.driver, '我', '请登录账户')
            clickElement(self.driver, '我', '手机登录')
            send_keys(self, '我', '请输入手机号', gl.get_value('uname'))
            send_keys(self, '我', '请输入密码', gl.get_value('pwd'))
            clickElement(self.driver, '我', '登录')
            if finElement(self.driver, '我', '用户名') is not None:
                gl.set_value('login', True)
                print('用户登录成功')
            else:
                print('登录失败')
    else:
        gl.set_value('login', True)
        print('用户已登录')


@given('点击底部的我')
def click_me(self):
    time.sleep(3)
    clickElement(self.driver, '我')


@when('选择{env}环境')
def select_env(self, env):
    time.sleep(3)
    clickElement(self.driver, '我', '我的评价')
    if env == '测试':
        env_str = '测试(dev)'
    elif env == '预正式':
        env_str = '预正式'
    elif env == '正式':
        env_str = '正式'
    clickElement(self.driver, '环境', env_str)


@given('看见{page}|{element}')
def find_element(self, page, element):
    time.sleep(3)
    finElement(self.driver, page, element)


@then('只点击{page}')
def click_page_without_element(self, page):
    time.sleep(3)
    clickElement(self.driver, page)


@then('点击{page}|{element}')
def click_page(self, page, element):
    time.sleep(3)
    clickElement(self.driver, page, element)


@when('在{page}|{element}键入{keys}')
def send_keys(self, page, element, keys):
    time.sleep(3)
    el = finElement(self.driver, page, element)
    if el is not None:
        el.clear()
        el.send_keys(keys)


@given('检查到{page}|{element}相关信息')
def valid_text(self, page, element=None):
    time.sleep(3)
    res = finElement(self.driver, page, element)
    assert res.text is not None, '未获取到元素信息：' + param



@then('标记{info}')
def sign_log(self, info):
    gl.set_value('login', True)
    print('标记' + info)


@then('sleep{mn}秒')
def sleep_m(self, mn=2):
    time.sleep(int(mn))


@when('返回上一级')
def sleep_m(self):
    time.sleep(5)
    clickElement(self.driver, '返回上一级')


@when('返回上2级')
def sleep_m(self):
    time.sleep(3)
    clickElement(self.driver, '返回上一级')
    clickElement(self.driver, '返回上一级')