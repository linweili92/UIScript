#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/5/24
from appium import webdriver
from behave import *
from common.AppiumUtil import swipLeft, clickElement, finElement
from common import GlobalVar as gl
from common.LogUtil import logerror, loginfo
import time
gl.init()

if __name__ == '__main__':
    self.driver = webdriver.Remote()


@when('启动APP')
def start_app(self):
    loginfo('启动APP')
    loginfo('等待启动页')
    self.driver.wait_activity('.activity.welcome.SplashActivity', 5)
    swipLeft(self.driver, n=3)
    loginfo('点击 【开始体验】')
    clickElement(self.driver, '开始体验')


@then('重新启动APP')
def restart_app(self):
    loginfo('重新启动APP')
    self.driver.start_activity('cn.carhouse.yctone', '.activity.welcome.SplashActivity')
    # context.driver.find_element_by_accessibility_id("爱车小屋商户").click()
    self.driver.wait_activity('.activity.welcome.SplashActivity', 3)
    # web_driver_wait(self.driver, 'cn.carhouse.yctone:id/tab_icon')
    time.sleep(5)


@given('未登录')
def un_login(self):
    if gl.get_value('login') is True:
        loginfo('点击 【我】')
        clickElement(self.driver, '我')
        if finElement(self.driver, '我', '请登录账户') is None:
            loginfo('点击 【我|设置】')
            clickElement(self.driver, '我', '设置')
            loginfo('点击 【我|退出登录】')
            clickElement(self.driver, '我', '退出登录')
            if finElement(self.driver, '我', '请登录账户') is not None:
                gl.set_value('login', False)
                loginfo('用户已退出登录')
    else:
        loginfo('用户未登录')
        gl.set_value('login', False)


@given('已登录')
def is_login(self):
    if gl.get_value('login') is False:
        loginfo('点击 【我】')
        clickElement(self.driver, '我')
        if finElement(self.driver, '我', '请登录账户') is not None:
            loginfo('点击 【我|请登录账户】')
            clickElement(self.driver, '我', '请登录账户')
            loginfo('点击 【我|手机登录】')
            clickElement(self.driver, '我', '手机登录')
            send_keys(self, '我', '请输入手机号', gl.get_value('uname'))
            send_keys(self, '我', '请输入密码', gl.get_value('pwd'))
            loginfo('点击 【我|登录】')
            clickElement(self.driver, '我', '登录')
            if finElement(self.driver, '我', '用户名') is not None:
                gl.set_value('login', True)
                loginfo('用户登录成功')
            else:
                logerror('登录失败')
    else:
        gl.set_value('login', True)
        loginfo('用户已登录')


@given('点击底部的我')
def click_me(self):
    loginfo('点击底部的我')
    clickElement(self.driver, '我')


@when('选择{env}环境')
def select_env(self, env):
    loginfo('点击 【我|我的评价】')
    clickElement(self.driver, '我', '我的评价')
    if env == '测试':
        env_str = '测试(dev)'
    elif env == '预正式':
        env_str = '预正式'
    elif env == '正式':
        env_str = '正式'
    loginfo('选择' + env + '环境')
    clickElement(self.driver, '环境', env_str)


@given('看见{page}|{element}')
def find_element(self, page, element):
    loginfo('看见 【 ' + page + '|' + element + '】')
    el = finElement(self.driver, page, element)
    assert el is not None, '没有看到元素: ' + element


@when('看见{page}|{element}')
def find_element(self, page, element):
    loginfo('看见 【 ' + page + '|' + element + '】')
    el = finElement(self.driver, page, element)
    assert el is not None, '没有看到元素: ' + element


@then('只点击{page}')
def click_page_without_element(self, page):
    loginfo('只点击 【 ' + page + '】')
    clickElement(self.driver, page)


@given('点击{page}|{element}')
def click_page(self, page, element):
    loginfo('点击 【 ' + page + '|' + element + '】')
    clickElement(self.driver, page, element)


@then('点击{page}|{element}')
def click_page(self, page, element):
    loginfo('点击 【 ' + page + '|' + element + '】')
    clickElement(self.driver, page, element)


@when('点击{page}|{element}')
def click_page(self, page, element):
    loginfo('点击 【 ' + page + '|' + element + '】')
    clickElement(self.driver, page, element)


@when('在{page}|{element}键入{keys}')
def send_keys(self, page, element, keys):
    el = finElement(self.driver, page, element)
    if el is not None:
        el.clear()
        el.send_keys(keys)
        loginfo('在【{}|{}】 输入 {}'.format(page, element, keys))


@when('输入安全密码')
def secret_keys(self):
    for i1 in [1, 2]:
        for i2 in [1, 2, 3]:
            self.driver.find_element_by_xpath(
                '//android.widget.LinearLayout[@resource-id="cn.carhouse.yctone:id/ckb"]/android.widget.LinearLayout/android.widget.LinearLayout[{}]/android.widget.TextView[{}]'.format(i1,i2)).click()
#     self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="cn.carhouse.yctone:id/ckb"]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
#     self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="cn.carhouse.yctone:id/ckb"]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
#     self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="cn.carhouse.yctone:id/ckb"]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[3]').click()
#     self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="cn.carhouse.yctone:id/ckb"]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]').click()
#     self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="cn.carhouse.yctone:id/ckb"]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]').click()
#     self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="cn.carhouse.yctone:id/ckb"]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[3]').click()
#
#
# @given('检查到{page}|{element}相关信息')
def valid_text(self, page, element=None):
    loginfo('检查到【{}|{}】相关信息'.format(page, element))
    res = finElement(self.driver, page, element)
    assert res.text is not None, '未获取到元素信息：' + param


@then('标记{info}')
def sign_log(self, info):
    loginfo('标记{}'.format(info))
    gl.set_value('login', True)
    print('标记' + info)


@then('等待{mn}秒')
def sleep_m(self, mn=2):
    time.sleep(int(mn))


@when('返回上一级')
def sleep_m(self):
    loginfo('返回上一级')
    clickElement(self.driver, '返回上一级')


@then('返回上一级')
def sleep_m(self):
    loginfo('返回上一级')
    clickElement(self.driver, '返回上一级')


@then('返回上级')
def sleep_m(self):
    loginfo('返回上级')
    clickElement(self.driver, '返回上级')


@then('返回财富上一级')
def sleep_m(self):
    loginfo('返回财富上一级')
    clickElement(self.driver, '返回财富上一级')

