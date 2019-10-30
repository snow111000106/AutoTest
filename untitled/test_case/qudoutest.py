#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from library import operation
from time import sleep
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Mytest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '6.0'  # 设备系统版本
        desired_caps['deviceName'] = 'LZKNWCLZUOJZ5HPF'  # 设备名称
        desired_caps['appPackage'] = 'com.xingjiabi.shengsheng'
        desired_caps['appActivity'] = 'com.xingjiabi.shengsheng.app.SplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

    def test_case(self):
        sleep(2)
        try:
            operation.swipe_down(self, 100)
            WebDriverWait(self.driver, 60).until(
                    lambda x: x.find_element_by_id('com.xingjiabi.shengsheng:id/live_forum_chest_enter_icon'))
            self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/live_forum_chest_enter_icon').click()
            sleep(2)
            self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/tv_live_lucky_money_enter').click()
            sleep(6)
            self.driver.tap([(234, 199), (308, 238)], 100)
            sleep(2)
            operation.continuity_click(self, 'com.xingjiabi.shengsheng:id/iv_live_gift_super', 20)
            sleep(1)
        except Exception as e:
                print(e)
        finally:
            sleep(2)
            self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/watch_live_close').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
