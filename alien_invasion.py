from selenium import webdriver
import time
from PIL import Image
import random
from pytesseract import image_to_string
import urllib.request
yuming=(random.randint(11,1000))
from system import *
a=0
def test(a):
    while  a<5 :
        table_text = TestHtml()
        table_text.login()
        if table_text!="登录":
            a+=1
        else:
            # 执行登陆成功后的操作
            test.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/ul/li[2]/div').click()
            test.driver.find_element_by_xpath("//span[contains(text(),'租户管理')]").click()
            test.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/ul/li[2]/ul/li[1]').click()
            time.sleep(6)
            test.driver.find_element_by_xpath('//*[@id="vue"]/div/div[2]/div/div/div[1]/div/button').click()
            test.driver.find_element_by_xpath(
                '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div[1]/input').send_keys(
                'git')
            test.driver.find_element_by_xpath("//span[contains(text(),'正式')]").click()
            test.driver.find_element_by_xpath(
                '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[5]/div/div/input').send_keys(
                '18206292280')
            test.driver.find_element_by_xpath(
                '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[7]/div/div[1]/input').send_keys(
                yuming)
            time.sleep(10)


test(a)