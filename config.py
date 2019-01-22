from hashlib import md5

YOUDAO_ACCOUNT_INFO = {
    'username': '',
    'password': ''
}

SHANBAY_ACCOUNT_INFO = {
    'account': '',
    'password': ''
}


SHANBAY_API = {
    'login': 'https://apiv3.shanbay.com/bayuser/login',
    'add_vocabulary': 'https://www.shanbay.com/bdc/vocabulary/add/batch'
}

SHANBAY_MAX_SEND_ONE_TIME = 10

SHANBAY_DATA = {
    'login': SHANBAY_ACCOUNT_INFO,
    'add_vocabulary': {
        'words': None,
        # _: 'timestamp' optional
    }
}

YOUDAO_API = {
    'login': 'https://logindict.youdao.com/login/acc/login',
    'get_words': 'http://dict.youdao.com/wordbook/wordlist',
}

YOUDAO_DATA = {
    'login': {
        'app': 'web',
        'tp': 'urstoken',
        'cf': 3,
        'product': 'DICT',
        'username': YOUDAO_ACCOUNT_INFO['username'],
        'password': md5(YOUDAO_ACCOUNT_INFO['password'].encode()).hexdigest(),
    },
    'get_words': {
        'p': None,
    }
}

# YOUDAO_MAX_ITEM_PER_PAGE = 15  # get by query instead.
