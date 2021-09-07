import json
import requests

url_WhiteBoard = "http://10.4.107.225:8000/board-management/board"

class TestWhiteBoardMessageSend(object):
    def test_MessageSend_success(self):
        data = {
            "id": "9eb5de4d-76f3-467d-f79a2051b8ba",
            "name": "哈哈哈哈哈",
            "messageType": 1,
            "chatMessage": "",
            "boardMessage": {
                "color": "#000000",
                "size": 1,
                "type": 1,
                "x": 263,
                "y": 118
            }
        }
        response = requests.post(url=url_WhiteBoard, json=data)  # 正确的数据格式为json格式
        print(response.status_code)

    def test_MessageSend_analysisfail(self):
        data = {
            "id": "9eb5de4d-76f3-467d-f79a2051b8ba",
            "name": "哈哈哈哈哈",
            "messageType": 1,
            "chatMessage": "",
            "boardMessage": {
                "color": "#000000",
                "size": 1,
                "type": 1,
                "x": 263,
                "y": 118
            }
        }
        response = requests.post(url=url_WhiteBoard, data=data)  # json.dumps将一个Python数据结构转换为JSON
        print(response.status_code)
        print(response.json())
        res_code = response.json()["code"]
        res_message = response.json()["message"]
        assert res_code == 400000000
        assert res_message == "Invalid request."

#TestWhiteBoardMessageSend().test_MessageSend_success()
#TestWhiteBoardMessageSend().test_MessageSend_analysisfail()