#coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox()

#第一种方法
def findElement(driver,by,value):
    ''''定位元素，参数locator是元祖类型'''
    element = WebDriverWait(driver, 30, 0.5).until(lambda x: x.find_element(by,value))
    return element
#可以看by的文件
driver.get("https://www.baidu.com")
a = findElement(driver,"id","kw")
a.send_keys("selenium")


#第二种方法
def findElements(driver,locator):
    ''''定位元素，参数locator是元祖类型'''
    elements = WebDriverWait(driver, 30, 0.5).until(lambda x: x.find_element(*locator))
    return elements
loc = ("css selector","#su")
b=findElements(driver,loc)
b.click()

#显示时间封装  8课下优化
#参数，**   百度搜装饰器