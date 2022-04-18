from selenium import webdriver
import time
from PIL import Image
import random
from pytesseract import image_to_string
import urllib.request
yuming=(random.randint(11,1000))

class TestHtml():
    def __init__(self):
        # 驱动chrome浏览器
        self.driver = webdriver.Chrome("chromedriver.exe")
        # 获取测试环境地址
        self.driver.get("http://114.217.52.94:8081")
        time.sleep(3)
        # 窗口最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def login(self):
        # 刷新页面
        self.driver.refresh()
        # admin登录
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/section/main/div/section/div/div[2]/div[2]/div/div/form/div[1]/div/div/input').send_keys(
            "admin")
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/section/main/div/section/div/div[2]/div[2]/div/div/form/div[2]/div/div/input').send_keys("123456")
        #获取代码

        self.pic= self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/section/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/img')
        print("qwe")
        # 获取验证码的src属性
        pic_url = self.pic.get_attribute('src')
        #保存验证码图片到指定路径
        urllib.request.urlretrieve(pic_url, 'C:\\Users\\admin\\aa.jpg')
        self.img =Image.open(r"C:\\Users\\admin\\aa.jpg")
        time.sleep(1)
        pt = (image_to_string(self.img))
        print(pt)
        # 输入二维码
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/section/main/div/section/div/div[2]/div[2]/div/div/form/div[3]/div/div[1]/input').send_keys(pt)
        time.sleep(6)
        # 点击登录
        self.driver.find_element_by_xpath("//span[contains(text(),'登录')]").click()
        self.test=self.driver.find_element_by_xpath("//span[contains(text(),'登录')]").text
        return (self.test)
        # 测试下登陆成功aa是不是False
            #self.a=self.driver.find_element_by_xpath("//span[contains(text(),'数字大屏')]").text
            # # 执行登陆成功后的操作
            # self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/ul/li[2]/div').click()
            # self.driver.find_element_by_xpath("//span[contains(text(),'租户管理')]").click()
            # self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/ul/li[2]/ul/li[1]').click()
            # time.sleep(6)
            # self.driver.find_element_by_xpath('//*[@id="vue"]/div/div[2]/div/div/div[1]/div/button').click()
            # self.driver.find_element_by_xpath(
            #     '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div[1]/input').send_keys(
            #     'git')
            # self.driver.find_element_by_xpath("//span[contains(text(),'正式')]").click()
            # self.driver.find_element_by_xpath(
            #     '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[5]/div/div/input').send_keys(
            #     '18206292280')
            # self.driver.find_element_by_xpath(
            #     '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[7]/div/div[1]/input').send_keys(
            #     yuming)
            # time.sleep(10)









if __name__ == '__main__':
    test_html = TestHtml()
    test_html.login()








# self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/ul/li[2]/div').click()
# self.driver.find_element_by_xpath("//span[contains(text(),'租户管理')]").click()
# self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/ul/li[2]/ul/li[1]').click()
# time.sleep(6)
# self.driver.find_element_by_xpath('//*[@id="vue"]/div/div[2]/div/div/div[1]/div/button').click()
# self.driver.find_element_by_xpath(
#     '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div[1]/input').send_keys(
#     'git')
# self.driver.find_element_by_xpath("//span[contains(text(),'正式')]").click()
# self.driver.find_element_by_xpath(
#     '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[5]/div/div/input').send_keys(
#     '18206292280')
# self.driver.find_element_by_xpath(
#     '//*[@id="vue"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/form/div[7]/div/div[1]/input').send_keys(
#     yuming)
# time.sleep(10)
# self.driver.quit()
# self.driver.back()
# self.driver.forward()
#self.driver.refresh()

# jymi_loc = '//span[text()="租户管理"]'
#
# self.driver.find_element_by_xpath(jymi_loc).click()
# time.sleep(5)
#
# #  frame 切换
# iframe_loc = '//iframe[contains(@src,"subAccTransDetail")]'
# # self.driver.switch_to.frame(iframe_loc)
# self.driver.switch_to.frame(self.driver.find_element_by_xpath(iframe_loc))
#
# time.sleep(1)
#
# start_date_loc = '//input[@id="STARTDATE$text"]'
# end_date_loc = '//input[@id="ENDDATE$text"]'
# self.driver.find_element_by_xpath(start_date_loc).send_keys('2021-07-06')
# self.driver.find_element_by_xpath(start_date_loc).send_keys('2021-07-06')
#
# cx_loc ='//span[text()="查询"]'
# self.driver.find_element_by_xpath(cx_loc).click()
#
# time.sleep(2)
# menu_table=self.driver.find_element_by_xpath('//div[@class="mini-panel-body mini-grid-rows"]')
# # text = menu_table.text
# text = self.driver.page_source
# handles = self.driver.window_handles
# self.driver.switch_to.window(self.driver.window_handles[-1])

#return text





