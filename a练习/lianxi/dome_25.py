# #coding:utf-8
#
# from bs4 import BeautifulSoup as  bs
# import requests
# request_url= "http://admin.modo33.com/OM/RentCase/Today?BranchID=4&roomType=%E8%AF%B7%E9%80%89%E6%8B%A9&titleName="
# reqonse = bs(requests.get(request_url).text,'lxml')
# print(reqonse)


# import requests     # 导入requests模块
# from bs4 import BeautifulSoup as bs # 从bs4 模块中导入BeautifulSoup模块并命名为bs
#
# request_url = 'https://testerhome.com/topics/4621'  # 请求的url是 上一章的url地址
# response = bs(requests.get(request_url).text , 'lxml') # 返回一个bs对象 ，格式为lxml
#
# print("这篇文章的名字是 ：" , response.h1.string)  # 获取文章标题˜
# print("该文章属于 ：" , response.find('a',{"class":"node"}).text) #获取发表在哪一个技术类型下
# print("该文章的分类为 ： ", response.h2.string)
# print("-------"*10+"这里是获取所有的楼层评论"+"-------"*10)
# for i in response.find_all('div',{"class":"reply"}):
#     print(i.p.text)
# print("-------"*10+"这里是获取所有的楼层评论"+"-------"*10)


class Father():

    def fangzi(self):
        print("父亲的房子")

    def chezi(self):
        print("父亲的车子")

class Mother():

    def piaozi(self):
        print("妈妈的票子")

class sun(Father,Mother):

    def quxifu(self):
        fang = self.fangzi()
        che = self.chezi()
        piao = self.piaozi()

if __name__ == "__main__":
    s = sun()
    s.quxifu()














#
# url= "http://admin.modo33.com/OM/RentCase/Today?BranchID=4&roomType=请选择&titleName="
# r = requests.get(url)
# #请求首页获取整个html页面
# blog = r.content
# #print(blog)
# #用html.parser解析html
# soup = BeautifulSoup(blog,"html.parser")
# #获取所有的class属性为daytitle，返回tag类
# times = soup.find_all(class_="data_roomStatus ft roomtype_0")
# for i in times:
#     print(i.tag)
# title = soup.find_all(class_="data_roomStatus ft roomtype_0")
#
# descs= soup.find_all(class_="data_roomStatus ft roomtype_0")
# for i, j, k in zip(times, title, descs):
#     print(i.a.string)
#     print(j.a.string)
#     print(k.div.contents[0])
#     print(" ")

#爬虫   bs4
#"https://www.qiushibaike.com/"