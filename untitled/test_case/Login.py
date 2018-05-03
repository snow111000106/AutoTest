# coding=utf-8
import os, sys,csv
from time import sleep
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Mytest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '4.3'  # 设备系统版本
        desired_caps['deviceName'] = 'emulator-5554'  # 设备名称
        desired_caps['app'] = os.path.abspath('/Users/snow/Downloads/app-huawei-release_6434.apk')
        #desired_caps['appPackage'] = 'com.xingjiabi.shengsheng'
        desired_caps['appActivity'] = 'com.xingjiabi.shengsheng.app.NavigationActivity'
        desired_caps['appWaitActivity'] ='com.xingjiabi.shengsheng.mine.XjbLoginActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app


    def login(self,username,passwd):
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/tvXjbLoginTab').click()
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/xjb_login_name').send_keys(username)
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/xjb_login_psd').send_keys(passwd)
        self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/xjb_login_but').click()


    def test_case(self):
        csvfile = file('/Users/snow/PycharmProjects/untitled/data/login_test.csv', 'rb')
        reader = csv.reader(csvfile)

        for line in reader:
            name=line[0]
            password=line[1]
            #account_name=line[2]
            self.login(name,password)
            sleep(5)
            try:
                #A=self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/tvAccountName').text
                self.assertIsNotNone(self.driver.find_element_by_id('com.xingjiabi.shengsheng:id/tvAccountName'),'case filed')
                print ('case pass')
            except NoSuchElementException:
                print ('NoSuchElementException')
            except:
                print('error')
            self.driver.reset()
        csvfile.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
