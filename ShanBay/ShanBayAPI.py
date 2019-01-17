import requests
import dev_config
import json

config = dev_config


class ShanBayAPI(object):
    def __init__(self):
        self.session = requests.Session()

    def __change_session_headers(self, key, value):
        self.session.headers.update({key: value})

    def login(self):
        __method = 'login'

        self.__change_session_headers('content-type', 'application/json')

        url = config.SHANBAY_API[__method]
        post_data = json.dumps(config.SHANBAY_DATA[__method])

        try:
            response = self.session.post(url=url, data=post_data)
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                return False

        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    shanbay = ShanBayAPI()
    print(shanbay.login())
