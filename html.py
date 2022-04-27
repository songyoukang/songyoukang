from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
#导入鼠标操作类
from selenium.webdriver import ActionChains
#导入实例浏览器
driver=webdriver.Chrome()
#导入鼠标操作
action=ActionChains(driver)
#隐式等待
driver.implicitly_wait(10)
#获取URL
driver.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=62095104_35_oem_dg&wd=selenium%E4%B8%AD%E9%BC%A0%E6%A0%87%E6%82%AC%E6%B5%AE&oq=selenium%25E4%25B8%25AD%25E9%25BC%25A0%25E6%25A0%2587%25E6%2582%25AC%25E6%25B5%25AE&rsv_pq=eec5c2dd0003a835&rsv_t=1d9dTpJFg2PoZzLILi8CM4Mis9sExkQKXxn41pV3KSuVLkBjJKkVHAu9T8bLnqp1Sctl5NY1G9BS&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t')
sleep(3)


driver.maximize_window()
print(driver.title)
# #只针对标签为select的标签可以使用
# move=driver.find_element_by_xpath("//*[@id='s-usersetting-top' and @name='tj_settingicon']")
# action.move_to_element(move).perform()
# sleep(3)
# driver.find_element_by_xpath("//a[contains(@href,'https://www.baidu.com/duty/privacysettings.html')]").click()
# sleep(3)
# driver.find_element_by_xpath("//a[contains(@href,'https://www.baidu.com/duty/privacysettings.html')]").click()

#滚动条（X，Y） 0代表原点，1000代表向下移动1000
js="window.scrollTo(0,1000)"
driver.execute_script(js)



# select=Select(sel)
# select.select_by_value(2)
# select.select_by_index()
# sel.select_by_visible_text("安徽")
# sleep(3)
#获取弹出窗口,非alert是自定义窗口，无需该处理
alert=driver.switch_to.alert
#打印弹窗文本
print(alert.text)
#同意
alert.accept()
#移除弹窗
alert.dismiss()
# # 输入后键盘操作
# test.send_keys(Keys.BACK_SPACE)
# #右击鼠标
# action.context_click(test).perform()
# #双击鼠标
# #action.double_click(test)
# #悬停鼠标
# move=driver.find_element_by_xpath('/html/body/div[4]/ul/li[2]/a')
# action.move_to_element(move).perform()
# sleep(3)
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
