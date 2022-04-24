from selenium import webdriver
from time import  sleep
from bs4 import  BeautifulSoup
driver=webdriver.Chrome()
#driver.get("http://baidu.com")
driver.get("https://www.tianqi.com/province/jiangsu/15/")
sleep(3)
#driver.find_element_by_id('kw').send_keys('软件测试')
#driver.find_element_by_link_text('更多').click()
iframe_loc = '//iframe[contains(@src,"subAccTransDetail")]'
#self.driver.switch_to.frame(iframe_loc)
elements=driver.find_element_by_xpath('//*[@class="mainWeather"]/ul')
#elements=driver.find_elements_by_class_name('raweather760')
element=elements.text
#elements=driver.find_elements_by_class_name('raweather760')
aa=(str(element))
file='123.txt'
with open(file,'w') as f:
    f.write(aa)









driver.quit()