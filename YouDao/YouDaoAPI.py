import requests

import dev_config as config


class YouDaoAPI(object):
    def __init__(self):
        self.session = requests.Session()
        self.__has_login = False

    def __change_session_headers(self, key, value):
        self.session.headers.update({key: value})

    def login(self):
        __method = 'login'
        url = config.YOUDAO_API[__method]
        data = config.YOUDAO_DATA[__method]

        try:
            response = self.session.post(url=url, data=data)
            if config.YOUDAO_ACCOUNT_INFO['username'] not in response.text:
                return False, response.text
        except Exception as e:
            print(e)
            return False

        return True


if __name__ == '__main__':
    api = YouDaoAPI()
    print(api.login())
