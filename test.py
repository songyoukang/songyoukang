from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,strftime
from selenium.webdriver.support.select import Select
#导入鼠标操作类
from selenium.webdriver import ActionChains
#导入pytest框架
import pytest
#用例跳过
from alien_invation.songyoukang.until import Until_driver

version=24
#测试用例,setup 和teardown
class Testdomo(object):
    def setup(self):
        #Until_driver().get_driver()
        self.driver=Until_driver()
        self.driver.get_driver()
        # #导入实例浏览器
        # self.driver=webdriver.Chrome()
        # #导入鼠标操作
        # action=ActionChains(self.driver)
        # #隐式等待
        # self.driver.implicitly_wait(10)
        # #获取URL
        # self.driver.get('http://www.baidu.com')
        # sleep(5)
        #获取cookie,添加cookie
        #cookie_value={'name':'BDUSS','value':'DNkNlBNMUdSSnp4OEhMV21VaTRsOTNqblN2WlRtfnhTSHVDbEhyb3pZcWUycEZpSVFBQUFBJCQAAAAAAAAAAAEAAACeuhJQu7XE0LqisMnT0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ5NamKeTWpiR'}
        #driver.add_cookie(cookie_value)
        #cookie_value={'name':'token','value':'Bearer%20eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsImp0aSI6ImJiNmNlYzM0LWU0NWUtNGQ4Zi05OGM4LTU3MDgyODVkMGIwYiIsImlhdCI6MTY1MTEzNTQxNywiZXhwIjoxNjUxMjIxODE3LCJsb2dpbklkIjoiMzg4NjMyMjA3Nzg1MzA0MDY0IiwiZm9yY2VSZXNldFB3ZCI6ZmFsc2UsInJvbGVJZHMiOiIzOTQ1NDk0NDY2MTkyODc1NTIsMzk0NTQ5NDQ4NTAyNTMwMDQ4LDM5NDU0OTQ0ODA2NjMyMjQzMiIsIm9yZ0lkcyI6IjMyMDMwNTEwMjAwMSIsImxvZ2luQ2hhbm5lbCI6IndlYiIsInVzZXJJcCI6IjE3Mi4xNi4xMDAuMTcyIn0.wUHdrG0t2wKQtnxit06J9VUhefATP3hrf-SzPx5cLUU'}
        #driver.add_cookie(cookie_value)
    def test1(self):
        self.driver.refresh()
        sleep(5)
        print("111111")
        #最大窗口
        self.driver.maximize_window()
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('name,age', [("宋友康", 25), ("cs", 28)])
    def test2(self, name, age):
        print(f'我的名字是\n{name}{age}')
        print("我的名字是\n{}{}".format(name, age))
    def fun_med(self, num1, num2):
        return num1 + num2
        # class Testdomo1(object):
    def test_fun(self):
        result = Testdomo().fun_med(1, 2)
        assert 3 == result
    def teardown(self):
        self.driver.quit()
    #@pytest.mark.skipif(version!=25,reason="版本不正确，跳过")
if __name__ == '__main__':
    pytest.main(['-s', 'test.py'])
















#截图保存，防止文件被覆盖,传入时间戳
# now_time=strftime('%Y%m%d_%H%M%S')
# driver.get_screenshot_as_file("./a_{}.png".format(now_time))
# #打印窗口文本
# print(driver.title)
# #switch_to.frame()默认可以直接使用表单(frame/iframe)的id或name属性。如果表单没有id和name属性，可以使用元素定位方法先找到这个表单，再切换进去
# iframe=driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/div[2]/iframe')
# driver.switch_to.frame(iframe)
# sleep(3)
# driver.find_element_by_xpath('//*[@id="wrap"]/a[1]/span').click()
# #切回主页面
# #driver.switch_to.default_content()
# #窗口切换,(handles[-1]) 代表窗口的最后一个页面，也就是最新的页面
# handles=driver.window_handles
# print(handles)
# driver.switch_to.window(handles[1])
# sleep(5)
# driver.close()
# sleep(5)
# driver.switch_to.window(handles[0])
# # #只针对标签为select的标签可以使用
# # move=driver.find_element_by_xpath("//*[@id='s-usersetting-top' and @name='tj_settingicon']")
# # action.move_to_element(move).perform()
# # sleep(3)
# # driver.find_element_by_xpath("//a[contains(@href,'https://www.baidu.com/duty/privacysettings.html')]").click()
# # sleep(3)
# # driver.find_element_by_xpath("//a[contains(@href,'https://www.baidu.com/duty/privacysettings.html')]").click()
#
# #滚动条（X，Y） 0代表原点，1000代表向下移动1000
# js="window.scrollTo(0,1000)"
# driver.execute_script(js)
# select=Select(sel)
# select.select_by_value(2)
# select.select_by_index()
# sel.select_by_visible_text("安徽")
# sleep(3)
#获取弹出窗口,非alert是自定义窗口，无需该处理
#alert=driver.switch_to.alert
#打印弹窗文本
# print(alert.text)
# #同意
# alert.accept()
# #移除弹窗
# alert.dismiss()
# # # 输入后键盘操作
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
# elements=driver.find_element_by_css_selector('h5')
# element=elements.text
# aa=(str(element))
# print(aa)·
# sleep(3)

