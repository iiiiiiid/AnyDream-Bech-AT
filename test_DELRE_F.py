import json
import requests

url_WhiteBoard_id = "http://10.4.107.225:8000/board-management/board/9ba1234512345"

class TestWhiteBoardMessageSend(object):

    def test_DEL_fail(self):
        para = {
            "id": "9ba1234512345"
        }
        response = requests.delete(url=url_WhiteBoard_id, params=para)
        print(response.json())
        print(response.status_code)
        res_code = response.json()["code"]
        res_message = response.json()["message"]
        assert res_code == 404000000
        assert res_message == "Resource not found."

    def test_GETRESTORE_fail(self):
        para = {
            "id": "9ba1234512345"
        }
        response = requests.get(url=url_WhiteBoard_id, params=para)# 把python对象转换成json对象，生成字符串格式
        print(response.json())
        print(response.status_code)
        res = response.json()["message"]
        assert res == "Resource not found."

#TestWhiteBoardMessageSend().test_DEL_fail()#撤销失败
#TestWhiteBoardMessageSend().test_GETRESTORE_fail()#恢复失败