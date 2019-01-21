import json

import requests

import dev_config

config = dev_config


class ShanBayAPI(object):
    def __init__(self):
        self.session = requests.Session()
        self.__has_login = False

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
                self.__has_login = True
                return json.loads(response.text)
            else:
                return False

        except Exception as e:
            print(e)
            return False

    def add_to_vocabulary(self, words):
        __method = 'add_vocabulary'
        url = config.SHANBAY_API[__method]
        params = config.SHANBAY_DATA[__method]

        params['words'] = '\n'.join(words)
        self.__change_session_headers('x-requested-with', 'XMLHttpRequest')

        try:
            response = self.session.get(url=url, params=params)
            if response.status_code == 200:
                failed_list = json.loads(response.text)['notfound_words']
                return response.text, failed_list

            else:
                return False, None

        except Exception as e:
            print(e)
            return False, None


if __name__ == '__main__':
    shanbay = ShanBayAPI()
    shanbay.login()
