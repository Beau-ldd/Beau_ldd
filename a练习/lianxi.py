#coding=utf-8
import requests
import unittest
class V2exAPITestCase(unittest.TestCase):

    def test(self):
        url = "https://www.v2ex.com/api/nodes/show.json"
        querystring = {"name":"python"}
        response = requests.request("GET", url, params=querystring).json()
        self.assertEqual(response['name'],'python')
        self.assertEqual(response['id'],90)
if __name__ == '__main__':
    unittest.main()

import requests

url = "http://admin.modo35.com/OA/Login"
headers = {'cache-control': "no-cache", 'postman-token': "7d0c28b1-37a7-a96e-ce65-13d45e22b992"}

response = requests.request("GET", url, headers=headers).json()

print(response.text)