import urllib.request
from selenium import webdriver
import time
import random
from pytesseract import image_to_string
from PIL import Image
import urllib.request
#驱动chrome浏览器
driver=webdriver.Chrome("chromedriver.exe")
#获取测试环境地址
driver.get("http://114.217.52.94:15672/")
#窗口最大化
driver.maximize_window()
#driver.implicitly_wait(6)
#admin登录
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/section/div/div[2]/div[2]/div/div/form/div[1]/div/div/input').send_keys("admin")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/section/div/div[2]/div[2]/div/div/form/div[2]/div/div/input').send_keys("123456")

# 首先对验证码进行定位
pic = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/section/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/img')
# 获取验证码的src属性
pic_url = pic.get_attribute('src')
# 保存验证码图片到指定路径
urllib.request.urlretrieve(pic_url, 'C:\\Users\\admin\\aa.jpg')
img = Image.open(r"C:\\Users\\admin\\aa.jpg")
pt=(image_to_string(img))
print(pt)
# 输入二维码
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/section/div/div[2]/div[2]/div/div/form/div[3]/div/div[1]/input').send_keys(pt)
print("saaaaaaaaaaaaaaaaaaaaaaaaaas")
time.sleep(10)