from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from time import sleep



class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.poll = 1

    def findElement(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElementNew(self, loctor):
        # 找到了返回element，没找到抛异常
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(loctor))
        return element
        '''EC.presence_of_element_located是判断元素可见不可见，（loctor）本身就是元祖不需要加*，直接写“id”，“kw”元素就好'''
    def findElementsNew(self, loctor):
        '''找到了返回list, 没找到抛异常'''
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elements

    # def visible(self, loctor):
    #     '''一直等待某个元素可见'''
    #     try:
    #         ui.WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(loctor))
    #         return True
    #     except TimeoutException:
    #         return False

    def findElements(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_elements(*loctor))
        return elements

    def sendKeys(self, loctor, text):
        '''键盘输入事件'''
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def click(self, loctor):
        '''鼠标单击事件'''
        ele = self.findElement(loctor)
        ele.click()

    def click_kj(self,loctor):
        ''' 判断元素是否存在，存在点击，不存在sleep一下点击'''
        try:
            ele = self.findElementNew(loctor)
        except TimeoutException:
            print("未找到元素：")
            sleep(2)
            ele.click()
        except WebDriverException:
            sleep(2)
            ele.click()
        else:
            print('元素可见')
            ele.click()




    def Right_click(self,right):
        '''鼠标右键点击事件'''
        qqq = self.findElement(right)
        ActionChains(self.driver).context_click(qqq).perform()

    def Mouse_click(self, mouse):
        '''鼠标双击事件'''
        aaa = self.findElement(mouse)
        ActionChains(self.driver).double_click(aaa).perform()


    def clicks(self,loctor):
        ele = self.findElements(loctor)
        # print(len(ele))
        ele[3].click()
#****************************************************************************************************************
    # def iframe(self,a):
    #     frame = self.driver.find_element_by_id(a)  # iframe 定位
    #     self.driver.switch_to_frame(frame)

    def element_f(self):
        '''判断元素是否存在'''
        try:
            self.driver.find_element_by_xpath(" ").is_displayed()
        except :
            print("未找到元素")
            # sleep(1)
            # ele = self.findElement(loctor)
            # ele.click()
        else:
            print("元素存在")
            # ele = self.findElement(loctor)
            # ele.click()
    #
    # def is_element_visible(self, element):
    #     driver = self.driver
    #     try:
    #         the_element = EC.visibility_of_element_located(element)
    #         assert the_element(driver)
    #         flag = True
    #     except:
    #         flag = False
    #     return flag
    #
    #     the_element = is_element_visible(self, element)
    #     if the_element:
    #         print("元素出现")
    #     else:
    #         time_start = datetime.now()
    #         while not the_element:
    #             recheck_the_element = is_element_visible(self, element)
    #             time_now = datetime.now()
    #             if recheck_the_element:
    #                 print("元素出现")
    #                 break
    #             # 此处超时时限设置为10秒
    #             elif (time_now - time_start).seconds > 10:
    #                 print("元素是无形的!")
    #                 break
    #             else:
    #                 continue
#*********************************************************************************************************************