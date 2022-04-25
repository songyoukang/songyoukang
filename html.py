from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.tianqi.com/province/jiangsu/15/')

text=driver.find_elements_by_css_selector('h5')
text.text
print(str(aa))
sleep(3)
driver.quit()