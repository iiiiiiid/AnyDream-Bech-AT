import json
import requests

url_WhiteBoard = "http://10.4.107.225:8000/board-management/board"
url_WhiteBoard_id = "http://10.4.107.225:8000/board-management/board/9eb5de4d-76f3-467d-f79a2051b8ba"

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
        response = requests.post(url=url_WhiteBoard, json=data)
        print(response.status_code)

    def test_DEL_success(self):
        response = requests.delete(url=url_WhiteBoard_id)
        print(response.status_code)

    def test_RESTORE_success(self):
        response = requests.get(url=url_WhiteBoard_id)
        print(response.status_code)

#TestWhiteBoardMessageSend().test_MessageSend_success()#发送白板消息
#TestWhiteBoardMessageSend().test_DEL_success()#撤销
#TestWhiteBoardMessageSend().test_RESTORE_success()#取消撤销