# coding:utf-8


login_url = "http://192.168.1.16/"

class LoginPage:
    # 定位用户名
    account_loc = ("xpath", '//*[@id="userName"]')
    # 定位密码
    psw_loc = ("xpath", '//*[@id="password"]')
    # 定位登录按钮
    login_loc = ("class name", 'ant-btn-primary')
    #引入上面元素
    def open_url(self):
        self.open(login_url)

    def input_account(self,acc):
        self.send_keys(self.account_loc,acc)

    def input_psw(self,psw):
        self.send_keys(self.psw_loc,psw)

    def clicl_button(self):
        # self.click(self.account_loc)$('.ant-btn-primary').click()
        js = "document.getElementsByClassName('ant-btn-primary')[0].click()"
        driver.execute_script(js)

    def login(self,acc="admin",psw="123456"):
        print("开始登录：%s  %s"%(acc,psw))
        self.open_url()
        self.input_account(acc)
        self.input_psw(psw)
        self.clicl_button()

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.open(login_url)
    login.login()

