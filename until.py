from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,strftime
from selenium.webdriver.support.select import Select
#导入鼠标操作类
from selenium.webdriver import ActionChains
#导入pytest框架
import pytest
#用法
#@classmethod
#私有化属性
#driver 改成 __driver


def get_alert_msg(self):
    sleep(2)
    msg=Until_driver.get_driver().find_element_by_xpath("qqq").text
    #print(msg)
    return msg
class Until_driver():
    driver=None
    def get_driver(self):
        if self.driver is None:

            # 导入实例浏览器
            self.driver = webdriver.Chrome()
            # 导入鼠标操作
            action = ActionChains(self.driver)
            # 隐式等待
            self.driver.implicitly_wait(10)
            # 获取URL
            self.driver.get('http://www.baidu.com')
            sleep(5)
        return self.driver

    def close_driver(self):
        if self.driver:
            sleep(3)
            self.driver.quit()

        #获取cookie,添加cookie
        #cookie_value={'name':'BDUSS','value':'DNkNlBNMUdSSnp4OEhMV21VaTRsOTNqblN2WlRtfnhTSHVDbEhyb3pZcWUycEZpSVFBQUFBJCQAAAAAAAAAAAEAAACeuhJQu7XE0LqisMnT0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ5NamKeTWpiR'}
        #driver.add_cookie(cookie_value)
        #cookie_value={'name':'token','value':'Bearer%20eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsImp0aSI6ImJiNmNlYzM0LWU0NWUtNGQ4Zi05OGM4LTU3MDgyODVkMGIwYiIsImlhdCI6MTY1MTEzNTQxNywiZXhwIjoxNjUxMjIxODE3LCJsb2dpbklkIjoiMzg4NjMyMjA3Nzg1MzA0MDY0IiwiZm9yY2VSZXNldFB3ZCI6ZmFsc2UsInJvbGVJZHMiOiIzOTQ1NDk0NDY2MTkyODc1NTIsMzk0NTQ5NDQ4NTAyNTMwMDQ4LDM5NDU0OTQ0ODA2NjMyMjQzMiIsIm9yZ0lkcyI6IjMyMDMwNTEwMjAwMSIsImxvZ2luQ2hhbm5lbCI6IndlYiIsInVzZXJJcCI6IjE3Mi4xNi4xMDAuMTcyIn0.wUHdrG0t2wKQtnxit06J9VUhefATP3hrf-SzPx5cLUU'}
        #driver.add_cookie(cookie_value)

if __name__ == '__main__':
    driver=Until_driver()
    driver.get_driver()
    driver.close_driver()