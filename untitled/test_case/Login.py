#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, sys,csv
from time import sleep
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Mytest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '6.0'  # 设备系统版本
        desired_caps['deviceName'] = 'LZKNWCLZUOJZ5HPF'  # 设备名称
        desired_caps['app'] = os.path.abspath('/Users/snow/Downloads/app-huawei-release_6434.apk')
        #desired_caps['appPackage'] = 'com.xingjiabi.shengsheng'
        #desired_caps['appActivity'] = 'com.xingjiabi.shengsheng.app.SplashActivity'
        # desired_caps['appWaitActivity'] ='com.xingjiabi.shengsheng.mine.XjbLoginActivity'
        desired_caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

    def login(self, username, passwd):
        sleep(3)
        self.driver.swipe(700, 200, 100, 200, 500)
        sleep(3)
        self.driver.swipe(700, 200, 100, 200, 500)
        sleep(3)
        self.driver.swipe(700, 200, 100, 200, 500)
        sleep(3)
        self.driver.swipe(700, 200, 100, 200, 500)
        sleep(3)
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/tvSelectGirl').click()
        sleep(3)
        self.driver.find_elements_by_id('com.xingjiabi.shengsheng:id/imgTab')[4].click()
        sleep(3)
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/btnLogin').click()
        self.driver.wait_activity('com.xingjiabi.shengsheng.mine.XjbLoginActivity', 5, 1)
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/xjb_login_name').send_keys(username)
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/xjb_login_psd').send_keys(passwd)
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/xjb_login_but').click()

    def find_toast(self, text):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    def test_case(self):
        csvfile = open('F:/snow/autoTest/untitled/data/login_test.csv', 'r')
        csvreader = csv.reader(csvfile)

        for line in csvreader:
            name = line[0]
            password = line[1]
            self.login(name, password)
            sleep(3)
            activity = self.driver.current_activity()
            print(activity)
            if self.driver.current_activity() == 'com.xingjiabi.shengsheng.app.NavigationActivity':
                print('case pass1')
            elif self.driver.find_element_by_id(
                    'com.xingjiabi.shengsheng:id/md_content').text == '用户名或者密码输错啦，好好想想~ 错误码（a1208）':
                print('case pass2')
            elif find_toast("密码错误，请重新输入"):
                print('case pass3')
            else:
                print('case filed1')
            self.driver.clear()
        csvfile.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
