from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains
#导入实例浏览器
driver=webdriver.Chrome()
#导入鼠标操作
action=ActionChains(driver)
#隐式等待
driver.implicitly_wait(10)
#获取URL
driver.get('https://www.tianqi.com/province/jiangsu/15/')
sleep(3)


driver.maximize_window()
print(driver.title)
test=driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[2]/ul/li[1]')
# 输入后键盘操作
test.send_keys(Keys.BACK_SPACE)
#右击鼠标
action.context_click(test).perform()
#双击鼠标
#action.double_click(test)
#悬停鼠标
move=driver.find_element_by_xpath('/html/body/div[4]/ul/li[2]/a')
action.move_to_element(move).perform()
sleep(3)
#action.perform()

#元素拖拽
#action.drag_and_drop(元素a,元素b)
# sleep(3)
# action.perform()
# driver.back()
# #driver.forward()
# driver.refresh()
# ab=driver.current_url
# bb=driver.title
# print(ab,bb)
#
# elements=driver.find_element_by_css_selector('h5')
# element=elements.text
# aa=(str(element))
# print(aa)
# sleep(3)
driver.quit()
