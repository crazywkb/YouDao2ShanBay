import requests
import dev_config
import json


class ShanBayAPI(object):
    def __init__(self):
        self.session = requests.Session()

    def login(self):
        __method = 'login'
        try:
            response = self.session.post(dev_config.SHANBAY_API[__method], data=json.dumps(dev_config.SHANBAY_DATA[__method]))
            if response.status_code == 200:
                print("Login Success.")
            print(response.text)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    shanbay = ShanBayAPI()
    shanbay.login()
