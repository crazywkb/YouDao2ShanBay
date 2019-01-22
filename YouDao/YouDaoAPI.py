import requests
from bs4 import BeautifulSoup
import dev_config as config


class YouDaoAPI(object):
    def __init__(self):
        self.session = requests.Session()
        self.__has_login = False
        self.__total_words_sum = 0

    def __change_session_headers(self, key, value):
        self.session.headers.update({key: value})

    def login(self):
        """
        login
        :return: bool
        """
        __method = 'login'
        url = config.YOUDAO_API[__method]
        data = config.YOUDAO_DATA[__method]

        try:
            response = self.session.post(url=url, data=data)
            if config.YOUDAO_ACCOUNT_INFO['username'] not in response.text:
                return False
            self.__has_login = True

        except Exception as e:
            print(e)
            return False
        return True

    def __get_words_num(self):
        __method = 'get_words'
        if not self.__has_login:
            raise Exception("YouDao not login.")

        url = config.YOUDAO_API[__method]
        params = config.YOUDAO_DATA[__method]
        params['p'] = 0

        response = self.session.get(url=url, params=params)
        soup = BeautifulSoup(response.text, 'lxml')
        self.__total_words_sum = int(soup.find('div', attrs={'class': 'right'}).findChildren('strong')[1].text)

    def get_words(self):
        """
        get total word list of youdao's wordbook
        :return: (bool, wordlist)
        """
        __method = 'get_words'

        if not self.__has_login:
            raise Exception("YouDao not login.")

        self.__get_words_num()

        total_words = list()
        url = config.YOUDAO_API[__method]
        params = config.YOUDAO_DATA[__method]

        page_num = 0
        while True:
            params['p'] = page_num
            try:
                response = self.session.get(url=url, params=params)
                soup = BeautifulSoup(response.text, 'lxml')
                word_div = soup.findAll('div', attrs={'class': 'word'})
                words = [word.strong.text for word in word_div]
                total_words.extend(words)

                if len(total_words) >= self.__total_words_sum:
                    # make sure the program can be terminated
                    # if compared by 'equal' operator, there can be a endless loop.
                    return len(total_words) == self.__total_words_sum, total_words

            except Exception as e:
                print(e)
                return False, total_words

            page_num += 1


if __name__ == '__main__':
    api = YouDaoAPI()
    api.login()
    print(api.get_words())
