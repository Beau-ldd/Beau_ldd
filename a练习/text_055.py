# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('http://119.254.84.142')
driver.maximize_window()
driver.implicitly_wait(6)


driver.find_element_by_xpath('//*[@id="userName"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('admin')
driver.find_element_by_class_name("ant-btn-primary").click()
driver.find_element_by_xpath("//*[text()='日志']").click()
driver.find_element_by_xpath("//*[text()='消耗列表']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='products']").click()   #定位请选择产品与服务器
time.sleep(2)
driver.find_element_by_xpath('//ul[@class="ant-cascader-menu"]/li[1]').click()  #霍去病
time.sleep(2)
driver.find_element_by_xpath('//ul[@class="ant-cascader-menu"][2]/li').click()  #一统大汉
time.sleep(2)
driver.find_element_by_xpath("//*[@id='dates']/span/input[1]").click()  #定位日期框
time.sleep(2)
driver.find_element_by_xpath("//tr[@class='ant-calendar-current-week ant-calendar-active-week']/td[3]/div").click() #定位开始日期
time.sleep(2)
print("555")
driver.find_element_by_xpath("//tr[@class='ant-calendar-current-week ant-calendar-active-week']/td[6]/div").click()   #定位结束日期
time.sleep(10)
driver.quit()












#
#
#
# js="document.getElementsByClassName(\"icon fl \")[0].click()"                 #[0]  是自己生成的排序（0,2,3,4,5,6）  大模块排序写的同一个属性
# driver.execute_script(js)
#
#
# print('打印')
# driver.find_element_by_link_text(u"当日房态").click()
#
# time.sleep(3)
# print('打印')
#
# driver.quit()        #关闭driver