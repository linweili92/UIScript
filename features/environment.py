#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/5/24
from appium import webdriver
import os, sys
from common.YamlUtil import load_yaml
from common import GlobalVar as gl
gl.init()


# 执行功能之前
def before_all(self):
    gl.set_value('login', False)
    get_capabilities(self)
    if gl.get_value('platformName') == 'Android':
        if not gl.get_value('stf'):
            change_param(self, 'deviceName')
            change_param(self, 'platformVersion')
            change_param(self, 'appPackage')
            change_param(self, 'appActivity')
        else:
            print('connect to stf')
    else:
        print('ios device dosomething')


# 执行场景之前
def before_feature(self, feature):
    gl.set_value('login', False)
    if gl.get_value('platformName') == 'Android':
        self.driver = webdriver.Remote(
            command_executor='http://' + gl.get_value('appium_url') + '/wd/hub',
            desired_capabilities={
                'app': gl.get_value('apps'),
                'automationName': gl.get_value('automationName'),
                'platformName': gl.get_value('platformName'),
                'platformVersion': gl.get_value('platformVersion'),
                'deviceName': gl.get_value('deviceName'),
                'noReset': gl.get_value('noReset'),
                'appPackage': gl.get_value('appPackage'),
                'appActivity': gl.get_value('appActivity')
            })
    elif gl.get_value('platformName') == 'ios':
        print('ios remote      ')


# 执行步骤之后
def after_step(self, step):
    pass


# 执行场景之后
def after_feature(self, feature):
    pass


# 执行功能之后
def after_all(self):
    self.driver.close()


# 获取config.yaml配置信息
def get_capabilities(self):
    change_param(self, 'appium_url')  # Appium服务地址
    change_param(self, 'platformName')  # 测试平台 IOS 或 ANDROID
    change_param(self, 'apps')  # 待测APP路径
    change_param(self, 'stf')  # 是否使用stf设备
    change_param(self, 'uname')  # 是否使用stf设备
    change_param(self, 'pwd')  # 是否使用stf设备


def change_param(self, param):
    # 获取behave执行命令时附带的参数
    userdata = self.config.userdata
    if param == 'apps':
        if userdata.get(param) is None:
            if gl.get_value('platformName') == 'Android':
                config = os.path.abspath('.\\apps\\B_520_2.8.6_test01.apk')
                gl.set_value(param, config)
            else:
                print('ios app path')
        else:
            gl.set_value(param, userdata.get(param))
    else:
        if userdata.get(param) is None:
            config = os.path.join(os.path.dirname(__file__), 'config.yaml')
            gl.set_value(param, load_yaml(config)[param])
        else:
            gl.set_value(param, userdata.get(param))